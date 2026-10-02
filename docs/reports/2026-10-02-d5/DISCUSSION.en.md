# D5 Results and Discussion (2026-10-02)

[日本語](DISCUSSION.ja.md) | [English](DISCUSSION.en.md) | [Report](FINAL-REPORT.en.md) | [Index](README.md)

## Read the Records Separately

D5 was a single inherited improvement trial: the original D4 design and review were read in full before selected parts were revised. The requested designer configuration was GPT-6.1 Sol High, with GPT-6.1 Sol Medium for independent review. Actual model identities and applied reasoning settings are UNKNOWN for both. Independent scoring returned 77/100, numerical failure and adoption HOLD. Requested settings alone do not establish measured model capability.

| Record | Route and evidence | Score | Comparison treatment |
|---|---|---:|---|
| Historical D4 | Inherited improvement under earlier conditions; requested Sol Medium. Original design and review retained in this public evidence | 78/100; HOLD | Historical score unchanged; D5 is one point lower |
| Separately reported clean-sheet trial | A design route separate from inherited improvement. The score of 73 comes from the publication handoff | 73/100 | Excluded from D5 inputs and not rescored. Its original frozen packet and detailed assessment are not included here, so categories, gates, actual settings, and causes of differences are not inferred |
| D5 | Improvement of original D4; requested Sol High. One fresh independent review after anonymous freezing | 77/100; FAIL/HOLD | One point below D4 and numerically four above the separately reported 73; this is not a causal capability comparison |

The existing bilingual final report separately addresses additional conditions introduced on 2 October. Additional domestic-storage boundaries, automated regional recovery, and 90-day backups were not D5 scoring inputs. Historical D4, the separately reported 73, D5, and the unscored report on additional conditions must not be combined into one score sequence under identical conditions. No new experiment or scoring was performed.

## The Burden Added by More Specific Controls

**Discussion:** D5 made provider-specific scaling, IAM, monitoring, deletion, and recovery more concrete. It added admission limits and epoch/fence controls intended to reduce unsafe unattended behavior. Making remaining weaknesses specifically traceable is a useful outcome of this improvement route. [Design changes](evidence/d4-to-d5-change-table.csv)

However, the added SQL-backed AdmissionCoordinator became a new dependency on principal request paths without sufficient support for its operation counts, SQL contention, latency, or recovery ordering. Custom brokers/adapters/journals require task-level effort grounds; the proposed 40–80 hours and 16–32 hours were insufficiently supported. Complexity fell from 4 to 3. The assessment reflects that proposed safety controls also carry performance, cost, implementation, and operational responsibilities. The frozen design was not repaired to raise its score. [Independent findings](evidence/independent-review-D5/step4-findings.md)

Cost remained 3. Keeping unknown rates separate rather than treating them as zero was appropriate, but conditional budget feasibility covering all meters, headroom for residual costs, and grounds for lower-cost control alternatives remained insufficient. Price-page retrieval failures and pending owner answers were not simply classified as model inability.

## What the Comparisons Can Establish

Original requirements, formal answers, rubric, and pass conditions were fixed. However, the designer read earlier scores and findings, new public sources were added, and the independent evaluator was fresh. Source-access successes and failures differed from earlier trials; equality of actual models and reasoning settings could not be verified. D5 also added new controls. Consequently, 78→77 or 73→77 alone cannot establish the effect of High reasoning, a model ranking, or a universal advantage of inherited design. [Pre-score disclosure](evidence/independent-review-D5/workflow-disclosure.md)

Adding D5 to the historical D1–D4 sequence of 53→72→69→78 gives an inherited-improvement record of 53→72→69→78→77. The latest score is 24 points above the first, but improvement is not monotonic. This records requested configurations and revision histories; it is neither a controlled model comparison nor proof of a stable ability to pass. The separately reported clean-sheet 73 is not inserted as an intermediate point in this inherited series.

## Acceptance and the Next Decision

Acceptance requires not only a total of at least 80, but also all categories at least 3, six required categories at least 4, no unresolved P0, and all six hardgates PASS. With Cost3, G3/G4 HOLD, and unresolved adoption prerequisites, adding three points alone would not establish a pass. G3 awaits decisions on deletion initiation, ledger linkage/retention, and copy responsibility. G4 awaits accountable owners, approved effort, absence coverage, and unattended recovery authority.

**Hypothesis:** Stronger future models might reduce desk-design shortcomings by consistently explaining the minimum necessary controls, comparable costs and effort, and the valid-write salvage contract. There is no basis here to predict or guarantee a passing date or success with the next model. Model capability also cannot turn absent prices, regional-feature/contract evidence, owner approvals, or empirical records into verified facts.

This discussion does not authorize another trial or cloud execution. The current result remains 77/100 and FAIL/HOLD, with design deficiencies separated from OWNER / SOURCE ACCESS / UNAUTHORIZED LIVE prerequisites for the next decision. Desk results do not prove SLOs, legal compliance, bills, or actual staffing.
