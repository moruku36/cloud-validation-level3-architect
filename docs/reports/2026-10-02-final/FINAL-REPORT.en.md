# Level3 Cloud Architecture Thought Experiment Final Report

Prepared: 2 October 2026, Japan time

Language: [日本語](FINAL-REPORT.ja.md) | English · [Package guide](README.md)

## 1 Conclusion

**This thought experiment concludes with the clarification of additional requirements, comparison of AWS, Azure, and GCP candidates, identification of conditions that prevent acceptance, and verification of partial prices.** A two-region architecture within Japan is worth considering, but neither a combination of products and operations that meets every specified condition nor an all-inclusive total within the tax-inclusive budget has been demonstrated. No cloud provider has been selected.

The following three areas should receive priority if the work proceeds toward a production design.

1. Domestic storage and deletion deadlines for personal data, including authentication, email, and monitoring. A database in a Japanese region alone cannot establish compliance with this requirement
2. Unattended recovery that distinguishes a region-wide outage from logical corruption. Database replication alone cannot guarantee a 30-minute RTO and five-minute RPO for the core functions
3. Complete costs, including databases in two regions, backups, authentication, and networking. Comparable all-inclusive estimates remain incomplete; missing prices are not treated as zero

The historical D4 assessment on 1 October 2026 was 78/100 and HOLD. Two gates, deletion evidence and operational responsibility, remained HOLD, and Cost scored 3. The new conditions addressed here differ from those assessed then, and no new independent scoring has been performed. Completing a research report is distinct from passing acceptance, selecting a system, or starting production operation.

## 2 Requirements and Changes

“Confirmed” conditions in the table below are design requirements. They do not establish permission to delete, purchase, or operate anything, or confirm legal compliance. The decisions of 2 October take precedence where they conflict with older material.

| Item | Final design condition | Change from earlier conditions and implications |
|---|---|---|
| Service | Registration, login, profiles, list/detail views, favorites, and administrator updates; images and notification email included | Payments, video, real-time chat, heavy analytics, and user image uploads are outside the initial scope |
| Load | Continuous 10 RPS, 24 hours a day, with a 9:1 read/write ratio; 100 RPS for 15 minutes | Continuous 10 RPS is an initial calculation assumption approved on 2 October |
| Bursts | Four per steady-state month; launch sensitivity cases of once and several times per day | Frequencies are revisable calculation assumptions, not committed forecasts |
| Independent load | 1,000 RPS for 15 minutes | A separate test or future scenario, not blended into normal costs |
| User scale | 10,000 registered users, 1 million page views/month, 500 peak concurrent users, and a future scale of 1 million registered users | Registered users are not automatically converted into MAU or traffic; consistency between page views and dynamic RPS is unproven |
| Data | 20 GB business data plus 2 GB/month, 100 GB images plus 10 GB/month, and 200 GB/month outbound traffic | Existing formal scenario inputs; GB, billable GiB, allocated database capacity, and update/WAL volume are distinct |
| Availability | At least 99.9% per calendar month for core functions, including planned downtime and authentication/data-dependency failures | Administration screens and notification email delays are outside this same SLO, but remain subject to monitoring and recovery |
| Performance | Core API p95 ≤ 500 ms and server-side error rate < 1% | Email delivery completion time is excluded from these performance metrics |
| Domestic storage | Personal data must be stored in Japan, including authentication, email, and monitoring | Additional categories are confirmed; evidence remains necessary for keys, management metadata, external transmission, and recipient-side responsibilities |
| Regional architecture | Primary in eastern Japan, secondary in western Japan, with automatic failover even when the owner is absent | Regional disasters, previously outside the guaranteed scope, are now included in the RTO/RPO targets |
| Regional recovery | Target RTO ≤ 30 minutes and RPO ≤ 5 minutes | Not measured; the existing RTO clock runs from the onset of impact until completion of five stable minutes after restoration of core functions |
| Logical corruption | Automatic recovery from accidental deletion and corruption under predefined conditions; target loss of valid updates within five minutes | Stopping and notifying when a safe recovery point is unknown is a proposed safeguard; detailed activation criteria are neither approved nor designed |
| Logical recovery time | Provisional target of recovery within four hours from the decision to begin recovery | The five-minute loss target does not change the recovery-duration target; this earlier clock excludes the period before detection |
| Backups | Retain for 90 days, then expire and delete successively | Changed from the earlier maximum of 35 days; this does not mean 90-day PITR |
| PITR | 14 days of recovery history | The earlier seven-day proposal is not adopted; this is distinct from long-term snapshots in function and price |
| Live-data deletion | Within 30 days of receiving a deletion request | The starting point is confirmed; backups must not be used normally before expiry, and deletion must be reapplied after restoration |
| Deletion notices | Separate notices for live-system deletion completion and final completion after backups are also gone | Notification routes and completion criteria covering every copy require design |
| Deletion ledger | Matching ID, receipt date, and completion dates only; no names or email bodies; retain until no later than one year after final deletion completion | A pseudonymous ID does not guarantee anonymity; the ledger's own replication and deletion must be managed |
| Operations | Service operates 24/7; human response is during weekday daytime; an assistant provides initial analysis and difficult decisions go to the service owner | Actual monitoring, automated recovery infrastructure, and accountable people are separately required; 24-hour human response is not guaranteed |
| Budget | JPY 200,000 including tax in the first month and JPY 100,000/month thereafter, covering production and minimally separated development/validation | Includes mandatory traffic, DNS, monitoring, backups, security, authentication, and email; labor, domain purchase/renewal, and paid human support are separately stated |
| Development | Separate from production, started as needed, with a calculation assumption of 40 hours/month | Includes storage, IP, and other costs while stopped; not a time commitment or execution schedule |
| Overload | Scale within budget, then limit admission and provide retry guidance | Autoscaling alone is not assumed to guarantee a strict billing cap |

