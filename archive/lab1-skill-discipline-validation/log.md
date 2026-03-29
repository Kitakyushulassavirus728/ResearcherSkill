# Experiment Log

## Experiment 0 — Baseline
**Branch:** research/improve-researcher-skill
**Type:** real (evaluation only)
**Parent:** none
**Hypothesis:** Establish baseline quality of researcher.md
**Changes:** None — evaluated as-is
**Result:** 6.25/10 composite | 345 lines, 2644 words
**Duration:** 0s
**Status:** keep
**Insight:** Main weaknesses are conciseness (5/10) and robustness (5/10). The skill is too long (~5500 tokens), putting it well past the ~3000 token degradation threshold from the research. Critical rules are buried in the middle. No structural techniques (XML tags, primacy/recency positioning) are used. Discovery phase has confusing questions (Q6 time budget unclear, Q8 tracking is impossible to do tracked). Negative framing used in several places.

## Experiment 1 — Comprehensive rewrite
**Branch:** research/improve-researcher-skill
**Type:** real
**Parent:** experiment #0
**Hypothesis:** Applying multiple research findings simultaneously (primacy/recency, conciseness, XML tags, positive framing, question fixes) will significantly improve all rubric scores
**Changes:** Rewrote entire researcher.md: added <critical> tags at top/bottom, removed Q8, clarified Q6, positive framing, compacted tables, separated reference material, flattened verbose sections
**Result:** 7.60/10 vs 6.25/10 baseline (+21.6%) | 245 lines, 1677 words (37% reduction)
**Duration:** 0
**Status:** keep
**Insight:** Big wins from conciseness (5→7) and structure (6→8). Primacy/recency with <critical> tags is effective. Still room for improvement: conciseness could go further (7/10), robustness needs structured self-audit mechanism (7/10). The multi-variable approach worked because changes were synergistic — can't shorten without restructuring.

## Experiment 2 — Trim config template, reorder references, add drift re-injection
**Branch:** research/improve-researcher-skill
**Type:** real
**Parent:** experiment #1
**Hypothesis:** Removing verbose templates, reordering references by usage timeline, and adding drift re-injection will improve conciseness and robustness
**Changes:** Replaced config.md code template with prose description, compacted results.tsv column desc, reordered references (qualitative rubric first), added "re-read <critical> block" to THINK checklist
**Result:** 8.00/10 vs 7.60 (+5.3%) | 227 lines, 1622 words
**Duration:** 0
**Status:** keep
**Insight:** Incremental but solid. Config template removal saved 18 lines. Re-injection of <critical> in THINK phase is a low-cost, high-value change for long sessions. Reference reordering is minor but correct — information should appear near where it's first needed. Remaining vectors: further conciseness (can the log entry format be trimmed?), robustness (structured output?), clarity (any ambiguities left?).

## Experiment 3 — Resume branch checkout, log format compression, filler removal
**Branch:** research/improve-researcher-skill
**Type:** real
**Parent:** experiment #2
**Hypothesis:** Targeted fixes (resume gap, filler removal, log compression, clearer re-read) will incrementally improve all dimensions
**Changes:** Resume now says checkout active branch, Phase 2 says "no announcements", removed "This is the core" filler, compressed 13-line log template to 1-line prose, clarified re-read instruction
**Result:** 8.35/10 vs 8.00 (+4.4%) | 213 lines, 1589 words
**Duration:** 0
**Status:** keep
**Insight:** Log compression was the biggest win (13→1 lines, -5.6% total). Clarity improved from resume fix and re-read wording. Concern: the 1-line log format description might be TOO compressed — agent may not produce consistent entries. Consider restoring a minimal 3-line example instead of pure prose. Robustness still the weakest dimension at 7.5.

## Experiment 4 — Restore compact log example, broaden closing critical block
**Branch:** research/improve-researcher-skill
**Type:** real
**Parent:** experiment #3
**Hypothesis:** A compact visual example for log format + broader closing critical block (3 rules instead of 1) will improve clarity and robustness
**Changes:** Replaced 1-line log prose with 3-line compact example. Expanded closing <critical> to cover execution discipline + protect .lab + autonomy.
**Result:** 8.58/10 vs 8.35 (+2.7%) | 219 lines, 1610 words (slight increase justified by clarity)
**Duration:** 0
**Status:** keep
**Insight:** The trade-off of +6 lines for +0.5 clarity and +1.0 robustness was clearly worthwhile. Broadening the closing critical block was the highest-value change — recency now covers the 3 most important behaviors. Robustness jumped from 7.5 to 8.5. Diminishing returns now — the remaining gains will be smaller.

