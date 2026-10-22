# Glossary and Abbreviations

[日本語](glossary.md) | English · [README](../README.md)

A list of the repository's own abbreviations, prefixes, and verification codes. This is the English counterpart of the Japanese [glossary](glossary.md), with the same sections and the same information.

> **Addendum of 2026-10-14.** The opening "When a code is unclear" table and Sections 5–8 were added. Sections 1–4 keep the September wording. No new experiment or scoring was done. Where a source does not define what a code stands for, the expansion is not guessed.

## 0. When a code is unclear

The same letters are used for different purposes at different times. Do not rely on the letters alone; check the source.

| Letters | How they are used | Meaning | Details |
|---|---|---|---|
| **A / B / C (C-0, C-1, ...)** | September workflow stages | A: single-cloud design; B: three-provider comparison and selection; C: empirical stage (C-0 is preparation, C-1 includes the read-only console check) | Section 2 |
| **D** | September task label | A design-feedback task sent back after the B-3 review | Section 1 |
| **D1–D5** | October trial identifiers | Independently assessed trials. The formal title of the D5 report is "single inherited improvement trial" | Section 5 |
| **D01–D06** | Finding IDs in the D5 independent review | P1 and P2 findings of trial D5 (separate from the trial identifiers) | Section 5 |
| **G0–G11** | September C-1 execution gates | Twelve safety gates before moving to a real environment | Section 2 |
| **G1–G4** | September B-2 limited-completion groups | Four design-completion groups fixed in the C-0 work contract (example: G1 covers recovery, deletion, and retention periods) | Section 7 |
| **T1–T5** | Requirements diagram node IDs | Node IDs in [docs/requirements.md](requirements.md); T5 is "Securing scale-up/out headroom (bottleneck identification & incremental scaling)". Illustrative decomposition, not accepted design | Section 6 |
| **T01–T16** | Future validation tests | Planned verification tests, none executed. Not scored design trials (for two T05 variants, see Section 6) | Section 6 |
| **S01–S35** | D5 review scenarios | Failure, cost, and operations scenarios assessed on paper. Not live tests | Section 6 |

## 1. Action and issue-tracking codes

| Code | Name | Meaning and role |
|---|---|---|
| **H** | **Human Decision (awaiting a human decision)** | Business, legal, or staffing decisions that AI alone cannot make (mail storage scope, PITR period, in-house operations staffing, and so on). |
| **D** | **Design Feedback (limited design send-back)** | A redesign task to resolve design inconsistencies or missing grounds raised in the B-3 review. |
| **E** | **Experiment Validation (awaiting empirical testing)** | A verification item that waits for deployment and tests (T01–T16) in a real environment. |
| **REQ-xx** | **Requirement ID** | Requirement definition IDs ([REQ-01 to REQ-24](requirements.md); the source file is in Japanese). |
| **F01–F11** | **Findings (review findings)** | The eleven failure reasons and design issues extracted in the B-3 evaluation review ([review.md](../experiments/B/B-3/review.md)). |

Note: this "D" is a September issue-tracking code. It is separate from the October trials D1–D5 (Section 5) and from the D5 findings D01–D06.

---

## 2. Phase and stage abbreviations

| Abbreviation | Official name | Meaning and phase |
|---|---|---|
| **LC1** | **Limited Completion 1** | The limited completion stage of the B-2 design: a record of design completion for four groups (dependency capacity, lifecycle, IAM, retention) as preparation for C-0. |
| **CP1** | **C-0 Proposal 1** | The first approval proposal form for the Phase C minimal experiment (C-1): a document draft with a 500 JPY limit, a 6-hour limit, key waiting, and so on. |
| **CP2** | **C-0 Proposal 2** | The final version of the limited-experiment conditions and execution gates reflecting the user approval of 2026-09-12. |
| **G0–G11** | **Execution Gates 0 to 11** | The twelve-step safe-execution gates in Phase C-1 ([execution-gates-2026-09-12.md](../infra/c1/execution-gates-2026-09-12.md); Japanese). |
| **G1** | **Read-only Preflight Gate** | The first cloud-checking gate in C-1 (a quota of at most six safe read-only API calls). |