Pinned versions of the original formal business answers and supplement are listed in the [evidence register](EVIDENCE.en.md).

## 3 Architecture Candidates for the Three Providers

These are final candidates for comparison, not product selections or confirmed SKU capacities. Their shared logical architecture comprises an application and regionally highly available database in eastern Japan, a standby application and asynchronous database replica in western Japan, an independent deletion ledger, monitoring and recovery control, and domestic backups. Regional HA and cross-region disaster recovery are treated separately, and the recovery destination's configuration must also be managed.

| Comparison | AWS Tokyo and Osaka | Azure Japan East and Japan West | GCP Tokyo and Osaka |
|---|---|---|---|
| Application candidate | ECS Fargate and regional load balancers | Container Apps with a suitable public entry point | Cloud Run with a suitable load balancer |
| Database candidate | RDS PostgreSQL Multi-AZ plus an Osaka read replica; Aurora Global Database is a separate candidate | PostgreSQL Flexible Server HA plus a Japan West read replica | Cloud SQL Enterprise Plus HA plus an Osaka DR replica |
| Regional failover | External control for replica promotion and entry-point switching; the Aurora option also needs fault decisions and an invoking actor | External control is required because replica promotion is not automatic by default | Control is required to invoke Advanced DR and align entry points and dependencies |
| 14-day PITR | Within the RDS retention-setting range | Within the standard retention-setting range | Enterprise's seven-day limit is insufficient; change to Plus or another suitable option |
| 90-day backups | Snapshot retention and expiry deletion separate from 14-day PITR | A long-term retention path separate from the standard 35-day limit | Select a backup method supporting 90-day retention and a domestic destination |
| Domestic authentication | Cognito MRR or another option; regional applicability and secondary-region restrictions need confirmation | External ID Japan Go-Local or another option; additional charges and exceptions need confirmation | Using Firebase Authentication unchanged lacks evidence of suitability; another architecture satisfying domestic storage is required |
| Cost evidence | Japanese Fargate and RDS rates confirmed; all-inclusive estimate incomplete | East/West Container Apps and database rates confirmed; all-inclusive estimate incomplete | Japanese Cloud Run rates confirmed; retrieval of current Japanese database rates incomplete |
| Selection decision | Deferred | Deferred | Deferred |

RDS is a comparison candidate in this report, not a substitute for Aurora pricing. A small burstable AWS database and an Azure General Purpose database are not assumed to offer equivalent performance. Selection must not simply follow ascending price.

### Verified Product Facts

