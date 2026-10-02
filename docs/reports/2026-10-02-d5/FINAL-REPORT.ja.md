# Level3 D5 単一継承改善試行 — 公開版最終レポート（2026-10-02）

[日本語](FINAL-REPORT.ja.md) | [English](FINAL-REPORT.en.md) | [索引](README.md)

これは読者向け編集版を基にした公開版です。設計・レビュー・採点を変更していません。原本と原180ファイルZIPは非公開で保全しています。公開証拠は必要なプロジェクト資料に限定し、保存手順や内部運用記録は含めていません。

独立机上採点は **77/100**。原基準の数値合格は **FAIL**、導入判断は **HOLD** です。**80以上も80点超も未達**です。設計改訂1回、匿名凍結後の独立レビュー・採点1回で終了しました。採点後の設計修正、再採点、追加試行、モデル・推論設定の切替は実施していません。

|条件|結果|
|---|---|
|総合80以上|FAIL：77|
|80点超（別報告）|未達：77|
|全11項目3以上|PASS：最低3|
|必須6項目4以上|FAIL：Cost 3、残る5項目4|
|未解決P0なし|未充足：導入に必要なOWNER/SOURCE ACCESS/UNAUTHORIZED LIVEが未解決。設計側P0は指摘なし|
|全6 hardgate PASS|未充足：G1/G2/G5/G6 PASS、G3/G4 HOLD|
|最終判断|数値基準FAIL、導入HOLD。未回答・未検証を合格扱いしない|

## 独立採点と根拠

|項目|配点|独立評価|得点|
|---|---:|---:|---:|
|Requirements|15|4|12|
|Architecture|15|4|12|
|Security/IAM|10|4|8|
|Availability|10|4|8|
|Scalability|5|4|4|
|Cost|10|3|6|
|Operations|10|4|8|
|Backup/DR|10|4|8|
|Observability|5|4|4|
|Complexity|5|3|3|
|Vendor lock-in/migration|5|4|4|
|合計|100||77|

採点者は設計者とは別担当です。自己採点はなく、人間採点欄は全て空欄です。元rubricと正式補足の1〜5定義・配点・合格条件を変更していません。A/Bは設計根拠と検証計画を評価し、Cの実測要件と分けています。未実測という理由だけで全項目を一律に上限設定していません。

詳細の項目別根拠は [scoring.csv](evidence/independent-review-D5/scoring.csv)、判定全文は [review.md](evidence/independent-review-D5/review.md)、gate根拠は [gates.csv](evidence/independent-review-D5/gates.csv) にあります。相対リンクはこの公開ディレクトリを基準に確認してください。

## 残る設計不足

独立レビューのP1は、(D01)全主要要求経路に追加したSQL-backed AdmissionCoordinatorの操作回数・処理量・SQL競合・遅延配分・障害回復順序、(D02)独自の受付/epoch/fence/broker/adapter/journal実装に対する初期40〜80時間・リハーサル16〜32時間の作業別根拠、(D03)予算成立性と必須残余費用の余裕・低コスト制御代替案、(D04)論理破損後の正常書込み救済journalのpayload・独立保護・完全性・再適用順序です。

P2は(D05)監視系列数の合計が2522ではなく2422、3000上限に対する余裕が478ではなく578という保守的な100系列の差、(D06)S21 retry/S25レビュー頻度の旧CSV表現と支配文書の一致、現在の直接参照先の補強です。いずれも凍結案を修正せず [step4-findings.md](evidence/independent-review-D5/step4-findings.md) に残しました。

