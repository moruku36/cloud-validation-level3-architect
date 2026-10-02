# Level3 出典と証拠

言語：日本語 | [English](EVIDENCE.en.md) · [全体案内](README.md)

確認日：2026年10月2日（日本時間）。公開URLは将来変更され得る。本文では、正式シナリオ値、10月2日の所有者決定、公式製品仕様、計算仮定、未検証事項を区別する。

## 原要件と履歴

- リポジトリ：[cloud-validation-level3-architect](https://github.com/moruku36/cloud-validation-level3-architect)
- 入力固定コミット：`73ac52670aa4c8848b6f565236dd6094377c5613`
- [正式業務回答](https://github.com/moruku36/cloud-validation-level3-architect/blob/73ac52670aa4c8848b6f565236dd6094377c5613/docs/sources/business-answers-2026-09-08.md)：主要機能、10/100RPS、読書き9:1、20GB/100GB/200GB、復旧時計、SLO、予算対象等
- [正式補足](https://github.com/moruku36/cloud-validation-level3-architect/blob/73ac52670aa4c8848b6f565236dd6094377c5613/docs/sources/supplement-2026-09-08.md)：AWS/Azure/GCP同条件比較、24要件、評価基準、机上設計と実証の区別
- [過去の価格抽出記録](https://github.com/moruku36/cloud-validation-level3-architect/blob/73ac52670aa4c8848b6f565236dd6094377c5613/experiments/B/B-2/official-rates.json)：2026年9月10日時点の記録。現行GCP DB料金の代用には使用していない
- 2026年10月1日のD4報告：保存済み最終レポートおよび残課題一覧を読み取り、78/100・HOLD、Cost3、削除・運用ゲートHOLDという履歴を確認。新たな採点ではない
- 2026年10月2日の追加決定：サービス所有者との要件確認を最終報告第2節にまとめた。旧固定コミットには含まれない。私的会話の原文や個人識別子は公開資料に含めない

## 評価履歴と考察の根拠

最終報告第9節のD1〜D4の点数、要求モデル・推論設定、ゲート、D4のレビュー手順は、2026年10月1日の保存済み最終レポートに基づく。その記録では53、72、69、78点で、実ランタイムモデルID・適用推論設定は未確認。D4レビュー担当には前試行の点数・モデル名・比較を渡していない一方、設計の改訂には過去レビューと指示が使われている。全履歴をこのパッケージへ複製したものではない。

80点以上、全11項目3以上、指定6項目4以上という数値条件に加え、必須ゲートと未解決P0の受入条件を満たす必要があるという履歴を保持する。D4の採点説明の一部は、机上評価に禁止された実測を必須としないよう補正されたが、原rubric、設計、78点という判定は変更されていない。

第9節の改善の解釈、将来モデルへの期待、次回の比較方法は、以上の履歴と本報告の未解決条件に基づく考察・仮説・提案である。新しい実験結果、将来モデルの性能測定、発売時期の予測ではない。10月2日の追加条件を含む現在の報告は未採点であり、過去の78/100・HOLDを更新しない。

英語版は本パッケージの日本語版の対応訳であり、別の評価や価格調査を実施したものではない。言語間で結論、数値、留保、出典を一致させ、歴史的な全リポジトリの英訳は対象外とする。

## 価格資料

### AWS

公開Price Listの日本リージョンJSONを読み取り。認証情報・クラウド資源APIは使用していない。

| 出典 | 確認対象 |
|---|---|
| [ECS東京](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonECS/current/ap-northeast-1/index.json) | Fargate Linux/x86 CPUとmemory |
| [ECS大阪](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonECS/current/ap-northeast-3/index.json) | 同上 |
| [RDS東京](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/current/ap-northeast-1/index.json) | PostgreSQL db.t4g.medium、Single-AZ/Multi-AZ |
| [RDS大阪](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/current/ap-northeast-3/index.json) | 同上 |
| [Fargate料金説明](https://aws.amazon.com/fargate/pricing/) | 課金方式・追加費用の確認先 |

ECS catalog publicationDateは2026-09-11T12:44:25Z、確認したOnDemand term effectiveDateは2026-07-01。RDS catalog publicationDateは2026-10-01T06:02:30Z。価格はUSD。地域、engine、instanceType、deploymentOption、OnDemandを照合した。

### Azure

[公式Retail Prices API](https://prices.azure.com/api/retail/prices)を読み取り。地域別のserviceName/armRegionName、productName/skuName、Consumptionを照合。公開価格の読取であり、Azure契約環境・資源にはアクセスしていない。

- Container Apps：serviceName `Azure Container Apps`、region `japaneast` / `japanwest`。Standard vCPU Active Usage、Standard Memory Active Usage、Standard Requests
- DB：serviceName `Azure Database for PostgreSQL`、region `japaneast` / `japanwest`、product `Azure Database for PostgreSQL Flexible Server General Purpose Ddsv5 Series Compute`、sku `2 vCore`、armSkuName `Standard_D2ds_v5`
- 東DB meterId `b8337cf5-8521-5ef8-9345-c2bd0546a51d`、西DB `8cd5400c-3a11-5332-83d7-34d08216b778`、effectiveStartDate 2023-03-01、unit `1 Hour`
- 東Container Apps CPU meter `4ef945a7-c73f-5825-9fe9-117d65d7b4a5`、memory `5b8ebac4-2c47-523d-8559-a1e51867ad3c`、requests `31e4637c-3cd6-5207-a4fb-622bdc64b639`
- 西Container Apps CPU meter `57e22c85-06db-5efb-9a47-1575d0287389`、memory `55f298d4-0e5b-5cf4-b469-0d3345cb0cd4`、requests `d6ad3660-587a-5956-a0db-4d91fe9bd727`

[Container Apps価格説明](https://azure.microsoft.com/ja-jp/pricing/details/container-apps/)では地域単価が空欄になる取得経路があったため、数値は上記公開APIで確認した。価格表の別製品、無料meter、reservationを混用していない。

### GCP

- [Cloud Run料金](https://cloud.google.com/run/pricing)：東京・大阪がTier1であることとinstance-based CPU/memory単価を確認
- [Cloud SQL料金](https://cloud.google.com/sql/pricing)：今回の現行日本DB価格取得は失敗。取得できない数値を第三者記事や古い記録から補完していない

## 製品仕様

| 論点 | 一次資料 |
|---|---|
| RDS PITR | [Automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html) |
| RDS保持上限 | [Backup retention](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.BackupRetention.html) |
| RDS地域間replica | [Cross-region replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.XRgn.html) |
| AWS長期snapshot | [AWS BackupとRDS](https://aws.amazon.com/getting-started/hands-on/amazon-rds-backup-restore-using-aws-backup/) |
| Aurora自動backup | [Aurora backups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html) |
| Aurora Global Database切替 | [Failover](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html) |
| Azure昇格は非自動 | [Promote replicas](https://learn.microsoft.com/en-us/azure/postgresql/read-replica/concepts-read-replicas-promote) |
| Azure backup・PITR | [Backup and restore](https://learn.microsoft.com/en-us/azure/postgresql/backup-restore/concepts-backup-restore) |
| Azure HAと料金 | [Reliability](https://learn.microsoft.com/azure/reliability/reliability-postgresql-flexible-server) |
| Cloud SQL editionとPITR | [Editions](https://docs.cloud.google.com/sql/docs/postgres/editions-intro) |
| Cloud SQL Advanced DR | [Advanced DR](https://docs.cloud.google.com/sql/docs/postgres/use-advanced-disaster-recovery) |
| Cloud SQL長期backup | [Backup overview](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups) |
| Firebase認証のデータと削除 | [Privacy](https://firebase.google.com/support/privacy) |
| Entra日本保存・例外 | [Data residency](https://learn.microsoft.com/en-us/entra/fundamentals/data-residency) |
| Cognito MRRと制約 | [Multi-Region replication](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-multi-region.html) |

## 証拠の限界

確認できたのは公開仕様・公開部品価格・シナリオ入力・計算の整合性である。契約の適用、国内保存の実設定、SKUの実際の供給、全依存を含む地域間復旧、性能、全コピー削除、月次SLO、実請求は未検証。

遅れて発見した論理破損では巻戻しだけで正常更新を救えないこと、削除30日とbackup90日から最終残存が概ね120日になり得ること、台帳自身のbackupが保持期間へ影響することは、明示した条件からの設計上の推論である。サービスの実測値や法的結論ではない。
