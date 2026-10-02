# Evidence Appendix

[日本語](EVIDENCE.ja.md) | English · [README](../../README.md) · [Methods and results](METHODS-RESULTS.en.md)

This is a curated index, not an archive listing. It directs readers to key records in the pinned repository state (commit `0d67081cb994b69d10551df4346ab3757851ff2f`). The frozen reports and evidence it points to are unchanged.

## Which record to use

| Tier | Meaning | Primary sources |
|---|---|---|
| Authoritative latest | D5 independent result: 77/100, FAIL, HOLD | [D5 report](../reports/2026-10-02-d5/FINAL-REPORT.en.md), [gates](../reports/2026-10-02-d5/evidence/independent-review-D5/gates.csv) |
| Historical appendix | September A/B/C-1 (self-assessed) and D1–D4 | [A](../../experiments/A/final-report.md), [B](../../experiments/B/final-report.md), [C-1](../../evaluation/C-1-console-readonly-check-run.md), [final report](../reports/2026-10-02-final/FINAL-REPORT.en.md) |
| Separately unscored | Requirements changed on 2 Oct; not D5 input | [final report, requirements section](../reports/2026-10-02-final/FINAL-REPORT.en.md) |
| Reported context only | The separate fresh 73 | [discussion](../reports/2026-10-02-d5/DISCUSSION.en.md) |

## Key claims and where they are supported

| Claim | Source | Note |
|---|---|---|
| A: self-score 61 → 65, 8–9 Sep | [A report](../../experiments/A/final-report.md), [scores](../../experiments/A/A-3/scores.md) | Self-assessed; human fields blank |
| B: self-score 66, design FAIL, 10 Sep | [B report](../../experiments/B/final-report.md) | AWS preferred only as a reference; relative points are not a pass |
| C-1 INCOMPLETE, 13 Sep, 4 h 23 m 02 s | [C-1 record](../../evaluation/C-1-console-readonly-check-run.md) | Read-only; next-step wording is historical |
| D1–D4 scores 53/72/69/78 and requested settings | [final report, section 9](../reports/2026-10-02-final/FINAL-REPORT.en.md) | Actual runtime unverified |
| D4 ran 1 Oct (Step 4 started 09:36:51Z) | [D4 clocks](../reports/2026-10-02-d5/evidence/inherited/independent-review-D4/metadata-clocks.json) | D1–D3 clocks not public |
| D5: 77/100, categories, FAIL/HOLD | [D5 report](../reports/2026-10-02-d5/FINAL-REPORT.en.md) | Per-category grounds in [scoring.csv](../reports/2026-10-02-d5/evidence/independent-review-D5/scoring.csv) |
| D5 hardgates: G1/G2/G5/G6 PASS, G3/G4 HOLD | [gates.csv](../reports/2026-10-02-d5/evidence/independent-review-D5/gates.csv) | Desk definitions only |
| D5 findings D01–D06 | [step4-findings.md](../reports/2026-10-02-d5/evidence/independent-review-D5/step4-findings.md), [review.md](../reports/2026-10-02-d5/evidence/independent-review-D5/review.md) | Frozen design was not repaired |
| D5 cost conditions and known GCP compute | [cost conditions](../reports/2026-10-02-d5/evidence/blind-review-design-D5/cost-configuration-D5.md), [missing rates](../reports/2026-10-02-d5/evidence/blind-review-design-D5/quote-completeness.csv) | Not a bill or a lower bound |
| D4 → D5 design changes and confounds | [change table](../reports/2026-10-02-d5/evidence/d4-to-d5-change-table.csv), [pre-score disclosure](../reports/2026-10-02-d5/evidence/independent-review-D5/workflow-disclosure.md) | Blocks causal model claims |
| Series 53 → 72 → 69 → 78 → 77 and the 73 exclusion | [discussion](../reports/2026-10-02-d5/DISCUSSION.en.md) | 73 is not in the inherited series |
| Future comparison method | [final report, section 9](../reports/2026-10-02-final/FINAL-REPORT.en.md), [evidence note](../reports/2026-10-02-final/EVIDENCE.en.md) | A proposal, not an authorization |

## Scope gaps

- This index is selective and does not reproduce the complete archive. The full 180-file D5 archive is privately preserved and not published.
- Individual D1–D3 clocks are not public and are treated as unknown.
- The separate 73 is known only from the publication handoff. Its original packet, categories, gates, runtime, and clocks are not public, so its date and configuration are reported context, not verified fact.
- Actual runtime models and reasoning settings are UNKNOWN for every designer and reviewer, so the requested names are not evidence of capability.
- The September navigation was later edited on 17 Sep ([commit](https://github.com/moruku36/cloud-validation-level3-architect/commit/44876806639ecaffb7e139cd9cd6985be58c79ef)). The D5 publication merge commit is dated 3 Oct 01:17:44 JST = 2 Oct 16:17:44 UTC ([PR26 merge commit](https://github.com/moruku36/cloud-validation-level3-architect/commit/0d67081cb994b69d10551df4346ab3757851ff2f)); neither is a new experimental run.
- No live infrastructure acceptance, measured SLO, completed deletion, actual bill, or legal-compliance evidence is established by these desk results. Older next-action wording in archival reports is historical, not authorization.
- For code-oriented reading after the research narrative, use the [historical C-1 local verification guide](../../infra/c1/README.md). Its offline tests verify guards, not cloud performance or IAM enforcement.