---

## 3. Cost and verification symbols

| Symbol | Meaning | Note |
|---|---|---|
| **+ U** | **Uncertain / Variable Costs (unsettled costs)** | Usage-based or variable costs not included in the basic monthly estimate (AWS: 83,248 JPY). They specifically include:<br/>- CloudWatch Logs / metric volume<br/>- Route 53 query logs and additional health checks<br/>- Data-transfer overage (above 200 GB)<br/>- Added S3 backup and version retention<br/>- Additional security audit and WAF rule charges |
| **66 points** | **Self-assessed score (fail)** | A score judged a fail against the 80-point pass bar because of insufficient grounds for domestic data storage, consistency of withdrawal deletion, and unattended recovery (66 initially and 66 after the fix). |

In the October D5 trial, items whose rates or totals are not settled are also called "U". U is neither zero nor a fact; it is an item left unsettled (Section 5).

---

## 4. Safety guards and IaC terms

| Term | Meaning |
|---|---|
| **Preflight** | A read-only pre-check of prerequisites (no duplicate resource names, roles exist, region, and so on) before connecting to the cloud or applying changes. |
| **Private Binding** | A safety mechanism that keeps real values such as AWS account IDs, execution profiles, and secret ARNs out of the public repository code (bound in an encrypted area outside the repository). |
| **Bootstrap Stack** | The local initialization stack that manages the Terraform state bucket, the KMS encryption key, and the operator IAM roles. |
| **Fixture Stack** | The resource stack, such as a test S3 bucket, that is the subject of the experiment (managed on an S3 remote backend after bootstrap). |
| **Canary** | A safe synthetic test object used to confirm that a permission denial (AccessDenied) occurs on purpose. |

---

## 5. October trials and scoring (D1–D5)

### Trial identifiers

| Code | Meaning | Source |
|---|---|---|
| **D1–D5** | Trial identifiers for the October independent desk assessments. **No source defines what "D" stands for, so it is not expanded.** The formal title of the D5 report is "single inherited improvement trial" | [D5 report](reports/2026-10-02-d5/FINAL-REPORT.en.md), [D1–D4](reports/2026-10-02-final/FINAL-REPORT.en.md) |
| **D1–D4** | Requested designer settings, in order: GPT-6 Luna Low, Luna Medium, Luna High, and GPT-6.1 Sol Medium. Scores 53, 72, 69, 78 | [D1–D4 report, section 9](reports/2026-10-02-final/FINAL-REPORT.en.md) |
| **D5** | One inherited improvement trial that revised D4. Requested designer GPT-6.1 Sol High and independent reviewer GPT-6.1 Sol Medium. Score 77 | [D5 report](reports/2026-10-02-d5/FINAL-REPORT.en.md) |
| **D01–D06** | Finding IDs in the D5 independent review (four P1, two P2). Separate from the trial identifiers D1–D5 | [step4-findings.md](reports/2026-10-02-d5/evidence/independent-review-D5/step4-findings.md) |

### Assessment terms

