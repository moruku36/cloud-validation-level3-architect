# Level3 D5 Single Inherited Improvement Trial — Public Final Report (2026-10-02)

[日本語](FINAL-REPORT.ja.md) | [English](FINAL-REPORT.en.md) | [Index](README.md)

This public edition is based on the reader-facing editorial copy. It does not change the design, review, or assessment. The originals and complete 180-file archive remain privately preserved. Public evidence is limited to relevant project material; storage procedures and internal operational records are excluded.

The independent desk assessment is **77/100**. Numerical acceptance under the original criteria is **FAIL**; the adoption decision is **HOLD**. Neither **at least 80 nor strictly above 80** was achieved. The trial ended after one design revision and one independent review/scoring pass following anonymous freezing. There were no post-score design changes, rescoring, additional trials, or model/reasoning switches.

| Condition | Result |
|---|---|
| Overall score at least 80 | FAIL: 77 |
| Strictly above 80, reported separately | Not achieved: 77 |
| All 11 categories at least 3 | PASS: minimum 3 |
| Six required categories at least 4 | FAIL: Cost 3; other five 4 |
| No unresolved P0 | Not satisfied: OWNER / SOURCE ACCESS / UNAUTHORIZED LIVE adoption prerequisites remain unresolved. No desk-design P0 was identified |
| All six hardgates PASS | Not satisfied: G1/G2/G5/G6 PASS; G3/G4 HOLD |
| Final decision | Numerical FAIL, adoption HOLD. Unanswered and unverified matters are not treated as a pass |

## Independent Scores and Grounds

| Category | Weight | Independent rating | Points |
|---|---:|---:|---:|
| Requirements | 15 | 4 | 12 |
| Architecture | 15 | 4 | 12 |
| Security/IAM | 10 | 4 | 8 |
| Availability | 10 | 4 | 8 |
| Scalability | 5 | 4 | 4 |
| Cost | 10 | 3 | 6 |
| Operations | 10 | 4 | 8 |
| Backup/DR | 10 | 4 | 8 |
| Observability | 5 | 4 | 4 |
| Complexity | 5 | 3 | 3 |
| Vendor lock-in/migration | 5 | 4 | 4 |
| Total | 100 | | 77 |

The reviewer was separate from the designer. There was no self-assessment; all human scoring fields are blank. The original rubric and formal supplement's 1–5 definitions, weights, and pass conditions were unchanged. A/B evaluates design grounds and verification plans separately from C's empirical requirements. Categories were not uniformly capped merely because measurements were absent.

Category-level grounds are in [scoring.csv](evidence/independent-review-D5/scoring.csv), the full decision in [review.md](evidence/independent-review-D5/review.md), and gate grounds in [gates.csv](evidence/independent-review-D5/gates.csv). Relative links resolve from this public directory.

## Remaining Design Deficiencies

The independent P1 findings are: (D01) operation counts, throughput, SQL contention, latency allocation, and recovery ordering for the SQL-backed AdmissionCoordinator added to all principal request paths; (D02) task-level support for the proposed initial 40–80 hours and rehearsal 16–32 hours for custom admission/epoch/fence/broker/adapter/journal implementations; (D03) budget feasibility, headroom for mandatory residual costs, and lower-cost control alternatives; and (D04) the payload, independent protection, completeness, and replay order of the journal used to salvage valid writes after logical corruption.

P2 findings are: (D05) the metric-series sum is 2422 rather than 2522, leaving 578 rather than 478 below the 3000 cap—a conservative discrepancy of 100 series; and (D06) alignment of the older S21 retry/S25 review-cadence CSV wording with governing documents and stronger current direct references. These remain in [step4-findings.md](evidence/independent-review-D5/step4-findings.md); the frozen design was not repaired.

