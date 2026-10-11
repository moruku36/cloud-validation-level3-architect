# Claude Opus 5.5 High/Medium Additional Pilot Plan

[日本語](OPUS55-PILOT-PLAN.ja.md) | English · [Methods and results (research plan)](METHODS-RESULTS.en.md#5-conclusion-and-proposed-next-research) · [README](../../README.md)

## 1. Status

| Item | Value |
|---|---|
| Status | **Planned, not executed** |
| Execution date | Undecided |
| Detailed budget, time/token limits, open owner conditions | Undecided |
| Role | A planning record. **It is not permission to start.** No experiment is started now |

This document makes proposal (a), "Model and effort", in [Methods and results, section 5](METHODS-RESULTS.en.md#5-conclusion-and-proposed-next-research) concrete as a **new pilot**. It is not a comparison with the same inherited input and conditions as the D1–D5 series. The single runs below are a candidate procedure, not a confirmed or authorized trial count, budget, or execution.

## 2. Background

- The latest D5 score is 77 and the highest independent score is D4 at 78. Neither passed ([D5 report](../reports/2026-10-02-d5/FINAL-REPORT.en.md), [D1–D4](../reports/2026-10-02-final/FINAL-REPORT.en.md)).
- Arithmetic reference: if D5's Cost went 3 → 4 (+2) and Complexity 3 → 4 (+1) with all other scores held constant, the total would be 80. This calculation assumes the other scores stay constant and is not a prediction of attainment.
- Pass conditions: total >= 80, all 11 categories >= 3, the six mandatory categories (Requirements, Architecture, Security/IAM, Availability, Cost, Backup/DR) >= 4, no P0, and all six hardgates PASS. Complexity 3 meets the general floor of 3.
- In D5, G3/G4 were on HOLD because of human-side responsibility, retention, approved effort, recovery authority, and similar items. A model cannot supply these.
- Actual runtime models and reasoning settings are UNKNOWN in all past trials. The inherited designs and evaluators also differ between trials. No causal claim about model superiority can be drawn from historical scores.
- The additional owner answers from the separate 2 Oct final were intentionally not included in D5.

## 3. Proposal table

| Proposal | Hypothesis | Variable | Held constant | Measurement |
|---|---|---|---|---|
| New pilot: Opus 5.5 High, once | A design produced under this condition reaches a level that independent assessment judges worth continuing to study | Requested model "Opus 5.5" and effort "High" (requested labels) | The pre-run manifest (section 5): input version, rubric, reference materials, tool permissions, budget, stop conditions, evaluation procedure | Category scores, gate results, findings, P0, unknown costs (U) |
| Conditional candidate: Opus 5.5 Medium, once | Changing only effort under the same conditions gives a different result | Effort "Medium" (requested label), in a separate fresh session | The same manifest as High | Same as High |

- "Opus 5.5", "High", and "Medium" are **planned requested labels**. The official docs describe Opus 5.5 and effort settings, but availability under this subscription and execution environment, actual runtime, and applied effort remain unconfirmed.
- At run time, check the [official docs](https://code.claude.com/docs/en/model-config#choose-an-effort-level) and the models available in the CLI. If it is unavailable, **hold**; do not substitute another model on one's own. High and Medium are candidate effort settings.
- **Medium is not started automatically.** It is a candidate only if, after the High run, the input conditions held and independent assessment of the frozen artifact makes continuing worthwhile. It would then run under the same conditions in a separate fresh session.
- The concrete thresholds for "promising" and "worth continuing" are fixed before the run. **They are undecided now.**
- Design scores and operational-approval HOLD/P0 are reported separately.

## 4. Limits of comparison

- This is a new pilot. It is not inserted into the D1–D5 inherited series, it is not a same-inheritance comparison, and it is not called a reproduction of D5 conditions.
- If the additional owner answers from the separate 2 Oct final are used, the run is a **separate series** that states the input version and what changed. The choice of input version is fixed before the run. **It is not decided yet.**
- A single result is not read as a stable pass rate or model superiority. One run each of High and Medium cannot establish a causal effect of effort or its reproducibility.
- Use of the contract allowance does not prove the monetary cost is zero.

## 5. Pilot procedure

1. **Fix the manifest (before the run).** Record the input version (formal requirements/answers), rubric, reference materials, tool permissions, time/token budget, stop conditions, evaluator and evaluation procedure, and the "promising" thresholds, each with an identifier such as a hash or commit. Unanswered items stay unanswered.
2. **Check the environment.** Check the official docs and the models available in the CLI. Check the authentication method and the contract allowance. Hold if unavailable.
3. **Design session (fresh).** Do not show the designer any past generated designs, generated answers, scores, or fix hints. Include the formal requirements and owner answers fixed in the manifest. This plan itself contains past scores and hints, so do not mix it into the designer's input.
4. **Freeze.** Freeze the artifact after generation.
5. **Independent scoring.** A separate evaluator, blind to model name, effort, desired score, and past scores, scores the frozen artifact once with stated grounds. After freezing, add no artifact changes, supplementary evidence aimed at raising scores, or preliminary scoring. Keep the execution records in section 6 separate from the artifact and withhold identifying information from the evaluator.
6. **Report.** Record requested and observed values separately (section 6). Report design scores and HOLD/P0 separately.
7. **Medium decision.** Only if the section 3 condition is met, repeat steps 3–6 under the same conditions in a separate fresh session.
8. Any revision or rescoring after scoring is a **separate trial**, not mixed into the same one.

## 6. Records

| Kind | What is recorded |
|---|---|
| Requested | Model name, effort, input version, budget |
| Observed | Runtime, applied effort, usage (tokens etc.), wall time, termination reason, tool logs, as far as observable |

Anything not observable is UNKNOWN. Self-reports are not treated as confirmation.

## 7. Prohibitions and usage conditions

- The plan is to use the existing Claude contract allowance. Check the authentication method and allowance before the run. Do not switch to an API key, pay-as-you-go billing, or another provider without approval.
- No code or Terraform execution, cloud operations, or API billing.
- Do not set unknown prices to zero, fabricate evidence, fill in owner approvals on one's own, or relax criteria.

## 8. Open items

| Item | State |
|---|---|
| Execution date | Undecided |
| Detailed budget, time/token limits | Undecided |
| Owner conditions | Undecided |
| Input version (formal requirements/answers; whether to use the additional answers from the separate 2 Oct final) | Undecided |
| Concrete "promising" thresholds | Undecided |
| Availability of Opus 5.5 under this subscription and execution environment; applicability of High/Medium | Unconfirmed |
| Authentication method and contract allowance status | Unconfirmed |
| Evaluator configuration | Undecided |

## 9. Sources

- [D5 final report](../reports/2026-10-02-d5/FINAL-REPORT.ja.md) (Japanese; English: [FINAL-REPORT.en.md](../reports/2026-10-02-d5/FINAL-REPORT.en.md))
- [D1–D4 final report](../reports/2026-10-02-final/FINAL-REPORT.ja.md) (Japanese; English: [FINAL-REPORT.en.md](../reports/2026-10-02-final/FINAL-REPORT.en.md))
- [Methods and results](METHODS-RESULTS.en.md)
- Official docs: [Choose an effort level](https://code.claude.com/docs/en/model-config#choose-an-effort-level)
