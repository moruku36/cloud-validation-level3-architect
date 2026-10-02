# Methods and Results

[日本語](METHODS-RESULTS.ja.md) | English · [README](../../README.md) · [Evidence appendix](EVIDENCE.en.md)

## 1. Purpose, result, how to read

The experiment asks whether an AI agent can turn ambiguous business requirements into a reasonable, evidence-backed cloud design for AWS, Azure, and GCP. Every assessment is a desk assessment of documents. The latest authoritative result is **D5 (2 Oct 2026): independent 77/100, numerical FAIL, adoption HOLD** ([D5 report](../reports/2026-10-02-d5/FINAL-REPORT.en.md)). No design trial met the full acceptance conditions.

The work is described as two **research phases**: September (initial failures) and October (follow-up addressing the deficiencies). The older letters A/B/C name historical workflow stages inside September and are not the phases.

| Assessment kind | Where | Meaning |
|---|---|---|
| Self-assessment (the same agent that did the work; human fields blank) | September A, B | A documented self-assessment; it does not establish independent acceptance |
| Independent desk assessment (reviewer separate from the designer; anonymous frozen packets documented for D4/D5) | October D1–D5 | The scores used for acceptance, still desk-only |
| Human scoring and adoption approval | none | Blank or not obtained |

## 2. Phase 1: September initial failures

The A and B stages specified GPT-6 Astra Light as the model. The runtime identity and settings were not obtained, so the specified name is not treated as a measured value ([A](../../experiments/A/final-report.md), [B](../../experiments/B/final-report.md)).

| Date | Stage | Result | Source |
|---|---|---|---|
| 8 Sep | A-1 requirements | Prerequisite for A | [A](../../experiments/A/final-report.md) |
| 9 Sep | A-2 design, A-3 review | Self-score **61 → 65**, below the acceptance bar | [A scores](../../experiments/A/A-3/scores.md) |
| 10 Sep | B comparison and selection | Self-score **66** (initial, B-2 complete, B-3 limited fix all 66), design FAIL, selection on hold | [B](../../experiments/B/final-report.md) |
| 13 Sep | C-1 console read-only check | INCOMPLETE | [C-1](../../evaluation/C-1-console-readonly-check-run.md) |

