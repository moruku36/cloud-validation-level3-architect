# Level3 Cost Model and Unpriced Items

[日本語](COST-MODEL.ja.md) | [English](COST-MODEL.en.md) | [README](README.md)

Verification date: 2 October 2026 (Japan time). Public on-demand prices, in USD excluding tax. Free tiers, limited-time credits, and long-term contract discounts are not used. Unit prices are evidence as of the verification date, not a guarantee of future bills.

## 1 Comparison Conditions

- The primary system is in eastern Japan and the secondary system is in western Japan, using 730 billable hours per month. Development is separate from production, with an assumed 40 hours of operation
- The normal load of 10 RPS runs around the clock. Each 15-minute peak at 100 RPS is calculated as replacing a period of normal 10 RPS traffic. Recalculation is required if 100 RPS means additional traffic
- 10,000 registered users, 20 GB of business data plus 2 GB per month, 100 GB of images plus 10 GB per month, and 200 GB of outbound traffic per month are formal scenario inputs. MAU, email volume, CPU processing time, provisioned DB storage, and WAL volume are separate inputs
- Static and dynamic requests, normal months and the launch period, and 1,000 RPS testing are accounted for separately
- Include 14-day PITR, 90-day backups, copies within Japan, monitoring, authentication, keys, and temporary resources needed during failure or recovery. Unit prices and quantities that could not be obtained are marked U (undetermined)

## 2 Request Volumes

Normal requests = 10 × 3600 × 730 = 26,280,000. The increment for one 100 RPS peak = (100 − 10) × 900 = 81,000 requests.

| Scenario | Number of peaks | Dynamic requests per month | Purpose |
|---|---:|---:|---|
| Normal load only | 0 | 26,280,000 | Baseline |
| Steady state | 4 | 26,604,000 | Approved initial calculation assumption |
| Equivalent to one launch peak per day | 30 | 28,710,000 | Sensitivity case with 30 peaks. A comparison value that acknowledges the difference between 730 hours and a 30-day calendar month |
| Equivalent to three launch peaks per day | 90 | 33,570,000 | A concrete example of “several times,” not a forecast |

A 15-minute test at 1,000 RPS is a separate load of 900,000 requests. To include it in the monthly cost, enter the number of tests, execution environment, overlap with normal load, and cleanup time separately. The relationship between 1 million page views per month and 26.28 million dynamic requests per month is unverified. The conservative RPS calculation is used; the value has not been reduced on the basis of page views.

## 3 Common Application Unit Comparison

For comparison, assume the equivalent of 1 vCPU and 2 GiB in each region for 730 hours, plus the same capacity for development for 40 hours. This totals 1,500 instance-hours. This capacity has not been verified to meet the required load. Multiple application instances within a region, additional burst capacity, and additional capacity during failover must be added.

| Candidate | Verified Japan unit prices | Application subtotal under these assumptions, USD per month |
|---|---|---:|
| Fargate Linux/x86, Tokyo and Osaka | CPU 0.05056 per vCPU-hour; memory 0.00553 per GB-hour | 92.43 |
| Container Apps, Japan East and Japan West, active | CPU 0.000024 per vCPU-second; memory 0.000003 per GiB-second | 162.00 + request charges |
| Cloud Run, Tokyo and Osaka, instance-based Tier 1 | CPU 0.000018 per vCPU-second; memory 0.000002 per GiB-second | 118.80 |

The formulas are AWS = 1500 × (0.05056 + 2 × 0.00553), Azure = 1500 × 3600 × (0.000024 + 2 × 0.000003), and GCP = 1500 × 3600 × (0.000018 + 2 × 0.000002). AWS lists prices in GB, while the other providers use GiB; these have not been silently relabeled as identical units.

Container Apps request charges are $0.40 per million requests. Steady-state dynamic requests alone cost $10.6416, bringing the sum with the application subtotal above to $172.6416. Development requests and requests through other paths are not included. Idle discounts are not used. GCP uses instance-based pricing; charges from the separate request-based pricing model are not added. None of the options in this table includes load balancers, network traffic, security, logs, authentication, databases, or other such items.

