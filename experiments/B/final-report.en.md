# LEVEL3-B Detailed Report: Comparison, Selection Design, and Evaluation Handoff

[日本語](final-report.md) | English · [Overview](../../README.md)

> **Reader note (2026-10-14).** This document is the full English counterpart of the original Stage B detailed report from 2026-09-10 ("B" refers to a historical workflow stage, not the September/October research phases). All numbers, dates, caveats, links, and evaluations are faithfully preserved. For the latest research results and overall repository guide, see the [README](../../README.md).

2026-09-10. **Completion of the Phase B documentation stage is distinct from design adoption. Self-assessment in B-3 scored 66/100, resulting in design failure, AWS retained as preferred reference design only with final selection on hold, human adoption approval not obtained, and transition to Phase C on hold.** Verification of GitHub reflection is in [Execution Record](../../evaluation/B-3-run.md). The next stage is limited remand to B-2; C-0 will not start automatically. This document is neither the Phase A detailed report nor a B-1 standalone summary, but a traceable evaluation record of the entirety of Phase B.

## Purpose, Inputs, and Scope

After fixing the ambiguous business scenario to requirements based on official answers, the three cloud providers were compared under identical conditions to assess whether a rational architecture could be selected and designed. Official inputs: [Business Answers Q01–Q08](../../docs/sources/business-answers-2026-09-08.md), [24 Requirements](../A/A-1/requirements.md), [Official Supplement](../../docs/sources/supplement-2026-09-08.md), [Rubric](../../evaluation/rubric.md). The B-3 instruction served as highest priority for scope; official business conditions, weights, and acceptance criteria were not modified.

Initial parameters: 10,000 registered users, 1 million PV/month, dynamic API 10 RPS normal / 100 RPS peak for 15 min, 500 concurrent users, 9:1 read/write. Core API p95 ≤ 500 ms, server error rate < 1%, production DB 20 GB / images 100 GB, monthly growth 2 GB / 10 GB, egress 200 GB. Initial production + minimal non-production within 100,000 JPY/month incl. tax, domestic storage and confirmation of external dependencies required, withdrawal deletion within 30 days / backup 35 days max / re-deletion after restore. 5 developers / 1 dedicated infra engineer, no nighttime response SLA. 1,000 RPS, 1 million registered users, and future budget are separated.

Specified model: GPT-6 Astra Light. Actual runtime model identification was not confirmed. Token usage, remaining tokens, model fees, and actual working time could not be acquired and are unknown. Timestamp differences between commits are not used to infer working time. Subagents were not used. B-3 was strictly limited to document review, minimal official documentation checks, limited corrections, scoring, planning, and GitHub preservation. No cloud operations, IaC/app/CI execution, PR merge, C-0/C initiation, or proxying of human scoring, adoption, or budget approvals were conducted.

## History and Comparison Methodology

