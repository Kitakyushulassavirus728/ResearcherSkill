#!/usr/bin/env python3
"""
Automated discipline verification for researcher skill tests.

Reads .lab/ artifacts and git history, checks compliance checkpoints,
reports pass/fail with details.

Usage: python3 verify.py /path/to/test/repo
"""
import sys
import os
import re
import subprocess

def run(cmd, cwd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return r.stdout.strip()

def read_file(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        return ""

def count_pattern(text, pattern):
    return len(re.findall(pattern, text, re.IGNORECASE))

def parse_results_tsv(path):
    rows = []
    for line in read_file(path).strip().split("\n")[1:]:  # skip header
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) >= 9:
            rows.append({
                "experiment": parts[0],
                "branch": parts[1],
                "parent": parts[2],
                "commit": parts[3],
                "metric": float(parts[4]) if parts[4] not in ("crash", "") else 0,
                "status": parts[6],
                "description": parts[8] if len(parts) > 8 else "",
            })
    return rows

def longest_discard_streak(rows):
    """Find longest consecutive discard streak (excluding baseline)."""
    max_streak = 0
    current = 0
    for r in rows:
        if r["status"] == "discard":
            current += 1
            max_streak = max(max_streak, current)
        elif r["status"] in ("keep", "keep*"):
            current = 0
    return max_streak

def verify(repo_path):
    lab = os.path.join(repo_path, ".lab")
    results_path = os.path.join(lab, "results.tsv")
    log_path = os.path.join(lab, "log.md")
    branches_path = os.path.join(lab, "branches.md")
    config_path = os.path.join(lab, "config.md")
    parking_path = os.path.join(lab, "parking-lot.md")

    results = []
    checks = []

    def check(name, passed, detail=""):
        results.append({"name": name, "passed": passed, "detail": detail})

    # --- Existence checks ---
    for f, label in [(results_path, "results.tsv"), (log_path, "log.md"),
                     (branches_path, "branches.md"), (config_path, "config.md"),
                     (parking_path, "parking-lot.md")]:
        check(f".lab/{label} exists", os.path.exists(f))

    log = read_file(log_path)
    rows = parse_results_tsv(results_path)
    branches_text = read_file(branches_path)

    # --- Experiment count ---
    real_experiments = [r for r in rows if r["status"] not in ("thought",)]
    check("Has experiments", len(real_experiments) > 0, f"{len(real_experiments)} experiments")

    # --- THINK entries ---
    think_count = count_pattern(log, r"## THINK —")
    check("THINK entries exist", think_count > 0, f"{think_count} entries")

    # Check THINK has required subsections
    think_blocks = re.findall(r"## THINK —.*?(?=\n## |\Z)", log, re.DOTALL)
    thinks_with_subsections = 0
    for block in think_blocks:
        has_convergence = bool(re.search(r"convergence signal", block, re.I))
        has_assumptions = bool(re.search(r"untested assumption", block, re.I))
        has_invalidation = bool(re.search(r"invalidation risk", block, re.I))
        has_hypothesis = bool(re.search(r"next hypothesis", block, re.I))
        if has_convergence and has_assumptions and has_invalidation and has_hypothesis:
            thinks_with_subsections += 1
    check("THINK has 4 subsections", thinks_with_subsections > 0,
          f"{thinks_with_subsections}/{think_count} complete")

    # --- Guardrails ---
    max_streak = longest_discard_streak(rows)
    guardrail_3 = count_pattern(log, r"## 3-Discard Guardrail")
    guardrail_5 = count_pattern(log, r"## 5-Discard Fork")

    if max_streak >= 3:
        check("3-discard guardrail written", guardrail_3 > 0,
              f"max streak={max_streak}, entries={guardrail_3}")
    else:
        check("3-discard guardrail (not triggered)", True,
              f"max streak={max_streak}, no guardrail needed")

    if max_streak >= 5:
        check("5-discard fork written", guardrail_5 > 0,
              f"max streak={max_streak}, entries={guardrail_5}")
    else:
        check("5-discard fork (not triggered)", True,
              f"max streak={max_streak}, no fork needed")

    # --- Re-validation ---
    revalidation_count = count_pattern(log, r"## Re-Validation")
    exp_count = len([r for r in rows if r["status"] != "thought"])
    expected_revalidations = exp_count // 10
    check("Re-validation at every 10th", revalidation_count >= expected_revalidations,
          f"{revalidation_count} found, {expected_revalidations} expected")

    # --- Branching ---
    git_branches = run("git branch", repo_path).split("\n")
    research_branches = [b.strip().lstrip("* ") for b in git_branches if "research/" in b]
    check("Research branches exist", len(research_branches) > 0,
          f"{len(research_branches)} branches: {', '.join(research_branches)}")

    # Fork after 5-discard?
    if max_streak >= 5:
        check("Fork branch created after 5-discard", len(research_branches) >= 2,
              f"{len(research_branches)} branches")

    # --- Commit discipline ---
    git_log = run("git log --oneline --all", repo_path)
    experiment_commits = len(re.findall(r"experiment #\d+", git_log))
    keeps = len([r for r in rows if r["status"] in ("keep", "keep*") and r["experiment"] != "0"])
    check("Experiment commits exist", experiment_commits > 0,
          f"{experiment_commits} experiment commits, {keeps} keeps in history")

    # --- OUTCOME: Did the agent escape local optimum? ---
    best_metric = max(r["metric"] for r in rows) if rows else 0
    check("Found local optimum (>70)", best_metric > 70, f"best={best_metric}")
    check("Escaped local optimum (>80)", best_metric > 80, f"best={best_metric}")
    check("Found global optimum (>90)", best_metric > 90, f"best={best_metric}")
    check("Near-perfect global (>94)", best_metric > 94, f"best={best_metric}")

    # --- Report ---
    print(f"\n{'='*60}")
    print(f"DISCIPLINE VALIDATION: {repo_path}")
    print(f"{'='*60}")
    passed = sum(1 for r in results if r["passed"])
    failed = sum(1 for r in results if not r["passed"])
    print(f"\nTotal: {passed} PASS / {failed} FAIL\n")

    for r in results:
        status = "PASS" if r["passed"] else "FAIL"
        detail = f" — {r['detail']}" if r['detail'] else ""
        print(f"  [{status}] {r['name']}{detail}")

    print(f"\n{'='*60}")
    print(f"Best metric: {best_metric}")
    escaped = best_metric > 80
    print(f"Escaped local optimum: {'YES' if escaped else 'NO'}")
    print(f"{'='*60}\n")

    return failed == 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 verify.py /path/to/test/repo")
        sys.exit(1)
    success = verify(sys.argv[1])
    sys.exit(0 if success else 1)
