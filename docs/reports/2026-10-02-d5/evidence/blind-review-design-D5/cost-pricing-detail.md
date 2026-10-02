Current D5 authority: README.md and d5-desk-change-disposition.csv. Provider adapters, global admission, API journey/sampling, timing, broker, ledger replay, staffing/migration and complete quote files govern all superseded generic proposals below. Formal original source facts govern all conditional choices. No author score or verified outcome.

# D4 current pricing authority

cost-configuration-D5.md and conditional-bill-of-quantities.csv add explicit proposed quantities and alternative sizing/runtime. The historical D3 narrow price reconciliation below is preserved as provenance; statements that no quantity is proposed are superseded by those D4 files. Prices unavailable in matched Japan tables remain U, and no finite all-in bound is inferred. Formal cap/exclusions are already answered; only invoice/quantity approval details remain open.

# D3 cost model and comparison (desk estimate; no provider selection)

Checked 2026-10-01 UTC. This revision replaces D2's conflicting Cloud SQL arithmetic with U. It supplies one common production and minimum-dev cost structure across AWS, Azure and Google Cloud. It cannot honestly produce comparable all-in monthly amounts from the frozen inputs because essential SKU/HA fit, operating cadence, dev hours, tax treatment and region rates remain unknown. `U` means unbounded/unverified here, never zero. This is a cost estimate worksheet with partial evidenced meters, not a budget pass/fail result.

## Frozen basis and billing scope

- Requirements: 1M page views/month (not equivalent to API/provider requests), dynamic normal 10 RPS, peak 100 RPS for a 15-minute event, concurrency 500, read/write 9:1; normal load duration and number/frequency of 100 RPS events are not specified. Future stress case 1000 RPS for 15 minutes, likewise event frequency unspecified.
- Initial production: Japan domestic-data requirement, primary service + DB with required resilience, images 100 GB + 10 GB/month growth and 200 GB/month outward image transfer, business data 20 GB + 2 GB/month, backup max age 35 days, monitoring/security/auth/email/network as required. Region/legal acceptance for every dependency remains unresolved. This list does not imply a concrete product SKU.
- Minimum dev: one minimum independent development/verification environment alongside production. Environment count beyond “minimum”, runtime hours, database/data volume, sharing policy, security/monitoring, and uptime are U. No assumed 176h/month, free tier, credit, or inactive shutdown.
- Tax-inclusive cap: ¥100,000/month for production + minimum dev + required fees. Labor, domain purchase/renewal, and paid human support are excluded, and must be shown separately. No public price here is deemed tax-inclusive. Do not apply a generic tax multiplier: seller, customer, contract, Japanese consumption-tax invoicing/reverse-charge handling and applicable billing taxes are unknown. Tax amount remains U. The formal buyer answer controls scope; no legal/tax conclusion is made.
- Keep list prices in original USD. Currency sensitivity: ECB 2026-09-30 cross-rate = ¥156.9969/USD, retrieved 2026-10-01 UTC. Formula JPY sensitivity = USD × 156.9969; do not discard or replace source USD. This is not an invoice FX guarantee; refresh provider billing FX and bank spread at quote/invoice. (See official-source-extracts.md.)
- No paid credits, free tiers, savings plans, committed use discounts, private discounts, spot/interruptible pricing or term commitments are applied. No cloud resources were created or billed.

## Comparable initial production + minimum-dev ledger

`cost-ledger.csv` gives all three providers the same mandatory-meter columns. Price-bearing quantities are only counted where an input is fixed and the exact matching official public rate is captured. The comparable all-in result for each provider is `sum(priced eligible mandatory meters) + U meters + unknown applicable tax/FX margin`. Because of the U remainder, there is no finite defensible total or upper bound and no cap verdict.

| Provider | Production: evidence-bearing amount | Minimum dev amount | Full pair estimate | Current state |
|---|---|---|---|---|
| AWS | Route 53 illustration: 1 zone + 1M standard DNS queries = $0.90/month (assumed counts, not bill of required production). Tokyo compute, SQL HA, storage/backup/PITR, egress, LB/WAF, telemetry, auth/email and quantity-specific DNS/IP: U. | Same provider's smallest appropriate isolated app/SQL/storage/monitoring configuration and operating hours are U; Fargate pricing table has no auditable Tokyo rate in this capture. | `$0.90 DNS illustration + U production meters + U dev meters + tax` = U. | Partial global example only; not a floor guarantee for a deployable architecture and not comparable total. |
| Azure | Japan East production runtime, DB/HA, storage/backups, transfer, network/LB/WAF, observability/security, identity/email: U. Exact current selector/SKU values not exposed. | Same provider's minimum independent dev meters and hours: U. | `U production meters + U dev meters + tax` = U. | No priced mandatory component usable in an all-in estimate. |
| Google Cloud | Cloud Run standard rates are visible, Tokyo listed. For one peak event, the fixed request-meter sensitivity is `100 RPS × 900s = 90,000 requests × $0.40 / 1,000,000 = $0.036/event`, only if those 90,000 requests actually reach a request-billed Cloud Run service. At 1000 RPS, one 15-minute event = 900,000 requests = $0.36/event, same caveat. CPU/memory, scaling, SQL, storage, backups/PITR, transfer, ingress/LB/WAF, telemetry/security, auth/email: U. | Cloud Run can be priced only when runtime/memory/replica/time are chosen. Minimum dev hours/size, Cloud SQL and other meters: U. | `$0.036 × N100 RPS events + $0.36 × N1000 RPS events + U production + U dev + tax`; each event count is U. Total U. | Narrow variable request-meter sensitivity only. No all-in figure. Cloud SQL rates explicitly quarantined. |