[Official pricing and retrieval methods](EVIDENCE.en.md#pricing-sources)

## 4 Conditional DB Component Prices

**The databases below are not equivalent in performance, memory, or CPU characteristics. Do not rank them for adoption by comparing these prices.** The subtotals are included to show that the calculation can be reproduced from a specific bill of materials. They are not strict lower bounds on the minimum required cost.

### AWS RDS Option

A comparison candidate separate from Aurora. PostgreSQL db.t4g.medium is a burstable instance with 2 vCPUs and 4 GiB. Count Tokyo Multi-AZ at $0.202 per hour plus an Osaka Single-AZ read replica at $0.101 per hour, each for 730 hours. Development uses the same instance type in Tokyo Single-AZ for 40 hours at $0.101 per hour.

DB compute = 730 × (0.202 + 0.101) + 40 × 0.101 = **$225.23 per month**.

Priced subtotal including the common application example = **$317.66 per month**. DB storage, backups, inter-region transfer, additional CPU credit charges, load balancers, and other items are not included. In-region HA in Osaka is also excluded. It is unknown whether a small burstable instance can handle the DB load from sustained 10 RPS traffic and 100 RPS peaks.

### Azure PostgreSQL Option

Flexible Server Standard_D2ds_v5 costs $0.244 per hour in Japan East and $0.265 per hour in Japan West. Count HA in Japan East as two instances, primary and standby, plus one read replica in Japan West, for 730 hours. Development uses one instance of the same type in Japan East for 40 hours.

DB compute = 730 × (2 × 0.244 + 0.265) + 40 × 0.244 = **$559.45 per month**.

Priced subtotal including the common active application example and steady-state dynamic request charges = **$732.0916 per month**. Storage, backups, external monitoring, private endpoints and management features, inter-region transfer, authentication, and other items are not included. HA in Japan West is not included.

Public Flexible Server storage unit prices in both Japan East and Japan West were $0.138 per GB-month for ordinary Storage Data Stored and $0.095 per GB-month for LRS backup. However, 20 GB of logical DB data is not the same as provisioned storage. The copies required for HA, the included backup allowance and additional usage, and the long-term backup path are also undetermined, so these prices have not been added to the subtotal. Meters with the same name from the old Single Server offering or other products are not mixed in.

### GCP Cloud SQL Option

Enterprise Plus is a candidate on the assumption of 14-day PITR and Advanced DR. Current Japan DB prices could not be obtained. A Tokyo unit price was found in earlier records, but it is not used as either a current price or an Osaka price. The model is application $118.80 + DB compute U + remaining items U. Missing values are not treated as zero to conclude that GCP is cheaper than AWS or Azure.

## 5 All Inclusive Monthly Cost Formula

All-inclusive pre-tax cost = application + eastern Japan HA DB + western Japan DB + development compute + storage + 14-day PITR + 90-day backups + image delivery and outbound traffic + inter-region traffic + load balancers, DNS, WAF, and private network paths + authentication and email + monitoring, logs, and keys + recovery and deletion processing + temporary and residual resources.

For a USD model, estimated tax-inclusive cost = all-inclusive USD cost × billing exchange rate × applicable tax factor + contingency allowance. For JPY billing, use the actual JPY SKUs and contract terms. Do not equate the current market exchange rate with the exchange rate actually used for billing. Explicitly leave the applicable tax, exchange rate, and contingency percentage undetermined rather than choosing arbitrary values to make the estimate fit the budget.

| Required item | Quantity and pricing inputs | Cost effect of undetermined inputs |
|---|---|---|
| Application and DB capacity | CPU and memory, instance count, performance tests, connections, burst duration | Two primary-side instances or HA in western Japan increases fixed costs |
| DB storage | 20 GB plus growth, indexes, headroom, provisioning increments, in-region and inter-region copies | Logical data volume alone is insufficient for an estimate |
| PITR and backups | Daily changes, WAL, compression and deduplication, 90-day usage, copies within Japan | Match the actual method instead of simply calculating 20 GB × 90 |
| Images and traffic | 100 GB plus growth, 200 GB outbound, cache hit rate, requests, inter-region copies | Distinguish CDN, network, and request charges |
| Authentication and email | MAU, login methods, messages sent, storage locations, additional add-ons | Do not infer these automatically from 10,000 registered users |
| Operations infrastructure | Log GB and retention, metrics, probes, keys, secrets, audits, recovery control | Include both normal operating costs and incident-related increments |
| Development and testing | 40 hours, storage while stopped, startup constraints, test copies | Stopping compute alone does not reduce the cost to zero |
| Recovery and failure | Temporary simultaneous DB instances, snapshots and traffic, waiting for cleanup | Higher costs in the first month or an incident month |
| Billing | Seller currency, tax, exchange rate, contingency, charges that continue while resources are stopped | Comparison with the final tax-inclusive limit is required |

## 6 Budget Assessment

The all-inclusive price comparison across the three providers is incomplete. Compliance with a tax-inclusive budget of JPY 200,000 for the first month and JPY 100,000 for subsequent months cannot be determined. The AWS figure of $317.66 and Azure figure of $732.0916 are only partial subtotals for different selected DB components.

The Azure example has a large fixed DB compute cost, making it worthwhile to check the remaining required costs first. For the AWS example, burstable performance and unattended regional failover control should be verified before focusing on its lower price. The GCP example needs price and suitability checks for the DB and authentication with data stored in Japan. This is a proposed order of investigation, not a conclusion that any option exceeds the budget or should be adopted.

Labor, domain registration and renewal, and paid human support are outside the agreed infrastructure budget. Retain them as separate potential expenses rather than treating them as free. This deliverable is the final desk-based model, comprising quantity formulas, verified component prices, and explicitly unpriced items.