**A, mechanisms.** The review found a monitoring-cost omission: an omitted 166.44 USD/month probe subtotal, calculated from official unit prices, brought monitoring to 196.44 USD/month, and the budget was still missed. Five observations spaced one minute apart can span only four minutes, so the stability check was redefined as 300 seconds with six observations. Cost rose 2 → 3 and Observability 2 → 4, but the report says the Cost gain reflects a clearer explanation of why the budget fails, not a budget fit. Observability 4 is a design specification, not a measurement. Unmet requirements: total 65 < 80, and five of the six required categories (all but Requirements) were below 4. Deletion deadlines, end-to-end recovery, and per-AZ capacity remained unproven. [September findings](../../experiments/A/final-report.md#7-発見した問題と残課題).

**B, mechanisms.** Three providers were compared under identical conditions (10% tax, 150 JPY/USD, no free tiers). Basic monthly costs moved as follows. AWS went 76,034 → 83,248 JPY plus unknowns (U), against a 100,000 JPY budget, and the remaining 16,751.63 JPY could be consumed by U and required capacity increases. GCP went 135,580 → 101,933 JPY plus U, still over budget. Azure went 216,493 → 218,588 JPY plus U. The relative points (AWS 64, GCP 62, Azure 59) are not a formal pass. AWS stayed only a reference preference. Architecture, Security, Availability, Cost, and DR stayed at 3, below the required 4. Eleven findings (F01–F11), human decisions on mail storage, PITR, and ownership, and the empirical tests T01–T16 remained open and unexecuted. [September B findings and costs](../../experiments/B/final-report.md).

**C-1.** The console check ran 4 h 23 m 02 s against a 20-minute window and stopped. The recorded elapsed time includes interruptions. It made no changes, and Identity Center reuse or enablement stayed undetermined. Its next-action wording is historical, not current authorization.

## 3. Phase 2: October follow-up

October replaced self-scoring with independent review and iterated the design. The archived history places the original D1–D4 series on 1 Oct; the bilingual summary was published on 2 Oct ([history attribution](../reports/2026-10-02-final/EVIDENCE.en.md#basis-for-the-assessment-history-and-discussion)). Only the D4 clocks (1 Oct) are public; the individual D1–D3 clocks are **unknown** ([D4 clocks](../reports/2026-10-02-d5/evidence/inherited/independent-review-D4/metadata-clocks.json)).

| Trial | Requested designer setting | Independent score | Gates / note |
|---|---|---:|---|
| D1 | GPT-6 Luna Low | 53 | 2 PASS / 3 FAIL / 1 UNKNOWN |
| D2 | GPT-6 Luna Medium | 72 | 4 PASS / 2 UNKNOWN |
| D3 | GPT-6 Luna High | 69 | 4 PASS / 2 HOLD |
| D4 | GPT-6.1 Sol Medium | 78 | 4 PASS / 2 HOLD; Cost 3 |
| D5 (2 Oct) | GPT-6.1 Sol High | **77** | G3/G4 HOLD; Cost 3, Complexity 3 |

Sources: [D1–D4](../reports/2026-10-02-final/FINAL-REPORT.en.md), [D5](../reports/2026-10-02-d5/FINAL-REPORT.en.md). Actual runtime models and reasoning settings are UNKNOWN in every trial, including the reviewers (requested Sol Medium). The September self-scores (65, 66) must not be mixed with these independent scores.

**D5, mechanisms.** D5 revised the D4 design and added admission, epoch, and fence controls, which a fresh independent reviewer scored once after anonymous freezing. D5 ran on 2 Oct 2026 UTC and its core wall time was 60 m 48 s. The score fell by one because Complexity went 4 → 3, and Cost stayed 3. The findings behind this ([findings](../reports/2026-10-02-d5/evidence/independent-review-D5/step4-findings.md)):

- D01: the SQL-backed AdmissionCoordinator sits on every principal request path without sufficient support for operation counts, contention, latency, or recovery ordering.
- D02: the 40–80 hour initial effort and 16–32 hour rehearsal effort for custom controls lack sufficient task-level grounds.
- D03: budget feasibility, headroom for mandatory residual costs, and cheaper control alternatives are not shown. Known GCP compute alone is 387.4464 USD (P2/dev176) and 630.72 USD (P4/dev730), about 60,828 and 99,021 JPY at the frozen FX of 156.9969. This excludes other mandatory meters and tax and is not a bill or a guaranteed lower bound.
- D04: the journal used to salvage valid writes after logical corruption lacks defined payload, independent protection, completeness, and replay order.

The hardgates were G1, G2, G5, and G6 PASS, with G3 (deletion events, linkage retention, copy and recipient responsibility) and G4 (named owners, approved hours, absence coverage, unattended recovery authority) on HOLD ([gates](../reports/2026-10-02-d5/evidence/independent-review-D5/gates.csv)). The remaining P0 items are owner, source-access, and unauthorized-live prerequisites, not desk-design defects.

**Records kept apart.** A separate fresh trial was reported as 2 Oct, requested Sol High, with a score of 73. The public discussion substantiates 73 and the separate route via the publication handoff; it does not independently establish the reported date/High setting. Its original packet, categories, gates, actual settings, and exact clocks are not included. Its date and configuration are reported context, not verified chronology or model fact, and it is not inserted into the inherited series ([discussion](../reports/2026-10-02-d5/DISCUSSION.en.md)). Requirements changed on 2 Oct (90-day backups, 14-day PITR, automated regional recovery, extended domestic storage, deletion notices) are separately unscored and were not D5 input ([final report](../reports/2026-10-02-final/FINAL-REPORT.en.md)). The D5 merge commit is dated 3 Oct 01:17:44 JST (2 Oct 16:17:44 UTC); the [PR26 merge event](https://github.com/moruku36/cloud-validation-level3-architect/pull/26) is recorded one second later. Publication time therefore differs from trial and report time ([publication commit](https://github.com/moruku36/cloud-validation-level3-architect/commit/0d67081cb994b69d10551df4346ab3757851ff2f)).

### What addressed the earlier deficiencies

These are documented design responses, not measured recovery of a running service. The September findings and [October change ledger](../reports/2026-10-02-d5/evidence/d4-to-d5-change-table.csv) support this cross-phase reading; they do not establish that every September issue was closed.

| September deficiency | October response | What remained unproven |
|---|---|---|
| Coarse costs and omitted monitoring | Matched-rate attempts, quantities, quote-completeness ledger, explicit U and control meters | Complete totals, tax/FX, budget headroom; Cost 3 |
| Recovery clocks and dependencies underspecified | Detection/dispatch budget, external stability checks, provider adapters, 35 scenario reviews | Actual end-to-end timings, valid-write salvage and coordinator ordering |
| Deletion copies, ledger retention, restore re-deletion | Ten copy classes, watermark/key/ledger predicates, restore-publication checks | Approved linkage/retention/custody and recipient boundary; G3 HOLD |
| IAM and unattended staffing boundaries | Broker manifests, negative assertions, role-specific unique work and stop conditions | Effective IAM, named primary/deputy and approved hours/authority; G4 HOLD |

## 4. Remaining limitations

- New evidence, a fresh reviewer, and added controls confound any 78 → 77 or 73 → 77 comparison.
- Owner answers, exact regional SKU/quota/price access, and live demonstrations are unresolved.
- All-inclusive infrastructure costs lack complete quantities, rates, invoice FX, tax, and headroom. Labor is accounted for separately, with effort and staffing unapproved.
- Desk design cannot prove SLOs, deletion, bills, or legal compliance.
- Frontier limits are not established: these are four requested configurations plus one, not a model ranking.

## 5. Conclusion and controlled next research

The design improved in specificity (53 → 78), but it did not pass, and the latest score is 77. A model upgrade alone cannot promise a pass, because missing prices, owner approvals, and empirical records are not supplied by capability. The next decision should address, in order:

1. a simpler architecture before any custom coordinator, with its performance and effort justified;
2. complete cost quantities, rates, FX, tax, headroom, and labor;
3. owner decisions on deletion, custody, staffing, and recovery authority;
4. a valid-write salvage contract after logical corruption.

A controlled comparison would fix requirements, rubric, evidence access, and the evaluator. It would attest the model and effort, blind the reviewers, repeat each configuration several times, and separate feedback-assisted from unassisted runs. It must not change thresholds, treat unknown prices as zero, or cap categories merely because measurements are absent. This document does not authorize another trial or any cloud execution ([source](../reports/2026-10-02-final/FINAL-REPORT.en.md)).
