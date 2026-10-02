# Level3 Sources and Evidence

[日本語](EVIDENCE.ja.md) | [English](EVIDENCE.en.md) | [README](README.md)

Verification date: 2 October 2026 (Japan time). Public URLs may change in the future. The report distinguishes formal scenario inputs, the owner's decisions on 2 October, official product specifications, calculation assumptions, and unverified matters.

## Original Requirements and History

- Repository: [cloud-validation-level3-architect](https://github.com/moruku36/cloud-validation-level3-architect)
- Pinned input commit: `73ac52670aa4c8848b6f565236dd6094377c5613`
- [Formal business answers](https://github.com/moruku36/cloud-validation-level3-architect/blob/73ac52670aa4c8848b6f565236dd6094377c5613/docs/sources/business-answers-2026-09-08.md): core features, 10/100 RPS, a 9:1 read/write ratio, 20 GB/100 GB/200 GB, recovery clocks, SLOs, budget scope, and related inputs
- [Formal supplement](https://github.com/moruku36/cloud-validation-level3-architect/blob/73ac52670aa4c8848b6f565236dd6094377c5613/docs/sources/supplement-2026-09-08.md): comparison of AWS, Azure, and GCP under the same conditions, 24 requirements, assessment criteria, and the distinction between desk-based design and empirical validation
- [Earlier price extraction record](https://github.com/moruku36/cloud-validation-level3-architect/blob/73ac52670aa4c8848b6f565236dd6094377c5613/experiments/B/B-2/official-rates.json): a record as of 10 September 2026. It is not used as a substitute for current GCP DB prices
- D4 report dated 1 October 2026: the saved final report and outstanding-issues list were read, confirming the historical assessment of 78/100 and HOLD, Cost3, and HOLD for the deletion and operations gates. This is not a new assessment
- Additional decisions on 2 October 2026: the requirements confirmed with the service owner are summarized in [Section 2 of the final report](FINAL-REPORT.en.md). They are not included in the earlier pinned commit. The original private conversation and personal identifiers are excluded from public materials

## Basis for the Assessment History and Discussion

The D1–D4 scores, requested models and reasoning settings, gates, and D4 review procedure in Section 9 of the final report are based on the archived final report of 1 October 2026. That record reports scores of 53, 72, 69, and 78, with actual runtime model IDs and applied reasoning settings unverified. The D4 reviewer was not given earlier scores, model names, or their comparison, while design revisions used prior reviews and instructions. This package does not reproduce the entire historical archive.

The historical requirements are preserved: an overall score of at least 80, all 11 criteria at 3 or above, and six specified criteria at 4 or above, together with passage of mandatory gates and satisfaction of acceptance conditions for unresolved P0 items. Part of the D4 scoring explanation was corrected so that prohibited operational measurements were not treated as mandatory for a desk-design assessment; the original rubric, design, and score of 78 were unchanged.

Section 9's interpretation of improvement, expectations for future models, and proposed comparison method are discussion, hypotheses, and recommendations based on this history and the unresolved conditions in this report. They are not new experimental results, measurements of future models, or predictions of release dates. The current report incorporating the additional conditions of 2 October remains unscored and does not revise the historical 78/100 and HOLD.

The English documents are counterparts of the Japanese documents in this package, not a separate assessment or pricing investigation. Conclusions, numbers, caveats, and sources are kept aligned across languages; translation of the entire historical repository is outside the scope.

## Pricing Sources

### AWS

The Japan-region JSON files from the public Price List were read. No credentials or cloud resource APIs were used.

| Source | Items checked |
|---|---|
| [ECS Tokyo](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonECS/current/ap-northeast-1/index.json) | Fargate Linux/x86 CPU and memory |
| [ECS Osaka](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonECS/current/ap-northeast-3/index.json) | Same as above |
| [RDS Tokyo](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/current/ap-northeast-1/index.json) | PostgreSQL db.t4g.medium, Single-AZ and Multi-AZ |
| [RDS Osaka](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/current/ap-northeast-3/index.json) | Same as above |
| [Fargate pricing explanation](https://aws.amazon.com/fargate/pricing/) | Reference for billing methods and additional costs |

The ECS catalog publicationDate was 2026-09-11T12:44:25Z, and the effectiveDate of the verified OnDemand terms was 2026-07-01. The RDS catalog publicationDate was 2026-10-01T06:02:30Z. Prices are in USD. Region, engine, instanceType, deploymentOption, and OnDemand were matched.

### Azure

The [official Retail Prices API](https://prices.azure.com/api/retail/prices) was read. Regional serviceName/armRegionName, productName/skuName, and Consumption were matched. This was a read of public prices; no Azure subscription environment or resources were accessed.

- Container Apps: serviceName `Azure Container Apps`, regions `japaneast` / `japanwest`. Standard vCPU Active Usage, Standard Memory Active Usage, Standard Requests
- DB: serviceName `Azure Database for PostgreSQL`, regions `japaneast` / `japanwest`, product `Azure Database for PostgreSQL Flexible Server General Purpose Ddsv5 Series Compute`, sku `2 vCore`, armSkuName `Standard_D2ds_v5`
- Japan East DB meterId `b8337cf5-8521-5ef8-9345-c2bd0546a51d`, Japan West DB `8cd5400c-3a11-5332-83d7-34d08216b778`, effectiveStartDate 2023-03-01, unit `1 Hour`
- Japan East Container Apps CPU meter `4ef945a7-c73f-5825-9fe9-117d65d7b4a5`, memory `5b8ebac4-2c47-523d-8559-a1e51867ad3c`, requests `31e4637c-3cd6-5207-a4fb-622bdc64b639`
- Japan West Container Apps CPU meter `57e22c85-06db-5efb-9a47-1575d0287389`, memory `55f298d4-0e5b-5cf4-b469-0d3345cb0cd4`, requests `d6ad3660-587a-5956-a0db-4d91fe9bd727`

One retrieval path for the [Container Apps pricing explanation](https://azure.microsoft.com/ja-jp/pricing/details/container-apps/) returned blank regional unit prices, so the figures were verified using the public API above. Prices for other products, free meters, and reservations were not mixed in.

### GCP

- [Cloud Run pricing](https://cloud.google.com/run/pricing): verified that Tokyo and Osaka are Tier 1 and checked instance-based CPU and memory unit prices
- [Cloud SQL pricing](https://cloud.google.com/sql/pricing): the attempt to retrieve current Japan DB prices for this report failed. Unavailable figures have not been filled in from third-party articles or earlier records

## Product Specifications

| Topic | Primary source |
|---|---|
| RDS PITR | [Automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html) |
| RDS retention limit | [Backup retention](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.BackupRetention.html) |
| RDS cross-region replicas | [Cross-region replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.XRgn.html) |
| AWS long-term snapshots | [AWS Backup and RDS](https://aws.amazon.com/getting-started/hands-on/amazon-rds-backup-restore-using-aws-backup/) |
| Aurora automated backups | [Aurora backups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html) |
| Aurora Global Database failover | [Failover](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html) |
| Azure promotion is not automatic | [Promote replicas](https://learn.microsoft.com/en-us/azure/postgresql/read-replica/concepts-read-replicas-promote) |
| Azure backups and PITR | [Backup and restore](https://learn.microsoft.com/en-us/azure/postgresql/backup-restore/concepts-backup-restore) |
| Azure HA and pricing | [Reliability](https://learn.microsoft.com/azure/reliability/reliability-postgresql-flexible-server) |
| Cloud SQL editions and PITR | [Editions](https://docs.cloud.google.com/sql/docs/postgres/editions-intro) |
| Cloud SQL Advanced DR | [Advanced DR](https://docs.cloud.google.com/sql/docs/postgres/use-advanced-disaster-recovery) |
| Cloud SQL long-term backups | [Backup overview](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups) |
| Firebase Authentication data and deletion | [Privacy](https://firebase.google.com/support/privacy) |
| Entra storage in Japan and exceptions | [Data residency](https://learn.microsoft.com/en-us/entra/fundamentals/data-residency) |
| Cognito MRR and constraints | [Multi-Region replication](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-multi-region.html) |

## Evidence Limitations

What was verified consists of public specifications, public component prices, scenario inputs, and consistency of the calculations. The applicability of contractual terms, actual configuration of storage within Japan, actual SKU availability, cross-region recovery including all dependencies, performance, deletion across all copies, monthly SLOs, and actual bills remain unverified.

The following are design inferences from the stated conditions: rolling back alone cannot preserve valid updates when logical corruption is discovered late; a 30-day deletion deadline and 90-day backups can lead to final residual retention of roughly 120 days; and backups of the deletion ledger itself affect retention periods. These are not measured service results or legal conclusions.