Cost 3は価格取得失敗をモデル能力不足とした判定ではありません。未知を正直に分離した点は評価されましたが、税を含めた比較可能な全費用・条件付き成立性・代替案の具体性が不足しています。既知のGCP compute部分はP2/dev176で387.4464 USD、P4/dev730で630.72 USD。凍結した参考FX156.9969による計算では60,827.88/99,021.08円で、必須の他メーターと税を含みません。請求FX・税・完全総額はUで、請求実績や保証下限ではありません。[費用条件](evidence/blind-review-design-D5/cost-configuration-D5.md)、[数量表](evidence/blind-review-design-D5/conditional-bill-of-quantities.csv)、[不足単価](evidence/blind-review-design-D5/quote-completeness.csv)、[公開Cloud Run料金](https://cloud.google.com/run/pricing) を参照してください。

Complexity 3は追加した独自制御系の性能・失敗境界・実装工数の根拠不足です。主要のmanaged app/HA SQL/object/outbox構成、IAM/削除/復旧計画は概ね妥当と評価されましたが、導入可能との認定ではありません。

## 未回答・hardgate

G3は全10データ/コピー種別の台帳・restore publication predicateがある一方、削除開始事象、最小リンク情報の保持・保管責任、外部/受信者コピー責任が未承認です。G4は役割別工数と無人時の停止条件がある一方、主担当/代替担当の実名、承認時間、不在時対応、無人復旧権限が未確定です。

元の7質問をそのまま [questions-only.md](evidence/blind-review-design-D5/questions-only.md) に保持しました。既に確定した日本本番/backup、30日削除、最長35日backup、99.9%対象、30分/5分の測定時計、平日日中、税を含む本番＋最小dev10万円、別枠の労務/ドメイン/有償有人supportは再質問していません。

未回答は追加の国内保存/移転境界、削除完了/台帳のlinkage・retention・受信者コピー、論理損失/公開/region DR権限と追加依存の回復目標、担当/承認工数/不在時対応、稼働時間・burst頻度・最小dev・invoice FX/tax・余裕、成長MAU/DAU/予算/過負荷対応、mail/PITR選択です。正確なJapan SKU/機能/quota/権限/price、PITR watermark interfaceはSOURCE ACCESS、適用IAM・性能・failover・削除/restore・月間SLO・移行/cleanup実証はUNAUTHORIZED LIVEとして分離しました。

## 入力保全・試行差分・モデル記録

固定入力コミットは73ac52670aa4c8848b6f565236dd6094377c5613（元2026-10-01読取確認のmain）。D5で最新mainに置き換えていません。元D4の設計34ファイルと独立レビュー16ファイルを編集前に全文読解し、原文/回答/正式補足/rubricとREQ-01〜24の固定欄を保持しました。

元D4の数値78から今回77へ-1です。Cost 3は継続、Complexity 4→3、他9項目は4のままです。新しい公開資料、独立評価者、追加した制御系、実行設定の確認限界があるため、モデル優劣の因果比較や公平な全新規比較ではありません。[12論点の設計差分](evidence/d4-to-d5-change-table.csv) と [出典差分56記録](evidence/changed-public-evidence-ledger.csv) を保存しました。

|担当|要求設定|実際に独立確認できた設定|
|---|---|---|
|設計|GPT-6.1 Sol High|モデル名/推論設定UNKNOWN。要求受理はbackend証明ではない|
|新規独立レビュー|GPT-6.1 Sol Medium|モデル名/推論設定/backend/seed UNKNOWN|

設計者は指示に従い元レビューの数値・所見を読んでおり、改善のアンカーとなり得ます。新規レビュー担当には設計者名/モデル、過去点数、希望点数を渡していません。匿名凍結案内の点数を含まない履歴を読み取り範囲に含むこと、重複内容の再構成だけでなく全84ファイルを直接全文読むことを採点前に明確化し、完了しました。モデル・入力・設計・時計は変更していません。

公開出典は設計側27新規記録（18取得、4部分取得、5失敗）と29の保持記録です。新Azure URLの取得などは追加証拠の交絡として明記しました。レビュー側は公式15URLを新規確認（12取得、2地域価格部分取得、1Cloud SQL料金ページの取得失敗）。他の必須単価/権限/所在地ページは新規再確認しておらず、凍結した証拠を保持しています。過去と同一の出典アクセス条件や実際のモデル・推論設定は再現証明できません。[採点前開示](evidence/independent-review-D5/workflow-disclosure.md) と [独立出典台帳](evidence/independent-review-D5/source-access.csv) に採点前の状態を記録しています。

## 時間と切断通知

|工程|観測UTC|時間|固定上限|
|---|---|---:|---:|
|共通準備（親の開始〜Step1開始）|11:29:35〜11:34:26|4m51s（設計担当3m33s）|240min|
|Step1|11:34:26〜11:37:02|2m36s|90min|
|Step2|11:37:02〜11:54:21|17m19s|180min|
|Step3/凍結|11:54:21〜12:06:02|11m41s|120min|
|Step4|12:08:17〜12:25:18|17m01s|120min|
|Step5|12:25:41〜12:30:23|4m42s|90min|

凍結検証/引継ぎ2m15sとStep4→5移行23秒は別に記録しています。core全体60m48s、回答待ち0、timeout/時計リセット/無断延長0です。最終包装・Library保存はcore採点終了後の受領記録で扱います。

実行環境の切断通知後、12:29:22 UTCに実際のファイル読取/コマンド実行と84ハッシュの一致を確認し、評価担当もツール継続を確認しました。reviewerの環境操作失敗は0で、設計・レビューを再始動せず完了しました。許可受理だけを完了証拠にしていません。

## 成果物と証拠

D5凍結案は84内容ファイル、771857 bytes、manifestを含め85ファイルです。全84を独立担当が直接全文読み、35シナリオを独立批判レビューしました。before/afterと親の最終検証で変更0を確認しました。

- D5 manifest SHA256：3d3b4bb79305606902762ae91f150beba2d33f30e607196366f62e9b6db94072
- 不変rubric SHA256：7a3eb2157ec4fe897c5bd667fb409e70c2c98b73ca423d904e8d76c651b09987
- 元D4 manifest SHA256：9572c63a74407d6bcc19aa8a96ba374111def6db22a51b0cb57cc4f313fbd29f
- 元ZIP SHA256：385ae1504844485e889c26792bd336531675a62332c60a252c2ba01c27e98f03（424630 bytes、154 files）

元D4、原レポート、原180ファイルZIPと既存の非公開バックアップは変更していません。この公開版は原180ファイルZIPと同一ではありません。公開証拠のバイト列と原本との対応は [PUBLICATION-MANIFEST.json](PUBLICATION-MANIFEST.json)、公開ファイルのハッシュは [SHA256SUMS](SHA256SUMS) に記録しています。

[成果物索引](README.md) と [公開run manifest](evidence/provenance/run-manifest-public.json) を入口にしてください。費用表では単価・数量・FX・税・除外・確度を記録し、operations-accounting.mdで役割別人件工数を分離しています。全設計・復旧・削除・移行検証は机上の計画です。実測SLO、法令適合、請求実績、実際の運用体制の証明ではありません。D5採点終了までクラウドaccount/credentials/SDK/CLI/API、Terraform、資源の作成変更削除、実障害/負荷試験、GitHub書込/公開、有償外部実行は行っていません。

## 公開版と考察

本公開工程だけにGitHubの文書追加・PR・マージが承認されています。クラウド実行の承認にはなりません。日英報告は同じ結果と留保を伝える対応文書であり、別の採点ではありません。[考察](DISCUSSION.ja.md) は旧D4 78点と別途報告された全新規73点を区別し、D5の改善経路、制御系追加の負担、比較の限界を扱います。既存の [追加条件に関する最終報告](../2026-10-02-final/README.md) は変更していません。D5にはその追加条件を取り込んでおらず、D5の77点を追加条件の点数へ転用しません。