## Experiment 5 — Positive framing for .lab protection
**Branch:** research/improve-researcher-skill
**Type:** real
**Parent:** experiment #4
**Hypothesis:** Replacing negative framing with positive alternatives improves robustness per the research on positive vs negative instructions
**Changes:** Changed "do not run git clean / do not delete" to "use targeted commands that preserve... use git reset and checkout which leave .lab intact"
**Result:** 8.65/10 vs 8.58 (+0.8%) | 219 lines, 1615 words
**Duration:** 0
**Status:** keep
**Insight:** Small gain, as expected at this point. Robustness improved from 8.5 to 9.0 — positive framing gives the agent a concrete action instead of a prohibition. Approaching diminishing returns on researcher.md itself. Time to update README.md.

## Experiment 6 — Update README to reflect researcher.md changes
**Branch:** research/improve-researcher-skill
**Type:** real
**Parent:** experiment #5
**Hypothesis:** README should reflect the current state of researcher.md
**Changes:** Positive framing for .lab protection, added LLM compliance design feature, updated Discovery description for wall-clock budget
**Result:** N/A (README is secondary scope, metric applies to researcher.md only)
**Duration:** 0
**Status:** keep
**Insight:** README was already well-written. Changes were minimal: consistency with positive framing, adding the new LLM compliance feature to the list, and updating the Discovery description.

## Experiment 7 — Add persistence rule, clarify crash section
**Branch:** research/improve-researcher-skill
**Type:** real
**Parent:** experiment #5
**Hypothesis:** Adding a "keep going" persistence rule to the closing critical block restores a lost instruction from the original, improving completeness
**Changes:** Added 4th rule "Keep going — if stuck, re-read codebase, review failed experiments..." to closing <critical>. Minor crash section wording improvements.
**Result:** 8.75/10 vs 8.65 (+1.2%) | 220 lines, 1643 words
**Duration:** 0
**Status:** keep
**Insight:** Completeness jumped from 8.5 to 9.0. The original's "Never stop" instruction was genuinely important and had been lost in the rewrite. Reframed positively as "Keep going" with concrete recovery actions. This is a meaningful behavioral instruction that prevents premature termination.

## Experiment 8 — Multi-lab support (CANCELLED)
**Branch:** research/improve-researcher-skill
**Type:** real
**Parent:** experiment #7
**Hypothesis:** Adding multi-lab support (.lab/<slug>/) would improve the skill
**Changes:** Started rewriting Phase 0, Phase 2, and file references to support multiple labs in subdirectories
**Result:** N/A — user cancelled mid-implementation
**Duration:** 0
**Status:** discard
**Insight:** User intervention: feature was not wanted. Reverted all changes. Returning to quality improvement work on existing single-lab design.

## Experiment 9 — Remove redundant transition line, compress Q5
**Branch:** research/improve-researcher-skill
**Type:** real
**Parent:** experiment #7
**Hypothesis:** Removing redundant "You decide..." line and compressing Q5 improves conciseness without losing clarity
**Changes:** Removed line 95 (redundant with "complete freedom" in intro), compressed Run command question to 1 line
**Result:** 8.88/10 vs 8.75 (+1.5%) | 218 lines, 1617 words
**Duration:** 0
**Status:** keep
**Insight:** Marginal gain. We're in deep diminishing returns territory. The file is tight at 218 lines (37% reduction from original 345). All five rubric dimensions are at 8.5-9.0. Further improvements would require fundamentally different approaches (e.g., splitting into multiple files) which would change the skill's self-contained nature.

## Experiment 10 — Thought: plateau assessment + README persistence feature
**Branch:** research/improve-researcher-skill
**Type:** thought + real (README only)
**Parent:** experiment #9
**Hypothesis:** We've reached a plateau — systematic scan for remaining improvements
**Changes:** Added persistence feature to README key features. Scanned full file for remaining improvements.
**Result:** 8.88/10 (unchanged for researcher.md). README improved.
**Duration:** 0
**Status:** keep
**Insight:** Deep diminishing returns confirmed. Score trajectory shows last 4 experiments gained +0.53 total vs +1.35 for experiment 1 alone. All dimensions at 8.5-9.0. Remaining parking lot ideas either add lines (few-shot examples), break self-containment (progressive disclosure), or are minimal gain (merge crash into execution). No clear path to 9.0+ without architectural changes.

## Experiment 11 — Thought: rephrasing opening critical block
**Branch:** research/improve-researcher-skill
**Type:** thought
**Parent:** experiment #9
**Hypothesis:** Leading with "why" (prevents lost work) instead of authority ("non-negotiable") might improve compliance per sycophancy research
**Changes:** analysis only
**Result:** No change — decided current phrasing is already optimal
**Status:** thought
**Insight:** The pragmatic framing research says authoritative framing is MOST effective, emotional/motivational is LEAST. Current phrasing "non-negotiable" is authoritative, which is the strongest framing. Changing to "prevents lost work" would shift toward motivational framing — weaker per the research. The current "authoritative + implicitly helpful" combination is the optimal balance. No change warranted.

