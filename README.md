# Level3 Cloud Architecture Thought Experiment: Desk-Design Evaluation

[日本語](README.ja.md) | English

## Purpose

This repository records an experiment on whether an AI agent can turn ambiguous business requirements into a defensible AWS/Azure/GCP design, judged against a fixed rubric. The scored October trials are desk designs: no environment was deployed and no live infrastructure performance, recovery, or bills were measured in them. In September, C-1 separately made a read-only look at an existing authenticated console; it changed nothing and stopped incomplete. Reading this repository needs no cloud access. Local document or implementation work is not infrastructure acceptance, and a design-only assessment cannot prove live infrastructure, SLO attainment, deletion, bills, or legal compliance.

## Two research phases

- **September, initial attempt (self-assessed).** A-1 (8 Sep), A-2/A-3 (9 Sep) and B (10 Sep) produced self-scores of 61 → 65 (A) and 66 (B). The reports themselves record the shortcomings: omitted monitoring costs, and unproven deletion deadlines, recovery, and ownership/staffing constraints. C-1 (13 Sep) stopped incomplete. These are a different method from October, so the scores are not comparable ([A](experiments/A/final-report.md), [B](experiments/B/final-report.md), [C-1](evaluation/C-1-console-readonly-check-run.md)).
- **October, independent follow-up (1–2 Oct).** Independent review replaced self-scoring. Requirements/evidence mapping, an unknown-cost (U) ledger, and the IAM, deletion, and recovery specifics became more concrete, but nothing was proven live. The highest independent score is 78 (D4) and the latest is D5 at 77 (requested High). The separate fresh trial (73) and the unscored changed requirements are not part of this series. Actual models and applied reasoning settings are UNKNOWN.

## Result

| Item | Value |
|---|---|
| Authoritative latest result | D5, 2 Oct 2026: independent **77/100**, numerical FAIL, adoption HOLD ([D5 report](docs/reports/2026-10-02-d5/FINAL-REPORT.en.md)) |
| Highest independent score | D4, 78/100 (run 1 Oct). The series 53 → 72 → 69 → 78 → 77 is not monotonic ([discussion](docs/reports/2026-10-02-d5/DISCUSSION.en.md)) |
| Why no pass | Acceptance needs total >= 80, all 11 categories >= 3, six mandatory categories >= 4, no unresolved P0, and all six hardgates PASS. D5 had Cost 3, below the mandatory minimum of 4, and G3/G4 HOLD ([gates](docs/reports/2026-10-02-d5/evidence/independent-review-D5/gates.csv)) |
| September records | Self-assessed: A 61 → 65, B 66, C-1 incomplete. Not comparable with October |

Complexity 3 meets the general floor of 3 but lowers the weighted total; it is not by itself a mandatory-4 failure.

Here, a pass would mean acceptance of a design deliverable against fixed conditions. It would not mean production readiness.

## Reading path

1. This README: purpose, result, which record to trust.
2. [Methods and results](docs/research/METHODS-RESULTS.en.md): the September failures, the October follow-up, remaining limitations, and the proposed controlled next research.
3. [Evidence appendix](docs/research/EVIDENCE.en.md): a curated index of sources, with scope gaps stated.

## Which record to trust

- **Authoritative latest:** D5 (2 Oct 2026, independent review).
- **Historical appendices:** the September A/B/C-1 workflow stages and the D1–D4 trials. The letters A/B/C are historical workflow stages, not the two research phases.
- **Separately unscored:** the requirements changed on 2 Oct (90-day backups, 14-day PITR, automated regional recovery, and others) in the [final report](docs/reports/2026-10-02-final/FINAL-REPORT.en.md). They were not D5 input, and their existence is not evidence of a pass.
- **Reported context only:** a separate fresh-trial score of 73, known only from the publication handoff. It is excluded from the D1–D5 series.

## Caveats

Model names are requested settings, not verified runtimes. D5 requested a Sol High designer and a Sol Medium reviewer, and the actual models and settings are UNKNOWN. The results therefore show neither a causal model comparison nor the limits of current frontier models.

Historical experiment reports, evaluation records, and frozen publication packages are preserved. The older B and C-1 navigation guides now point here. Older wording about next actions in archival reports is historical, not current authorization.