| Term | Meaning |
|---|---|
| **Self-assessment** | Scoring by the same agent that did the work. September A and B. Not an independent acceptance decision. |
| **Independent assessment** | Scoring by a reviewer separate from the designer. October D1–D5. Scoring of anonymous frozen packets is documented for D4 and D5. |
| **Desk assessment** | Assessment of documents. It includes no deployment or measurement. |
| **Numerical FAIL / adoption HOLD** | The state in which numerical criteria such as the score are not met, and the state in which the adoption decision is deferred. Neither is an approval of acceptance or adoption. |
| **Six mandatory categories** | Requirements, Architecture, Security/IAM, Availability, Cost, Backup/DR. Each must be at least 4. |
| **Complexity 3** | Meets the general floor of 3 for every category but lowers the weighted total. It is not by itself a mandatory-4 failure. |
| **P0 / P1 / P2** | Finding priorities. An unresolved P0 prevents acceptance. In D5 the remaining P0 items are the adoption prerequisites owner, source access, and unauthorized live checks; no desk-design P0 was identified. |
| **OWNER / SOURCE ACCESS / UNAUTHORIZED LIVE** | The three classes D5 used for adoption prerequisites: those needing a human answer, those where a source of prices, features, or permissions could not be accessed, and those needing a live demonstration that has not been authorized. |
| **U** | An unsettled cost item. Treated neither as zero nor as fact (Section 3). |
| **Requested versus actual settings** | The requested model name and reasoning setting differ from what was actually verified. Actual runtime models and reasoning settings are UNKNOWN in every trial. |
| **UNKNOWN / INCOMPLETE** | A state that could not be confirmed, and a state that stopped partway and was not completed. The C-1 console check is INCOMPLETE. |

---

## 6. Tests and verification scenarios (T, S)

**T01–T16 are validation tests planned for a future empirical stage; they are not scored design trials, and none was executed. S01–S35 are failure, cost, and operations scenarios used to review the D5 design; they are not tests in a live environment.**

### T01–T16 (B-2 validation plan)

Source: the per-requirement table in [B-2 validation-plan.md](../experiments/B/B-2/validation-plan.md) (Japanese). The table has no formal titles; the labels below are short paraphrases of the row descriptions. The pass conditions are future decision methods, not evidence of success.

| Code | What is verified (short paraphrase) | Requirement |
|---|---|---|
| T01 | Read from another connection right after an update, concurrent updates, tampering, revoked sessions | REQ-02 |
| T02 | Image bypass; mail queue stoppage, duplicates, and bounces | REQ-03 |
| T03 | Capacity analysis with 10,000 and 1,000,000 synthetic registrations | REQ-04 |
| T04 | Load of 10 RPS normal, 100 RPS for 15 minutes, 9:1 read/write, and 500 users; per-API p95 and error rate | REQ-05, REQ-06 |
| T05 | All-copy deletion at withdrawal, inventory of snapshots, versions, and clones, and re-deletion after restore | REQ-07 |
| T06 | Matching domestic-storage and path-ledger settings against contracts and official specifications | REQ-08 |
| T07 | External measurement of 99.9% over a calendar month (including handling of missing data and planned downtime) | REQ-09 |
| T08 | Unattended recovery from process, task, database, and single-AZ failures (within 30 minutes; gap to confirmed data within 5 minutes) | REQ-10, REQ-11, REQ-13 |
| T09 | Converting actual usage to a monthly amount using unit prices | REQ-12 |
| T10 | A daytime owner exercising restore, deletion, and change procedures | REQ-13, REQ-14 |
| T11 | Future load (1000 RPS, 1,000,000 users) and data growth | REQ-15 |
| T12 | Permission-denial tests, TLS, and checks for personal data in logs | REQ-16 |
| T13 | Rebuild from an empty environment, state contention, rollback | REQ-18 |
| T14 | Deletion, leftover inventory, and rebuild | REQ-22 |
| T15 | Salvage of valid writes after accidental deletion, unknown corruption, and a missing ledger | REQ-23 |
| T16 | Domestic restore in Osaka without Tokyo keys or registry | REQ-24 |

### About T05 and "T5" (two distinct namespaces)

Codes beginning with "T" belong to two distinct namespaces: requirements diagram node IDs (T1–T5) and future validation test codes (T01–T16).

