# Level 3 Cloud Architecture Validation

[English](README.md) | [日本語](README.ja.md)

A phased cloud-architecture evaluation repository. Phase C-1 is safely halted: Terraform and Python guards are implemented, but no live AWS resources have been created for that phase.

## Current status

Phase C-1 is safely halted. The recorded local unit suite passed 36 tests, but the time-bounded read-only console precheck ended `INCOMPLETE`. No live resources were created for this phase. Further access or live operations depend on the project's existing human decision boundaries.

[Read-only precheck record](evaluation/C-1-console-readonly-check-run.md) · [Pending decisions, Issue 9](https://github.com/moruku36/cloud-validation-level3-astra-light/issues/9).

## Local verification

```bash
python -m unittest discover -s infra/c1/tests -v
terraform fmt -check -recursive infra/c1
```

The repository tracks design reviews, cost comparisons, findings, handoff responsibilities, and local Terraform/Python guard implementation. The Japanese guide retains the detailed phase-by-phase evaluation.


## Contents

- [docs/](docs)
- [evaluation/](evaluation)
- [experiments/](experiments)
- [infra/](infra)

## Detailed documentation

The [Japanese guide](README.ja.md) retains the complete original setup instructions, configuration, examples, project status, and limitations. Supporting documents keep their existing language.

## Final thought-experiment report (2026-10-02)

[Report overview](docs/reports/2026-10-02-final/README.md) · [English report](docs/reports/2026-10-02-final/FINAL-REPORT.en.md) · [日本語レポート](docs/reports/2026-10-02-final/FINAL-REPORT.ja.md)

The final report records the updated design assumptions, the AWS/Azure/GCP comparison, the partial cost model, and remaining evidence gaps. It also discusses the four recorded evaluations and conditions for a future model to reach the passing threshold. The desk study is complete; provider selection, production acceptance, live cloud testing, and budget compliance remain unproven. The historical D4 score of 78/100 and HOLD remains a record of the earlier requirements.

## D5 inherited improvement report (2026-10-02)

[D5 overview and evidence](docs/reports/2026-10-02-d5/README.md) · [English report](docs/reports/2026-10-02-d5/FINAL-REPORT.en.md) · [日本語報告](docs/reports/2026-10-02-d5/FINAL-REPORT.ja.md) · [English discussion](docs/reports/2026-10-02-d5/DISCUSSION.en.md) · [日本語考察](docs/reports/2026-10-02-d5/DISCUSSION.ja.md)

D5 records one improvement of the historical D4 design and one fresh independent assessment: **77/100, numerical FAIL / adoption HOLD**, with Cost/Complexity3 and G3/G4 HOLD. Requested designer/reviewer settings were GPT-6.1 Sol High/Medium; actual model and reasoning settings remain UNKNOWN. Original requirements were fixed, while new public evidence and a fresh reviewer prevent a controlled model comparison. Historical D4's 78, the separately reported clean-sheet 73, and the unscored report on additional conditions remain distinct. This publication changes no earlier score and authorizes no live cloud operation.