Cost 3 does not classify price-retrieval failure as model inability. Honest separation of unknowns was credited, but comparable all-inclusive costs with tax, conditional feasibility, and sufficiently concrete alternatives remain deficient. The known GCP compute portions are 387.4464 USD for P2/dev176 and 630.72 USD for P4/dev730. Using the frozen reference FX of 156.9969 gives 60,827.88 / 99,021.08 JPY, excluding mandatory other meters and tax. Invoice FX, tax, and complete totals are U; these are neither billed costs nor guaranteed lower bounds. See [cost conditions](evidence/blind-review-design-D5/cost-configuration-D5.md), [quantities](evidence/blind-review-design-D5/conditional-bill-of-quantities.csv), [missing rates](evidence/blind-review-design-D5/quote-completeness.csv), and the [public Cloud Run pricing source](https://cloud.google.com/run/pricing).

Complexity 3 reflects insufficient support for the added custom controls' performance, failure boundaries, and implementation effort. The principal managed app/HA SQL/object/outbox architecture and IAM/deletion/recovery plans were assessed as broadly reasonable; this is not a finding that they are ready for adoption.

## Unanswered Matters and Hardgates

G3 has a ledger for all ten data/copy types and a restore-publication predicate, but deletion-start events, retention and custodianship of minimum linking information, and responsibility for external/recipient copies remain unapproved. G4 includes role-specific effort and unattended stop conditions, but named primary/deputy owners, approved hours, absence coverage, and unattended recovery authority remain unresolved.

The original seven questions are preserved in [questions-only.md](evidence/blind-review-design-D5/questions-only.md). Already fixed matters were not asked again: Japanese production/backup locations, 30-day deletion, backups retained for at most 35 days, the 99.9% scope, the 30-minute/5-minute measurement clocks, weekday daytime staffing, a tax-inclusive 100,000 JPY budget for production plus minimum development, and separate labor/domain/paid human support costs.

Unanswered matters concern additional domestic-storage/transfer boundaries; deletion completion, ledger linkage/retention, and recipient copies; logical-loss/publication/regional-DR authority and recovery targets for added dependencies; accountable people, approved effort, and absence coverage; runtime hours, burst frequency, minimum development, invoice FX/tax and headroom; growth MAU/DAU/budget/overload behavior; and mail/PITR choices. Exact Japan SKU/features/quotas/permissions/prices and the PITR watermark interface are SOURCE ACCESS. Effective IAM, performance, failover, deletion/restore, monthly SLO, and migration/cleanup demonstrations are separately classified as UNAUTHORIZED LIVE.

## Input Preservation, Trial Changes, and Model Record

The fixed input commit is `73ac52670aa4c8848b6f565236dd6094377c5613`, the main read-only confirmation from 1 October 2026. D5 did not replace it with current main. All 34 original D4 design content files and 16 independent-review files were read in full before editing. Original requirements, answers, formal supplement, rubric, and fixed REQ-01–24 fields were preserved.

The score changed from original D4's 78 to 77, a decrease of one. Cost remained 3; Complexity changed from 4 to 3; the other nine categories remained 4. New public material, a fresh independent reviewer, added controls, and limits on verifying execution settings prevent causal model comparisons or a fair clean-room comparison. The [12-topic design change table](evidence/d4-to-d5-change-table.csv) and [56-record source change ledger](evidence/changed-public-evidence-ledger.csv) are retained.

| Role | Requested configuration | Independently observable actual configuration |
|---|---|---|
| Designer | GPT-6.1 Sol High | Model/reasoning UNKNOWN. Acceptance of a request is not backend attestation |
| Fresh independent reviewer | GPT-6.1 Sol Medium | Model/reasoning/backend/seed UNKNOWN |

The designer read the earlier review's scores and findings as instructed; they could anchor improvement. The fresh reviewer was not given the designer/model identity, earlier scores, or a desired score. Before scoring, the reading scope was clarified to include score-free history inside the anonymous frozen packet, and direct full reading of all 84 files was completed rather than relying solely on reconstruction of duplicate content. The model request, inputs, design, and clocks were not changed.

Designer source records comprise 27 new records (18 accessed, 4 partial, 5 failed) and 29 retained records. Access to new Azure URLs and similar changes are disclosed as evidence confounds. The reviewer freshly checked 15 official URLs (12 successful, 2 partial regional-price retrievals, and 1 failed Cloud SQL pricing retrieval). Other mandatory rate/permission/location pages were not freshly rechecked; their frozen evidence was retained. Equality with earlier source-access conditions or actual model/reasoning settings cannot be demonstrated. [Pre-score disclosure](evidence/independent-review-D5/workflow-disclosure.md) and the [independent source ledger](evidence/independent-review-D5/source-access.csv) record the state before scoring.

## Timing and Disconnection Notification

All observed times below are UTC on 2 October 2026.

| Stage | Observed UTC | Elapsed | Fixed cap |
|---|---|---:|---:|
| Common preparation, coordinator start to Step1 | 11:29:35–11:34:26 | 4m51s; designer 3m33s | 240min |
| Step1 | 11:34:26–11:37:02 | 2m36s | 90min |
| Step2 | 11:37:02–11:54:21 | 17m19s | 180min |
| Step3/freeze | 11:54:21–12:06:02 | 11m41s | 120min |
| Step4 | 12:08:17–12:25:18 | 17m01s | 120min |
| Step5 | 12:25:41–12:30:23 | 4m42s | 90min |

Freeze verification/handoff took a separately recorded 2m15s; Step4→5 transition took 23 seconds. Core wall time was 60m48s; answer waiting, timeouts, clock resets, and unauthorized extensions were all zero. Final packaging and Library retention were subsequent delivery work outside core scoring.

After an execution-environment disconnection notification, actual file reading/command execution and agreement of all 84 hashes were confirmed at 12:29:22 UTC. The reviewer also confirmed continued tool operation. Reviewer environment-action failures were zero; design and review finished without restarting. Permission acceptance alone was not treated as completion evidence.

## Deliverables and Evidence

The D5 frozen design comprises 84 content files, 771857 bytes, or 85 files including its manifest. The independent reviewer directly read all 84 and critically reviewed 35 scenarios. Before/after verification and the coordinator's final check confirmed zero changes.

- D5 manifest SHA-256: `3d3b4bb79305606902762ae91f150beba2d33f30e607196366f62e9b6db94072`
- Unchanged rubric SHA-256: `7a3eb2157ec4fe897c5bd667fb409e70c2c98b73ca423d904e8d76c651b09987`
- Original D4 manifest SHA-256: `9572c63a74407d6bcc19aa8a96ba374111def6db22a51b0cb57cc4f313fbd29f`
- Original upstream ZIP SHA-256: `385ae1504844485e889c26792bd336531675a62332c60a252c2ba01c27e98f03` (424630 bytes; 154 files)

Original D4, the original report, complete 180-file ZIP, and existing private backups are unchanged. This publication is not identical to the complete 180-file ZIP. [PUBLICATION-MANIFEST.json](PUBLICATION-MANIFEST.json) records public evidence and its correspondence to originals; [SHA256SUMS](SHA256SUMS) records public file hashes.

Start with the [index](README.md) and [public run manifest](evidence/provenance/run-manifest-public.json). Cost tables record rates, quantities, FX, tax, exclusions, and confidence; operations-accounting.md separates role-specific labor. All design, recovery, deletion, and migration verification is a desk plan. It does not prove measured SLOs, legal compliance, billed costs, or an actual operating team. Before D5 scoring ended, no cloud account/credentials/SDK/CLI/API, Terraform, resource creation/change/deletion, fault/load tests, GitHub writes/publication, or paid external execution occurred.

## Public Edition and Discussion

GitHub documentation additions, a PR, and merging are authorized only for this publication stage. This does not authorize cloud execution. The Japanese and English reports communicate the same findings and caveats; they are not separate assessments. The [discussion](DISCUSSION.en.md) distinguishes historical D4's 78 from a separately reported clean-sheet 73 and examines D5's improvement route, the burden of added controls, and comparison limits. The existing [final report on additional conditions](../2026-10-02-final/README.md) is unchanged. D5 did not incorporate those additional conditions; its 77 must not be reused as a score for them.
