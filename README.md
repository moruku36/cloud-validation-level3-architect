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