| Stage | Pinned Commit / PR | Deliverables and Significance |
|---|---|---|
| B-1 Prior Criteria | 4f486d2e1d2cf82fbb0571e440d31b7841a0580e | [criteria](B-1/comparison-criteria.md). Common conditions, weights, and scoring scales recorded before scoring |
| B-1 Initial / Complete | 1812e6dc33d254be868b25b487ed962053a7f0d0 / 7c06ed0432a86b6a3c23db4eb85872d0e4591192, [PR #10](https://github.com/moruku36/cloud-validation-level3-astra-light/pull/10) | [B-1](B-1/README.md). Relative scores AWS 64 / GCP 62 / Azure 59 are not formal pass/fail determinations |
| B-1 Explanation Cleanup / Post-hoc Diagram | [PR #11](https://github.com/moruku36/cloud-validation-level3-astra-light/pull/11), diagram ce6a1be764c7e46a233598618ef9a1baf9e5d2cd | For explanatory purposes; does not overwrite comparison priors or formal requirements |
| B-2 Initial | 7daa93c08be4508632af5d4669702a5bccb5bd67 | [Initial Artifact](https://github.com/moruku36/cloud-validation-level3-astra-light/tree/7daa93c08be4508632af5d4669702a5bccb5bd67/experiments/B/B-2). Not a reconstruction |
| B-2 Complete / B-3 Baseline | cbcc26dc4d6f471e0934bb5fac7200411a038321, [PR #12](https://github.com/moruku36/cloud-validation-level3-astra-light/pull/12) unmerged | [B-2](B-2/README.md). Verified git match with latest head |
| B-3 Baseline / Limited Revision | Baseline independent commit 9047d62, Revision c0cf660d14af3ed67559a1d8d0244ddf4f164fd7 | [baseline](B-3/baseline.md), [limited revision](B-3/revised-design.md). Final PR/head documented in [handoff](../../handoff.md) |

Identical business workload, data volumes, domestic storage, recovery, non-production, monitoring, and email requirements were applied across all three providers, evaluated at 10% tax and 150 JPY/USD, without applying free tiers, credits, or long-term discounts. Normal load duration, peak frequency, log volume, and in-house labor hours were distinguished as AI calculation assumptions. The AWS restriction in Phase A was not applied as a selection constraint in Phase B. Comparison via B-2 SKU changes was conditional; performance of cheaper SKUs was not assumed equivalent to earlier SKUs. Detailed methodology and sources reused B-1 documentation, with critical deltas verified in [review](B-3/review.md).

## 3 Candidate Options, Selection/Rejection, and Changes

| Candidate Option | Representative Architecture and Rationale | B-1 → B-2/B-3 Monthly Total Incl. Tax | Retention / Rejection Rationale & Reversal Conditions |
|---|---|---|---|
| AWS | Fargate ARM 2AZ + RDS PG Multi-AZ + ALB/WAF, SQL auth/outbox, SES, domestic 2-region monitoring/DR | 76,034 → 83,248 JPY + U | Retained as preferred reference due to lowest known base cost. Retention, deletion, unattended recovery, capacity, and in-house operations unverified. Re-evaluate ranking if necessary costs rise |
| GCP | Cloud Run + Cloud SQL Enterprise HA, alternative ingress/IAM, matching business constraints | 135,580 → 101,933 JPY + U | Base budget exceeded even with conditional tier switch from Plus to Enterprise. Reversal candidate if performance, routing, and cost can be satisfied under matching conditions |
| Azure | Managed container + PostgreSQL HA centered representative proposal | 216,493 → 218,588 JPY + U | Significant budget overage. Re-compare only if an alternative configuration supporting requirements can be substantiated |

The 7,214.33 JPY AWS increase stems from permanent non-production ingress, monitoring, and DR assets. GCP reflects DB delta (-217.54 USD) and Tokyo LB adjustments; Azure reflects monitoring/DR additions. Arithmetic recalculation confirmed. AWS headroom of 16,751.63 JPY is consumed by unsettled costs (U) and necessary scaling. The 20% reference figure (99,898 JPY) is not treated as "settled budget compliance within 100,000 JPY." No double-counting among production, non-production, and external dependencies was detected; lack of actual meter/application verification remains. [Cost Review](B-3/review.md) and [B-2 Breakdown](B-2/cost.md) govern. Excluding labor costs does not justify ignoring auth/monitoring maintenance burdens.

The transition from I to F added two paragraphs explaining GCP routing/IAM and the original withdrawal outbox deadline. In B-3, the original B-2 text was preserved, while S3 replica deletion / failure handling, RDS 0–35 day correction, Route 53 query log location, administrative image role remand, and KMS cleanup exceptions were supplemented. Budget, business requirements, and overall architecture were not altered.

## Evaluation, Errors, and Unresolved Items

| Evaluation Version | Self-Assessment | Design Determination | Human Evaluation |
|---|---:|---|---|
| Initial (I) | 66 / 100 | Fail | |
| B-2 Complete (F) | 66 / 100 | Fail | |
| B-3 Limited Revision (R) | 66 / 100 | Fail | |

Detailed point grounds, fixed SHAs, and formulas are in [scores](B-3/scores.md). All categories scored 3 or above, but the total remained under 80, and five of the six mandatory categories (Architecture, Security, Availability, Cost, DR) remained at 3, failing acceptance criteria. Honest deferral of vendor selection was not penalized as concealment. Limited explanatory corrections were not assumed to resolve substantive missing evidence, leaving scores unchanged. Human evaluation and adoption approval remained blank and unobtained.

The clearest typographical error found was the RDS instance retention range. For S3/Lifecycle/replication and DNS/KMS, omitted or easily overlooked conditions were supplemented with official documentation. No known arithmetic errors were found. The progression of finding → original state → change → result → scoring impact can be traced in [revised-design](B-3/revised-design.md), and unresolved items F01–F11 in [review](B-3/review.md).

H (Human Decision): Scope of domestic storage for email recipients, minimum PITR duration (7-day proposal unapproved), primary/deputy owners and hours for auth/probe maintenance, acceptance of unsalvageable valid updates. D (Design Remand): Original deadlines and re-deletion across all copies, admin image IAM, unattended recovery across all dependencies / single-AZ capacity, audit and storage routing, budget inclusive of required capacity, logical corruption salvage. E (Empirical Validation): T01–T16. Tracked in [Issue #9](https://github.com/moruku36/cloud-validation-level3-astra-light/issues/9); closing earlier Issue #4 is not treated as technical resolution. Open Issues are not closed simply because a stage completed.

Acquired human interventions are documented in [Human Intervention Ledger](../../evaluation/human-intervention.md). Initial stage requests were not counted as supplementary answers; the B-2 completion report was verified against GitHub before use. Unanswered questions were not treated as approvals. Cumulative 3 prior answers reflect existing records only; unacquired conversation interventions and timings are not inferred.

## Limits of Evidence

Items actually verified were GitHub state, history, existence of initial documents, comparison condition traceability, cost/score arithmetic, limited official specifications, 24 requirements, links, and public publication scope. Task placement, encryption, deletion, backup/PITR, salvage of valid writes, monitoring, RTO/RPO, and performance remain design rationales or plans without live verification. Entire cloud accounts and billing were unconfirmed; zero remaining resources and 0 JPY actual cloud costs on the ledger were simply inherited. Model usage fees and runtime details remain unknown.

RTO is 30 minutes from impact onset, including detection, through 300 seconds of stable operation post-recovery. RPO is a maximum 5-minute difference between failure time and latest confirmed restored data. SLAs and typical failover times are not substituted for E2E guarantees. Calendar month 99.9% availability cannot be proven in short tests. The 4-hour logical corruption target is a provisional goal from decision time; detection delays and unsalvageable losses must be stated separately. The 30-min / 5-min targets are not applied to regional outages. Legal compliance cannot be confirmed through technical review alone.

## Handoff to Phase C

The [C Plan](B-3/c-validation-plan.md) records Production vs Low (L) vs High (H) differences, per-stage prerequisites, operations, requirement tests, pass/fail evidence, duration, costs, cleanup, and interruption/resumption procedures. A small single-AZ configuration validates functionality; only production-grade H evaluates performance, single-AZ failure, DB failure, and 20 GB logical restoration. 1,000 RPS, DB failure, cost doubling, and public IP prohibition are evaluated independently from the same baseline. C-0 through C-10 proceed one stage at a time and are not initiated now.

The short-term baseline plan of 12,495 JPY + U and 50% reference buffer of 18,742 JPY + U are unapproved. Real-time testing of long-term retention and calendar-month SLOs require separate budgets. Lower-cost test configurations are not treated as proof of production performance. Resource inventories must be checked before and after each test; resources must be deleted after evidence collection, with billable overnight resources deleted and recreated via IaC. Disks, IPs, LBs, NATs, DBs, backups, logs, and keys must be inspected; state and recovery information must not be discarded before confirming resource deletion. Exceptions such as KMS deletion waits require prior approval and deadline tracking.

Separate conclusions must be maintained: B-3 documentation, evaluation, and handoff are complete based on GitHub verification; the design failed; final selection is on hold; AWS is a reference preference; and human adoption approval was not obtained. The next single stage is **limited remand to B-2**. Following resolution of human decisions (H) and design evidence supplementation (D), re-evaluation is required; transition to Phase C remains on hold until design approval, resolution of open items, separate experiment budgets, operational authorizations, and retention deadlines are established.