#### 1. Requirements diagram node IDs (T1–T5)
Source: the "Requirements structure tree (decomposition from business constraints to technical requirements)" in [docs/requirements.md](requirements.md) (Japanese). These are node IDs representing the decomposition of business constraints (B1–B5) into technical/architectural requirements.
*Note: Products mentioned in the diagram (e.g. Fargate/RDS) and the 2AZ layout are an **illustrative example decomposition** of business constraints into technical architecture requirements, NOT an accepted or deployed production design.*

| Node ID | Exact source text in diagram | Corresponding business constraint (exact source) | Explanatory description / role |
|---|---|---|---|
| **T1** | 最小固定費・不要リソース排除<br/>(NAT・過大インスタンス見送り) | B1: 予算上限: 税込10万円/月<br/>(本番＋開発最小1環境) | Minimizing fixed costs and eliminating oversized resources (foregoing NAT and oversized instances) |
| **T2** | 2AZ同期冗長化 & 自動フェイルオーバー<br/>(夜間無人復旧・300秒安定検証) | B2: 可用性: 99.9%以上<br/>RTO≦30分 / RPO≦5分 | 2AZ synchronous redundancy & automatic failover (nighttime unattended recovery & 300s stabilization verification) |
| **T3** | 国内リージョン完結 (東京/大阪)<br/>(海外転送・外部IdPの監査) | B3: データ主権: 日本国内限定保存<br/>(DR・バックアップ含む) | Domestic region confinement (Tokyo/Osaka) (audit overseas transfer & external IdP) |
| **T4** | マネージドサービス主導 (Fargate/RDS)<br/>(OSパッチ運用・K8s運用の排除) | B4: 運用体制: インフラ専任1名<br/>(平日日中のみ・夜間即応なし) | Managed service-driven architecture (Fargate/RDS) to eliminate OS patching & K8s operational burden |
| **T5** | スケールアップ/アウト余地確保<br/>(ボトルネック特定と段階的拡張) | B5: 規模: 初期1万人 (100万PV)<br/>将来100万人 / 1000RPS対応 | Securing headroom for scale-up/out (bottleneck identification & incremental scaling) |

#### 2. Future validation test codes (T01–T16) and "T05" distinction
- **"T05" is numbered differently in different sources:**
  - **B-2 T05** (source: `experiments/B/B-2/validation-plan.md`, REQ-07 row): All-copy deletion at withdrawal, inventory of snapshots, versions, and clones, and re-deletion after restore. C-0 [blockers.md](../experiments/C/C-0/blockers.md) and B-3 [traceability.md](../experiments/B/B-3/traceability.md) use T05 in this sense.
  - **A-3 T05** (source: `experiments/A/A-3/validation-handoff.md`, REQ-23, priority P1): Salvage of valid updates within 4 hours after the decision following logical corruption, plus a cold rebuild in Osaka. Part of an independent T01–T11 numbering system.
  - Neither source gives a formal title; cite the source ID when referencing either.
- **Difference between T5 and T05**: "T5" is the requirements diagram node ID defined above ("Securing scale-up/out headroom") and is part of a separate namespace from "T05" (the validation test code). Rather than not existing, T5 is defined specifically in the requirements diagram.

### S01–S35 (D5 review scenarios)

Source: [scenario-recovery-D5.csv](reports/2026-10-02-d5/evidence/blind-review-design-D5/scenario-recovery-D5.csv) (35 rows; the status of each row is "conditional desk proposal; no approvals, execution, or outcome").

| Range | Theme |
|---|---|
| S01–S06 | Failures of an AZ, the database, a whole region, DNS, a TLS certificate, and the authentication provider |
| S07 | Mail provider outage, duplicates, and backlog |
| S08 | Accidental SQL deletion and logical corruption |
| S09 | Delay or permanent failure of deletion work |
| S10–S11 | Replication lag and permanent replication failure |
| S12–S17 | Object versions, delete markers, and multipart leftovers; backup coverage gaps; key deletion waits and key loss |
| S18–S19 | Telemetry volume and cost surge; absence of the synthetic canary |
| S20–S22 | A 1000 RPS x 15 minute growth stress, queue retry storm, connection-pool exhaustion |
| S23–S25 | Operator absence, patch backlog, vendor changes to features, prices, regions, or contracts |
| S26–S30 | Unavailable price pages, a 20% exchange-rate move, tax treatment change, monthly-equivalent cost doubling, expansion of the minimum development environment |
| S31, S33 | Survival of deletion-ledger or audit-proof copies; loss or corruption of the ledger |
| S32 | Process crash and restart loop |
| S34 | WAF false positive and a bad edge rollout |
| S35 | Change in the scope of the public-IP prohibition |