- Cloud SQL Enterprise retains PITR logs for at most seven days; Enterprise Plus supports up to 35 days. Advanced DR is available only in Plus. [Official edition comparison](https://docs.cloud.google.com/sql/docs/postgres/editions-intro), [Advanced DR](https://docs.cloud.google.com/sql/docs/postgres/use-advanced-disaster-recovery)
- Azure PostgreSQL read-replica promotion is not automatic by default. Standard backup retention is at most 35 days. [Promotion](https://learn.microsoft.com/en-us/azure/postgresql/read-replica/concepts-read-replicas-promote), [Backups](https://learn.microsoft.com/en-us/azure/postgresql/backup-restore/concepts-backup-restore)
- RDS provides PITR within retention ranges such as 1–35 days and supports cross-region read replicas. Promotion, traffic, and backups are treated separately. [PITR](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html), [Cross-region replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.XRgn.html)
- Aurora automated backups also support up to 35 days, and data loss during Global Database failover depends on cross-region lag. [Backups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html), [Failover](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html)

## 4 Conditions for Domestic Storage and Deletion

Domestic storage must be checked through an inventory covering not only user tables, but also authentication profiles, email addresses, bodies and delivery logs, monitoring logs containing IP addresses and similar information, audit records, backups, and recovery replicas. Even if logs are anonymized or minimized, the remaining information must be classified and its storage location evidenced.

Official Firebase documentation states that Firebase Authentication is processed only in the United States and describes deletion from live and backup systems within 180 days after a user is deleted. It cannot be adopted as evidence that the current domestic-storage and 90-day residual-retention policy is satisfied. Entra External ID offers paid Japan Go-Local residency, but feature-specific data-location exceptions still require investigation. Cognito MRR has additional costs and pool-eligibility conditions; the secondary region does not support new registrations, profile changes, password resets, and certain other operations. These observations do not mean that Google, Azure, or AWS as a whole is unsuitable.

[Firebase privacy](https://firebase.google.com/support/privacy), [Entra residency](https://learn.microsoft.com/en-us/entra/fundamentals/data-residency), [Cognito MRR](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-multi-region.html)

The service operator cannot fully control storage locations or deletion within the receiving email service chosen by a user. Domestic storage on the operator's side, external delivery providers, and recipient-side responsibilities must be defined separately. No unapproved overseas-storage exception has been introduced here.

### Recommended Deletion and Restoration Procedure

The following is a design proposal that has not been implemented.

1. Record a matching ID and deadline when a request is received, and enumerate the affected copies
2. Process live copies in production, replicas, authentication, indexes/caches, email, monitoring, and related systems, then issue the first completion notice
3. Prohibit normal use of the affected data in backups, and track the expiry and processing result of every backup that still contains it
4. Before exposing a restored environment, reapply the deletion ledger entries since the restoration point and confirm that the affected data has not reappeared
5. Confirm that no affected copy remains, then issue the second completion notice; also delete the ledger after its approved retention period

Setting “90-day retention” alone does not prove erasure of every copy. If live-system deletion takes up to 30 days and backups continue to include the data during that period, residual retention could reach approximately 120 days from the request. Final notification must not uniformly be scheduled for “90 days after the request.” Actual final completion depends on expiry and verified deletion of the last backups containing the data. Provider-side erasure delays after expiry and the handling of legal exceptions remain unconfirmed.

A minimal ledger without names or email bodies does not necessarily enable delivery of a final notice after an address has been deleted. A user-held lookup receipt is a candidate, but requires separate approval and design. Other unresolved issues include the personal-data linkage of the matching ID itself, ledger backups surviving beyond the one-year deadline, and how to establish re-deletion completion if the ledger is lost.

## 5 Conditions for Automatic Recovery

### Regional Outages

East-to-west failover must be measured as a complete recovery procedure: external synthetic detection, corroboration using multiple signals, replication-lag checks, fencing and isolation of the former primary's writes, database promotion, route changes, core-function validation, and five minutes of stability verification. DNS TTL alone is not the recovery time. The system must prevent simultaneous writers in both regions during a partition. Monitoring, execution infrastructure, and keys need placement that avoids failing together with the eastern region, plus safeguards that stop unsafe action when automation misfires.

The five-minute RPO must be measured using actual committed writes and the recovered watermark. The precise trigger boundaries for stopping to avoid data loss versus prioritizing availability when lag exceeds five minutes remain undesigned. Automatic failback to the recovered former primary is not implicitly authorized by the answers gathered for this report.

A Single-AZ database in the west can reduce costs, but weakens in-region resilience after failover. If the western database is also made highly available, its extra cost must be compared with the post-failover SLO. The cost model's single-western-instance example is not a selected architecture that resolves this trade-off.

### Logical Corruption

Erroneous updates and deletions also replicate, so regional failover alone does not resolve logical corruption. Fourteen-day PITR is the window within which past recovery points can be selected; it is not a guarantee of losing no more than five minutes of valid writes.

For example, if corruption is discovered one hour later and the entire database is simply rolled back to just before it occurred, the intervening hour of valid updates may also be lost. Meeting the five-minute target requires early detection, identification of the correct recovery point, selective replay of valid updates, and consistency validation of the restored environment. Stopping and notifying when safety cannot be demonstrated is a reasonable candidate safeguard, but does not guarantee successful automatic recovery. This is a design inference applicable to all three providers.

## 6 Cost Conclusion

The [cost model](COST-MODEL.en.md) records the official Japanese-region rates and calculations that could be obtained. Required instance counts, database performance, backup capacity, authentication MAU, and other inputs remain unsettled, so a complete all-inclusive estimate for each of the three providers cannot be presented. This is explicitly an unmet part of the deliverable.

Raising the first-month budget to JPY 200,000 does not eliminate two-region fixed costs from month two onward. Even a development environment running for only 40 hours retains database/storage shutdown constraints, restart behavior, backups, and related costs. The comparison continues to avoid dependence on free tiers or long-term discounts.

Monthly billing alerts may arrive late. Budget controls therefore need a combination of pre-set capacity limits, real-time admission control, queue/retry limits, and traffic/log restrictions. Rejected requests must not be counted as successful requests to make the SLO look better. If the defined performance conditions up to 100 RPS conflict with the budget-driven restriction policy, that conflict must be reported as an unmet requirement.

## 7 Operations and Remaining Decisions

Initial analysis by an assistant and escalation to the service owner do not replace monitoring agents, execution authority, notification routes, or coverage when the responsible person is absent. With normal human response still limited to weekday daytime, meeting the RTO must not assume that a person will always decide at night. Unresolved matters include an emergency deputy, approved working hours, emergency key operations, and implementation conditions for safe shutdown and reopening to users.

Labor is listed separately from the infrastructure budget. Historical D4 estimates such as 32–64 role-hours/month, 40–80 person-hours initially, and 16–32 person-hours for the first recovery/deletion verification were assumptions under the earlier conditions. They are neither confirmed effort for the new unattended regional DR requirement nor contract estimates. They have not been converted into confirmed monetary totals here.

## 8 Evidence Required Before Production Adoption

The following stages require separate execution permission, spending limits, and defined test targets.

- Measure core API p95, error rate, CPU/database connections, and billable quantities under normal 10 RPS, 100 RPS for 15 minutes, and an independent 1,000 RPS for 15 minutes
- Measure recovery clocks for process, runtime, database, single-AZ, and regional failures, including owner absence, monitoring failure, network partitions, and prevention of dual writers
- Verify replication watermarks, the oldest 14-day PITR point, 90-day backup expiry, key availability, and loss when corruption detection is delayed
- Recover valid updates and re-delete departed users' data in an isolated restored environment; reject unsafe recovery when the ledger is missing or corrupted; reconcile deletion receipts for every copy
- Gather evidence of actual domestic-storage settings, contract terms, service exceptions, and logs, email, authentication, and management metadata
- Validate authentication, profiles, favorites, read/write consistency, and core functions externally after regional failover
- Obtain Japanese-region estimates for every component close to actual billing, including exchange rates, tax, contingency, and residual costs after shutdown and cleanup
- Observe 99.9% availability continuously over a calendar month; short tests do not substitute for a monthly SLO record

## 9 Interpretation of the Results and Future Possibilities

### 9.1 What This Experiment Reached

The archived independent assessments scored D1 through D4 at **53 → 72 → 69 → 78**. The final score improved by 25 points from the first, but D2 to D3 fell by three points, so progress was not monotonic. D4 did not pass this thought experiment. The additional conditions introduced on 2 October have not been scored; this report must not be read as a reassessment of the score of 78 or an upgrade to a pass.

| Trial | Requested design model and reasoning setting | Independent score | Historical mandatory-gate status | Decision |
|---|---|---:|---|---|
| D1 | GPT-6 Luna Low | 53/100 | 2 PASS / 3 FAIL / 1 UNKNOWN | HOLD |
| D2 | GPT-6 Luna Medium | 72/100 | 4 PASS / 2 UNKNOWN | HOLD |
| D3 | GPT-6 Luna High | 69/100 | 4 PASS / 2 HOLD | HOLD |
| D4 | GPT-6.1 Sol Medium | 78/100 | 4 PASS / 2 HOLD | HOLD |

This is a history of **four requested configurations**, not a test of four different models. The actual runtime model IDs and applied reasoning settings were unverified in every trial. Independent reviewers, separate from the designers, were also requested to use GPT-6.1 Sol Medium, but their actual settings were unverified too. Astra was neither requested nor launched. These results therefore cannot be generalized into a conclusion that all current frontier models are unable to pass a cloud-architect-level task.

The historical pass conditions required an overall score of at least 80/100, all 11 criteria at 3 or above, six specified criteria at 4 or above, passage of the mandatory gates, and satisfaction of acceptance conditions for unresolved P0 items. D4 met the floor of 3 for all 11 criteria, but Cost remained 3, the total was 78, and the deletion-evidence and operational-responsibility gates remained HOLD. Gaining “two more points” alone would not establish a pass. A gate's PASS also means that its applicable desk-design definition and disclosure requirements were met; it does not establish achievement in a running environment. [Assessment history and evidence status](EVIDENCE.en.md#basis-for-the-assessment-history-and-discussion)

### 9.2 How to Interpret the Improvement

**Discussion and interpretation:** The improvement from the first to the final trial suggests that this working process increased the design's specificity and verifiability. D4 made requirements-to-evidence mappings, IAM conditions, recovery procedures, and capacity/cost assumptions more detailed, while locating weaknesses more clearly. Even without a pass, making the remaining verification needs concrete is a useful outcome.

The score differences cannot, however, be directly interpreted as differences in model capability. Design iteration, accumulated prior reviews and instructions, the scope of evidence consulted, application of the rubric, and reviewer judgment may all have influenced the score differences, and their individual contributions cannot be isolated. Records of the D2-to-D3 decline are also consistent with stricter treatment of the same shortcomings; they do not establish that increasing the reasoning setting caused worse performance. The D4 reviewer was not given earlier scores, model names, or their comparison, but the design process itself was not a controlled comparison with identical inputs and histories.

Keeping an assessment at HOLD when deficiencies and unknowns remain is also important to evaluation safety. A report that makes unmet conditions traceable supports the next decision better than creating an apparent pass by replacing unknown prices with zero or treating a recovery proposal as a measured guarantee.

### 9.3 Expectations and Conditions for Stronger Future Models

**Hypothesis:** If future models become better at handling requirements consistently, detecting designs that conflict with product specifications, integrating evidence, and appropriately withholding uncertain judgments, they may reach a pass in a cloud-design evaluation at the same level. The overall 25-point improvement here is one reason to continue examining that possibility. However, this improvement is not direct evidence about a future model's ability and does not predict or guarantee a date, a probability of passing, or success with the next release.

Potential improvements include better distinctions between restrictions IAM can enforce and those requiring additional controls, procedures for rescuing valid updates after late-discovered logical corruption, and cost explanations that fully connect quantities with matching rates under identical conditions. Higher quality in these areas could reduce design shortcomings.

On the other hand, greater model intelligence alone cannot supply evidence that does not exist: applicable contract and domestic-storage evidence, unavailable prices, approved accountable people and authorities, records of deletion across every copy, or observed recovery outcomes. A good model must also identify and explain infeasible conditions and evidence gaps early. It remains unproven that a feasible solution exists for the current combination of budget, products, and operational conditions; a stronger model could still reasonably conclude HOLD under those same conditions.

A future “pass” in this report means acceptance of a design deliverable against fixed evaluation conditions. It does not mean earning a professional certification, replacing the full role of a human cloud architect, or permission for unrestricted autonomous production operations. Production acceptance requires the separately authorized demonstrations in Section 8.

### 9.4 How a Future Comparison Should Be Tested

The following proposes a future comparison method. It does not start or authorize another trial.

1. Freeze requirements, the original rubric, pass conditions, reference material, available tools, and time/spending limits in advance. If the additional conditions of 2 October are evaluated, give every candidate those same conditions and report a separate series from historical D1–D4
2. In addition to the requested configuration, verify and record runtime model IDs, versions, and applied reasoning settings; leave unavailable fields explicitly unverified
3. Have reviewers independent of the designers score deliverables using the same rubric, blinded to model names, prior scores, and trial order. Examine differences between reviewers, and retain gates and supporting evidence as well as scores to the extent they can be shared
4. Run each configuration multiple times from the same initial conditions, reporting score variation, gate-pass rates, and unverified items. Compare feedback-assisted improvement trials separately from trials without that feedback
5. Separate design quality from operational demonstration. Do not require prohibited experiments for a high desk-design score; require authorized cost, recovery, deletion, and other evidence for production acceptance. Do not claim a stable ability to pass based solely on the best single run

**Overall, the result remains HOLD, while there is room to improve the design and a possibility that stronger future models could move toward a pass. That expectation is a hypothesis to test through reproducibility under the same conditions and the necessary external evidence.**

## 10 Final Status

The thought experiment and final report are complete. No new scoring, acceptance pass, production deployment, or budget expenditure has occurred. Unresolved matters remain visible, and this report does not automatically proceed to further design iteration or operational demonstration.