The request-based Cloud Run sensitivities are alternative models and do not include CPU/RAM time; they cannot be generalized from PVs. Do not add instance-based costs for the same Cloud Run workload. The 90,000 and 900,000 request counts follow the user-specified burst rates/duration, but no monthly burst count is inferred. They are not estimates of total burst cost.

## Auditable cost formulas and bounded sensitivities

- 730-hour steady month convention is used only to normalize hourly meter equations. It does not assert that an app/load runs at a specific demand for 730 hours. `H_run`, active seconds, concurrency, replica count, request count, DB shape, provisioned storage/IO and dev hours stay variable.
- AWS Fargate compute form: `replicas × [(vCPU × Tokyo rate_vCPU/s) + (GB × Tokyo rate_GB/s) + (extra ephemeral GB × rate_GB/s)] × billed seconds`. This capture supports billing dimensions, second granularity, minimum one minute and supported sizes, but not auditable Tokyo unit rates. Fargate run/SKU, replica/time and add-on charges are U. US-East examples are explicitly excluded as regional proxies.
- Azure DB/compute/disk/network forms require selected `Japan East` SKU and meter quantity. Current accessible page rendering did not return a region-price table; D2 amounts are not carried forward. All mandatory Azure price rows therefore U.
- Cloud Run instance-based: `vCPU-seconds×0.000018 + GiB-seconds×0.000002` (standard USD rates, Tokyo is a listed region). Request-based active: `vCPU-seconds×0.000024 + GiB-seconds×0.0000025 + requests/1,000,000×0.40`, plus idle minimum-instance CPU/RAM where applicable. No min-replica count, app execution time, memory, concurrency or request multiplier is invented. One 100 RPS 15m event incurs request-only $0.036; one 1000 RPS 15m event incurs request-only $0.36. Multiply by actual event count only after owner/workload supplies it.
- Burst CPU/RAM charges cannot be bounded from RPS alone; code time, CPU-seconds/request, instance concurrency, memory floor, cold starts, autoscaling and max instances are unknown. Do not infer compute from request charge.
- SQL design cost formula (all providers): primary and standby/HA compute + allocated storage + I/O + backup/PITR/log storage + transfer + monitoring + any required replica. Database SKU and PITR lookback are unanswered. Database totals U.
- Object cost formula: stored live + noncurrent versions + delete markers/retained copies + requests + retrieval + replication + egress. Version count and request distribution unknown; storage age/retention lifecycle not supplied. No object upper bound.
- Image egress fixed at 200 GB/month, but charged path/pricing class/cache hit ratio/allowance vary by service and region. No usable all-provider comparable rate captured; egress amount U.
- 35 days is a maximum backup age requirement, not database PITR lookback, backup data size, retention shape, or restore/test frequency. No PITR SKU or backup amount assumed.
- Actual monthly cap headroom = `¥100,000 − (production tax-inclusive monthly invoice + minimum dev tax-inclusive monthly invoice)`. Required buffer for FX/usage/rate variation has no accepted numeric value. Do not report a pass until a priced complete quote, tax basis, headroom/buffer, and alert/limit controls are documented.

## Sensitivity limits

Only the Cloud Run request meter is bounded directly from fixed request-rate × 15-minute duration and public official rate. For normal 10 RPS, monthly event duration is unknown, so no monthly request cost bound is made. For peak events, request fee sensitivity is exact per event but monthly quantity is `U`. No quote/all-in upper or lower scenario is defensible for any provider because unknown components include database HA and backup, network, logging, security, identity, email, minimum dev and tax. A priced DNS/request example is not a lower bound for a complete service if the service shape itself is unsettled. This explicitly replaces D2's “priced subtotal is lower bound” overclaim.

## FX and tax calculation steps

1. Report every vendor's displayed USD original amount and product unit.
2. Convert to JPY sensitivity at the official ECB 2026-09-30 cross rate retrieved on 2026-10-01: `(EURJPY 178.27) / (EURUSD 1.1355) = JPY 156.9969 per USD`; retain four decimals for work, round display only.
3. Estimate tax-inclusive total only from actual seller/customer invoice treatment. The requirements specify tax inclusive; list-rate capture does not prove the amount includes Japanese consumption tax or other taxes. This line remains U pending bill-to/contract review. No jurisdictional or legal inference is made.
4. Add FX volatility/bank spread margin and usage buffer only when a buyer-approved percentage or quote exists; presently U. Show USD before conversion, converted JPY, tax, buffer and invoice currency separately.

## Source links and capture status

Exact URLs, extraction date, source lines, scope, inclusions/exclusions and retrieval failure descriptions are in `evidence/public/official-source-extracts.md`. Official sources used: AWS Fargate and Route 53, Azure PostgreSQL pricing page, Google Cloud Run and Cloud SQL pricing, ECB USD/JPY charts, Japan NTA consumption-tax guide. No public source supports an exact comparable all-in production-plus-dev estimate in the current capture. Access failure is evidence limitation, not a model failure.
