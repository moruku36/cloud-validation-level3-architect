# Level3 Cloud Architecture Thought Experiment: Desk-Design Evaluation

[日本語](README.ja.md) | English

## Purpose

This repository records a desk-based experiment. The question is whether an AI agent can turn ambiguous business requirements into a defensible AWS/Azure/GCP design, judged against a fixed rubric. Nothing here is a live deployment, and reading it needs no cloud access. A design-only assessment cannot prove live infrastructure, SLO attainment, deletion, bills, or legal compliance.

## Result

| Item | Value |
|---|---|
| Authoritative latest result | D5, 2 Oct 2026: independent **77/100**, numerical FAIL, adoption HOLD ([D5 report](docs/reports/2026-10-02-d5/FINAL-REPORT.en.md)) |
| Highest independent score | D4, 78/100 (run 1 Oct). The series 53 → 72 → 69 → 78 → 77 is not monotonic ([discussion](docs/reports/2026-10-02-d5/DISCUSSION.en.md)) |
| Why no pass | Acceptance needs total >= 80, all 11 categories >= 3, six required categories >= 4, no unresolved P0, and all six hardgates PASS. D5 had Cost 3, Complexity 3, and G3/G4 HOLD ([gates](docs/reports/2026-10-02-d5/evidence/independent-review-D5/gates.csv)) |
| September records | Self-assessed: A 61 → 65, B 66, C-1 incomplete. A different method, so not comparable with October ([A](experiments/A/final-report.md), [B](experiments/B/final-report.md), [C-1](evaluation/C-1-console-readonly-check-run.md)) |

Here, a pass would mean acceptance of a design deliverable against fixed conditions. It would not mean production readiness.

## Reading path

1. This README: purpose, result, which record to trust.
2. [Methods and results](docs/research/METHODS-RESULTS.en.md): the September failures, the October follow-up, remaining limitations, and the controlled next research.
3. [Evidence appendix](docs/research/EVIDENCE.en.md): a curated index of sources, with scope gaps stated.

## Which record to trust

- **Authoritative latest:** D5 (2 Oct 2026, independent review).
- **Historical appendices:** the September A/B/C-1 workflow stages and the D1–D4 trials. The letters A/B/C are historical workflow stages, not the two research phases used in the methods document.
- **Separately unscored:** the requirements changed on 2 Oct (90-day backups, 14-day PITR, automated regional recovery, and others) in the [final report](docs/reports/2026-10-02-final/FINAL-REPORT.en.md). They were not D5 input, and their existence is not evidence of a pass.
- **Reported context only:** a separate fresh-trial score of 73, known only from the publication handoff. It is excluded from the D1–D5 series.

## Caveats

Model names are requested settings, not verified runtimes. D5 requested a Sol High designer and a Sol Medium reviewer, and the actual models and settings are UNKNOWN. The results therefore show neither a causal model comparison nor the limits of current frontier models.

Historical experiment reports, evaluation records, and frozen publication packages are preserved. The older B and C-1 navigation guides now point here. Older wording about next actions in archival reports is historical, not current authorization.