---

## 7. Gate codes (three uses of G)

Codes beginning with G belong to three separate systems. When you see G3 or G4, check which period the document belongs to.

| System | Period | Meaning | Source |
|---|---|---|---|
| **D5 hardgates G1–G6** | October (D5 scoring) | Six mandatory gates for accepting a design; all must PASS | [gates.csv](reports/2026-10-02-d5/evidence/independent-review-D5/gates.csv), [review-gates.csv](reports/2026-10-02-d5/evidence/blind-review-design-D5/review-gates.csv) |
| **C-1 execution gates G0–G11** | September (C-1 preparation) | Safety gates before moving to a real environment (Section 2) | [execution-gates-2026-09-12.md](../infra/c1/execution-gates-2026-09-12.md) |
| **B-2 limited-completion groups G1–G4** | September (LC1) | Four design-completion groups fixed in the C-0 work contract | [LC1 README](../experiments/B/B-2/limited-completion/README.md) |

### Meaning of the D5 hardgates and D5 results

The meanings follow the item names in the designer-side self-check table (review-gates.csv). A gate PASS means the desk definition and disclosure conditions were met; it does not prove achievement in a live environment.

| Gate | Item name (as in the source) | Meaning | D5 result |
|---|---|---|---|
| G1 | 100% requirement traceability and no assumed Japan residency | All 24 requirements are traceable, and domestic storage is not filled in by assumption | PASS |
| G2 | Estimate / U / variable costs separated | Estimates, unsettled costs (U), and variable costs are kept apart | PASS |
| G3 | All-copy deletion/backup/ledger/audit across every data class | Deletion, backup, ledger, and audit across all copies of every data class | **HOLD**: a ledger for ten copy classes and a restore-publication predicate exist, but the deletion-start event, retention of linking information, independent custody, and the vendor and recipient boundary are not approved |
| G4 | Owners / hours / coverage / no-human recovery | Owners, hours, coverage, and recovery without a person | **HOLD**: role-specific effort and unattended stop conditions exist, but named primary and deputy owners, actual hours and leave coverage, and pre-approved recovery authority are not settled |
| G5 | Measurable formal RTO/RPO with explicit unverified state | Measurable formal RTO and RPO, with the unverified state stated | PASS |
| G6 | Unknown never converted to fact / zero / success | Unknowns are never turned into fact, zero, or success | PASS |

A note on the short names for G3 and G4: the [D1–D4 report](reports/2026-10-02-final/FINAL-REPORT.en.md), which covers D4 (1 Oct), describes the two gates that stayed on HOLD as "deletion evidence" and "operational responsibility". Their content is close to D5's G3 and G4 above, but that report gives no gate numbers, and these are not formally defined aliases.

---

## 8. General technical terms

Standard terms, not definitions specific to this repository.

| Term | Meaning |
|---|---|
| **RTO / RPO** | Recovery time objective and recovery point objective. In this repository: 30 minutes from the start of impact through five stable minutes after recovery, and a gap of at most five minutes to confirmed data |
| **PITR** | Point-in-time recovery. It refers to a retained change-history window and is separate from long-term snapshots |
| **SLO** | A service-level objective, such as 99.9% per calendar month |
| **IAM** | Cloud permission management |
| **DR** | Disaster recovery |
| **RPS** | Requests per second |
