# Official public source extracts (D3)

Captured through public web retrieval on 2026-10-01 UTC. Direct official URLs are given for independent access. These extracts record what was actually exposed; no account, console, cloud API, SDK, or calculator was used. Shell `curl` access from this environment returned HTTP CONNECT 403, so source bundle consists of normalized verbatim table lines/extracts transcribed from public page rendering rather than raw HTML. Cloud SQL price page exceeded public fetch limits; no rate is asserted.

## Google Cloud Run

URL: https://cloud.google.com/run/pricing (retrieved 2026-10-01 UTC; public web-rendered lines 3–9, 26–33, 36–50, 96–116, 128–143, 188–218)

- Page says usage billed in pricing table after free tier; D3 excludes free tier.
- Billing depends on selected region and billing configuration. Tokyo is listed as `asia-northeast1` for instance-based and request-based services.
- Instance-based Standard USD table: CPU $0.000018/vCPU-second; memory $0.000002/GiB-second.
- Request-based Standard USD table: active CPU $0.000024/vCPU-second; active memory $0.0000025/GiB-second; idle minimum-instance CPU and memory $0.0000025/sec per vCPU/GiB; requests $0.40 per 1,000,000.
- Page says traffic to internet billed by network pricing, and VPC connector carries its own compute costs. Same-region resource data transfer is $0, and transfer to Cloud CDN/LB is $0 (lines 6–9).
- Do not count the same service under instance-based and request-based models. These rates price only service compute/request meters; they do not establish a production design or complete total.

## Google Cloud SQL

URL: https://cloud.google.com/sql/pricing?hl=ja (attempted 2026-10-01 UTC).

Public page response through web retrieval failed with `Content length is too large: 4194305+`; a repeat returned an internal fetch error. Shell public HTTP retrieval returned `curl: (56) CONNECT tunnel failed, response 403`. The price page is dynamic and the Tokyo regional selector/SKU table was not available in an auditable capture. Prior D2 states conflicting Tokyo unit rates, while its public source package says U. D3 preserves both prior statements in this note and quarantines all numeric Cloud SQL claims and their subtotals. Cloud SQL rate, region edition/SKU, HA basis, storage, backup/PITR and IO are U. No Cloud SQL number used in D3 totals.

## AWS Fargate

URL: https://aws.amazon.com/fargate/pricing/ (retrieved 2026-10-01 UTC; public page, lines 221–242, 271–299, 305–326).

- Meter dimensions: vCPU, memory, operating system, CPU architecture, storage. Timing starts at image download and ends at task termination, rounded to nearest second; minimum one minute (Windows five minutes).
- 20 GB ephemeral storage included; additional configured storage billed.
- Supported Linux/X86 sizes include 1 vCPU with 2–8 GB, 2 vCPU with 4–16 GB, etc.
- Additional charges may apply for other AWS services, data transfer, CloudWatch Logs, and public IPv4.
- Published example rate for US East (N. Virginia), not Tokyo: Linux/X86 $0.000011244/vCPU-second, $0.000001235/GB-second memory, $0.0000000308/GB-second extra ephemeral storage. This US example is not substituted as Tokyo pricing. The regional table iframe was not accessible through the page extraction; Tokyo rate U.

## AWS Route 53

URL: https://aws.amazon.com/route53/pricing/ (retrieved 2026-10-01 UTC; public page lines 214–224 and its pricing table rendered in page).

Public rate summary retained from the current official page: $0.50 per hosted zone per month for first 25 zones and $0.40 per million standard DNS queries for the first billion monthly queries. Illustrative arithmetic only: 1 zone plus 1 million queries = $0.90/month. This is a DNS-only published AWS-region unit illustration. It excludes certificates, IP, LB, logs and other required services; actual zone/query volume is U.

## Azure Database for PostgreSQL Flexible Server

URL: https://azure.microsoft.com/en-us/pricing/details/postgresql/flexible-server/ (retrieved 2026-10-01 UTC).

Public page rendered a 1,922-line shell page but the actual table values and region selector were absent from extracted body; exact official Japan East rates could not be reproduced. Search/find for `12.410`, `0.115`, `Japan East` returned no matching text. D2 cited B1ms $12.410/month and Premium SSD $0.115/GiB-month, but that old snapshot was not re-verified in this current capture. D3 therefore marks Azure numeric PostgreSQL/Storage rates U and does not use D2 amounts.

## Currency method — ECB reference rates

USD chart: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html
JPY chart: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-jpy.en.html
Retrieved 2026-10-01 UTC. Most recent completed common reference date displayed was 2026-09-30: EUR 1 = USD 1.1355; EUR 1 = JPY 178.27. Cross-rate: 178.27 / 1.1355 = JPY 156.9969 per USD (display calculation rounded to 2 decimals = ¥157.00/USD). Preserve USD original and report FX-derived JPY separately. This is a spot reference sensitivity, not provider billing FX, invoice rate, bank spread, or future quote; refresh at quote/invoice date. No BOJ rate was obtainable via public browser route in this session, so ECB was used as a primary central-bank alternative.

## Japan consumption tax reference

National Tax Agency general guide: https://www.nta.go.jp/english/taxes/consumption_tax/01.htm (retrieved 2026-10-01 UTC). Page shell loaded but keyword extraction did not return a specific rule relevant to each cloud seller/cross-border contract. The formal cap is tax-inclusive per user answer. Tax treatment, supplier invoicing, taxable classification, reverse-charge application, and local/account-specific charges cannot be inferred from public list prices. Therefore, do not mechanically apply 10% or label any cloud list-price total tax-inclusive; exact tax amount remains U until contract/invoice treatment is known.