## Experiment 12 — Merge Crash & Timeout into Execution Discipline
**Branch:** research/improve-researcher-skill
**Type:** real
**Parent:** experiment #9
**Hypothesis:** Moving crash/timeout handling into the decision items eliminates a separate section, improving structure
**Changes:** Moved crash details into CRASH decision item, added TIMEOUT as new decision item, removed Crash & Timeout subsection
**Result:** 8.88/10 (unchanged — conciseness +0.5 offset by clarity -0.5) | 210 lines, 1592 words
**Duration:** 0
**Status:** keep (equal metric, simpler structure)
**Insight:** Trade-off: CRASH line is now dense, but all crash-related info is contextually co-located with the decision that triggers it. Structurally cleaner — Execution Discipline is now fully self-contained. The skill's own rule says "equal with simpler code = keep."

## Experiment 13 — Merge flow diagram into section header
**Branch:** research/improve-researcher-skill
**Type:** real
**Parent:** experiment #12
**Hypothesis:** Replacing 5-line code block flow diagram with inline heading saves lines while preserving visual model
**Changes:** `### The Flow` + code block → `### Flow: THINK → TEST → REFLECT → repeat`
**Result:** 8.88/10 (unchanged) | 206 lines, 1589 words
**Duration:** 0
**Status:** keep (equal, simpler)
**Insight:** Plateau confirmed. Last 7 experiments have not moved metric above 8.88. Convergence signal triggered: <0.5% over 5+ keeps. The skill has been compressed 40% while improving quality 42%. Remaining gains require architectural changes outside current scope.

## Experiment 14 — Wrap reference sections in XML tags
**Branch:** research/improve-researcher-skill
**Type:** real
**Parent:** experiment #13
**Hypothesis:** Adding `<reference>` XML tags around reference material creates semantic hierarchy alongside `<critical>` tags, helping the LLM differentiate procedural vs reference content
**Changes:** Wrapped qualitative rubric, hypothesis strategies, and convergence signals in `<reference name="...">` tags. Removed "Reference:" prefix from headings (redundant with tag).
**Result:** 9.03/10 vs 8.88 (+1.7%) | 210 lines, 1589 words. BROKE THROUGH PLATEAU.
**Duration:** 0
**Status:** keep
**Insight:** Architectural change (XML tag hierarchy) was the key to breaking the content-level plateau. The insight: when text optimization plateaus, information architecture optimization can still yield gains. The `<critical>` / `<reference>` tag hierarchy creates two attention levels: mandatory (process now) and advisory (consult when needed). Claude is specifically trained to attend to XML tags. This is the highest-leverage structural change since experiment 1's primacy/recency positioning.

## Experiment 16 — Expand CRASH into sub-bullets
**Branch:** research/improve-researcher-skill
**Type:** real
**Parent:** experiment #14
**Hypothesis:** Breaking dense CRASH one-liner into sub-bullets improves clarity without meaningful conciseness cost
**Changes:** Expanded CRASH from 1 dense line to 4 structured lines (main + 3 sub-bullets: trivial, fundamental, repeated)
**Result:** 9.15/10 vs 9.03 (+1.3%) | 213 lines, 1590 words
**Duration:** 0
**Status:** keep
**Insight:** Clarity jumped from 8.5 to 9.0 — the sub-bullet structure makes crash handling scannable. The +3 lines cost is negligible compared to the clarity gain. All 5 dimensions now at 9.0+. The skill is approaching its quality ceiling for the current architectural approach.

## Experiment 17 — Move Phase 4 before reference section
**Branch:** research/improve-researcher-skill
**Type:** real
**Parent:** experiment #16
**Hypothesis:** Phase sequence should be unbroken (0→1→2→3→4) with reference material after all phases
**Changes:** Moved Phase 4 (Wrap-Up) above the <reference> block
**Result:** 9.23/10 vs 9.15 (+0.9%) | 211 lines, 1590 words
**Duration:** 0
**Status:** keep
**Insight:** Structure effectiveness hit 10/10 — the information architecture is now optimal. Phases are sequential, reference is clearly separated, closing critical provides recency. The document reads as: CRITICAL → phases (sequential) → REFERENCE (consult-when-needed) → CRITICAL. This is the ideal layout per the research.

## Experiment 18 — Thought: final review of unapplied research
**Branch:** research/improve-researcher-skill
**Type:** thought
**Parent:** experiment #17
**Hypothesis:** There might be remaining high-leverage findings from the research report not yet applied
**Changes:** analysis only
**Result:** No change — all 11 applicable findings from the research have been applied or deliberately rejected with clear reasoning
**Status:** thought
**Insight:** 3 findings were rejected with justification: few-shot examples (adds lines for uncertain gain), structured output self-audit (conflicts with autonomy philosophy), progressive disclosure (breaks self-containment). The 8 applied findings cover the highest-leverage changes. Condition check failure risk was assessed as low due to simple binary conditionals. The skill is at its quality ceiling for the current single-file, self-contained architecture.
