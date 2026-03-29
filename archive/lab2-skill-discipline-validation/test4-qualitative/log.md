# Experiment Log

## Experiment 0 — Baseline
Branch: research/error-message-quality / Type: real / Parent: none
Hypothesis: Establish baseline quality
Changes: None — evaluated as-is
Result: 7.10 (median) | E1: 7.10, E2: 7.10, E3: 7.20
Duration: 0s
Status: keep
Insight: Clarity (8) and tone (7) are decent. Actionability (7) and brevity (6) are the weakest. The message is too verbose — "The system encountered an unexpected error while attempting to validate your credit card information against our payment gateway" adds technical detail users don't need. Actionability suffers because "try again later" is vague.

## Experiment 1 — Concise rewrite with clear action steps
Branch: research/error-message-quality / Type: real / Parent: #0
Hypothesis: Removing technical jargon and adding specific action steps will improve actionability and brevity
Changes: Rewrote message — removed "system encountered", "payment gateway", "validate credit card information". Added "check your card details" as specific action. Separated error codes to own line.
Result: 9.00 (median) | E1: 9.00 (c=9,a=9,t=9,b=9), E2: 9.00 (c=9,a=9,t=9,b=9), E3: 8.70 (c=9,a=8,t=9,b=9)
Duration: 0s
Status: keep
Insight: Massive jump from 7.10→9.00 (+26.8%). Brevity went 6→9, actionability 7→8.7avg. The "we're happy to help" phrase landed well for tone. Error codes on separate line improved scannability.

## Experiment 2 — Numbered troubleshooting steps
Branch: research/error-message-quality / Type: real / Parent: #1
Hypothesis: Numbered action steps will improve actionability by giving users a clear sequence
Changes: Added 3-step numbered list (check card, check funds, try again). Changed "we're happy to help" to "we'll sort it out".
Result: 8.80 (median) | E1: 8.80 (c=9,a=9,t=8,b=9), E2: 8.80 (c=9,a=9,t=8,b=9), E3: 8.80 (c=9,a=9,t=8,b=9)
Duration: 0s
Status: discard
Insight: Tone regressed 9→8 across all evaluators. The numbered list makes it feel like a troubleshooting manual rather than a friendly message. "We'll sort it out" is less warm than "we're happy to help". Actionability held at 9 but the tone cost isn't worth it.

## Experiment 3 — Ultra-concise with empathetic opening
Branch: research/error-message-quality / Type: real / Parent: #1
Hypothesis: Leading with "Sorry" and shortening error code label to "Ref:" will improve tone and brevity
Changes: Added "Sorry" opener, changed "We couldn't" to "your payment didn't go through", shortened "Error code: PGW-4012 | Transaction ID:" to "Ref: PGW-4012 /"
Result: 9.00 (median) | E1: 9.00 (c=9,a=9,t=9,b=9), E2: 9.00 (c=9,a=9,t=9,b=9), E3: 9.00 (c=9,a=9,t=9,b=9)
Duration: 0s
Status: keep
Insight: Equal to exp #1 but shorter text. All evaluators agree at 9.00 (no variance). The "Sorry" opening didn't improve tone score — already at 9. The simpler ref line is slightly better. We're hitting a ceiling at 9 on all dimensions. Need a fundamentally different approach to break through.

## Experiment 4 — Acknowledge possible system issue
Branch: research/error-message-quality / Type: real / Parent: #3
Hypothesis: Mentioning "this could be a temporary issue on our end" reduces blame and improves tone
Changes: Added "— this could be a temporary issue on our end" after first sentence. Changed "we're happy to help" to "we'll resolve it right away".
Result: 8.90 (median) | E1: 9.00 (c=9,a=9,t=9,b=9), E2: 8.70 (c=9,a=9,t=8,b=9), E3: 8.90 (c=9,a=9,t=9,b=8)
Duration: 0s
Status: discard
Insight: Adding extra clause hurt brevity/tone for some evaluators. The hedge "could be" might read as uncertain rather than reassuring. 2 discards in a row now — still have headroom to explore but need different angle.

## Experiment 5 — Minimal single-line message
Branch: research/error-message-quality / Type: real / Parent: #3
Hypothesis: Maximum brevity with inline ref will push brevity to 10
Changes: Removed "Sorry", removed "we're happy to help", compressed to single line with inline parenthetical ref
Result: 8.80 (median) | E1: 8.80 (c=9,a=9,t=8,b=9), E2: 8.80 (c=9,a=9,t=8,b=9), E3: 8.80 (c=9,a=9,t=8,b=9)
Duration: 0s
Status: discard
Insight: Tone consistently 8 — removing warmth phrases ("sorry", "we're happy to help") costs more than brevity gains. These phrases are load-bearing for the tone dimension.

## 3-Discard Guardrail Check
3 consecutive discards (#2, #4, #5). Convergence signals: all variants from exp #3 score worse. The sweet spot appears to be: short conversational paragraph + warm closing + separate ref line. Adding structure (lists), adding words (system issue), or removing warmth all regress. The current best at 9.00 may be near-optimal for this rubric.

Decision: Continue — I haven't yet tried fundamentally different framing (e.g., starting with the action instead of the problem, or making the message sound less like an error).

## Experiment 6 — Action-first framing
Branch: research/error-message-quality / Type: real / Parent: #3
Hypothesis: Leading with action instead of problem will improve actionability
Changes: Removed problem statement entirely, started with "Please check your card details", changed "we're happy to help" to "we're here to help"
Result: 8.10 (median) | E1: 7.90 (c=8,a=7,t=8,b=9), E2: 8.10 (c=8,a=8,t=8,b=9), E3: 8.80 (c=9,a=9,t=8,b=9)
Duration: 0s
Status: discard
Insight: Clarity dropped 9→8 — users need to know what happened before they can act. Removing the problem statement is counterproductive. Interestingly, E3 still rated high while E1/E2 rated low — suggests the framing is polarizing. 4 discards in a row now.

## Experiment 7 — Specific action items inline
Branch: research/error-message-quality / Type: real / Parent: #3
Hypothesis: Specifying card number, expiry, balance as inline checks will improve actionability to 10
Changes: Changed "check your card details" to "double-check your card number, expiry, and available balance"
Result: 8.80 (median) | E1: 8.80 (c=9,a=9,t=8,b=9), E2: 9.00 (c=9,a=9,t=9,b=9), E3: 8.70 (c=9,a=9,t=8,b=9)
Duration: 0s
Status: discard
Insight: More detail in the action didn't help actionability (still 9) and hurt tone for 2/3 evaluators. The specifics feel prescriptive rather than helpful. 4 consecutive discards. Exp #3's form appears to be near the rubric ceiling.

## Experiment 8 — Casual conversational tone
Branch: research/error-message-quality / Type: real / Parent: #3
Hypothesis: More casual/human language will push tone to 10
Changes: "Hmm" opener, "giving it another shot", "drop us a line", "we'll get it sorted"
Result: 8.80 (median) | E1: 9.00 (c=9,a=9,t=9,b=9), E2: 8.70 (c=9,a=8,t=9,b=9), E3: 8.80 (c=9,a=9,t=8,b=9)
Duration: 0s
Status: discard
Insight: Casual tone polarized evaluators — E1 loved it, E3 found tone less professional. "Hmm" may seem too casual for a payment error. 5 consecutive discards.

## 5-Discard Fork — Strategy Diversification
**Assumptions of current best (exp #3):**
1. Conversational single-paragraph format is optimal
2. "Sorry" opening improves tone
3. Vague action ("check card details") is better than specific
4. Warm closing phrase ("we're happy to help") is essential
5. Separate reference line improves brevity perception

**Decision:** Fork from baseline (#0) and invert assumption #1 — try a structured, formal format with clear visual hierarchy instead of conversational prose. The rubric ceiling at 9.00 might be a property of the conversational form, not the content.

## Experiment 9 — Formal structured with visual hierarchy
Branch: research/structured-formal-approach / Type: real / Parent: #0
Hypothesis: Formal heading + minimal sentences + visual separation will break through 9.00 ceiling
Changes: Added "Payment unsuccessful" heading, "Your card was declined" as terse statement, "Need help?" as standalone line, removed all warmth phrases
Result: 8.30 (median) | E1: 8.30 (c=9,a=8,t=7,b=9), E2: 8.30 (c=9,a=8,t=7,b=9), E3: 8.30 (c=9,a=8,t=7,b=9)
Duration: 0s
Status: discard
Insight: Tone crashed to 7 — formal/terse reads as cold and impersonal. "Your card was declined" sounds accusatory. Confirms that conversational warmth is essential, not optional. The inverted approach definitively did not work — the 9.00 ceiling is real for this rubric with haiku evaluators.

## Re-Validation after Experiment 10
Re-ran current HEAD (exp #3) with 3 fresh evaluators.
Result: 9.00 (median) | E1: 9.00, E2: 9.00, E3: 9.00
Recorded best: 9.00 (exp #3)
**No drift detected.** Score matches exactly.
