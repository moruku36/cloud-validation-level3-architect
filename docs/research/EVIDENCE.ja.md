# 証拠付録

日本語 | [English](EVIDENCE.en.md) · [README](../../README.ja.md) · [方法と結果](METHODS-RESULTS.ja.md)

本書は絞り込んだ索引であり、アーカイブの一覧ではない。固定したリポジトリ状態（コミット `0d67081cb994b69d10551df4346ab3757851ff2f`）の主要な記録へ案内する。参照先の凍結済み報告・証拠は変更していない。

## どの記録を使うか

|区分|意味|主な出典|
|---|---|---|
|最新の正式結果|D5の独立評価：77/100、不合格、保留|[D5報告](../reports/2026-10-02-d5/FINAL-REPORT.ja.md)、[gates](../reports/2026-10-02-d5/evidence/independent-review-D5/gates.csv)|
|履歴の付録|9月のA/B/C-1（自己評価）とD1〜D4|[A](../../experiments/A/final-report.md)、[B](../../experiments/B/final-report.md)、[C-1](../../evaluation/C-1-console-readonly-check-run.md)、[最終報告](../reports/2026-10-02-final/FINAL-REPORT.ja.md)|
|別途未採点|10/2に変更された要件。D5の入力ではない|[最終報告の要件節](../reports/2026-10-02-final/FINAL-REPORT.ja.md)|
|報告された文脈のみ|別の新規試行の73点|[考察](../reports/2026-10-02-d5/DISCUSSION.ja.md)|

## 主な主張と根拠

|主張|出典|備考|
|---|---|---|
|A：自己採点61→65（9/8〜9/9）|[A報告](../../experiments/A/final-report.md)、[採点](../../experiments/A/A-3/scores.md)|自己評価。人間欄は空欄|
|B：自己採点66、設計不合格（9/10）|[B報告](../../experiments/B/final-report.md)|AWSは参考優先のみ。相対点は合否ではない|
|C-1 未完了（9/13、4時間23分02秒）|[C-1記録](../../evaluation/C-1-console-readonly-check-run.md)|読取のみ。次工程の文言は履歴|
|D1〜D4の53/72/69/78と要求設定|[最終報告 第9節](../reports/2026-10-02-final/FINAL-REPORT.ja.md)|実行時の設定は未確認|
|D4は10/1実施（Step4開始 09:36:51Z）|[D4時刻](../reports/2026-10-02-d5/evidence/inherited/independent-review-D4/metadata-clocks.json)|D1〜D3の時刻は非公開|
|D5：77/100、項目別点、不合格・保留|[D5報告](../reports/2026-10-02-d5/FINAL-REPORT.ja.md)|項目別の根拠は[scoring.csv](../reports/2026-10-02-d5/evidence/independent-review-D5/scoring.csv)|
|D5ハードゲート：G1/G2/G5/G6 PASS、G3/G4 HOLD|[gates.csv](../reports/2026-10-02-d5/evidence/independent-review-D5/gates.csv)|机上の定義のみ|
|D5の指摘D01〜D06|[step4-findings.md](../reports/2026-10-02-d5/evidence/independent-review-D5/step4-findings.md)、[review.md](../reports/2026-10-02-d5/evidence/independent-review-D5/review.md)|凍結設計は修復していない|
|D5の費用条件と既知のGCP計算費|[費用条件](../reports/2026-10-02-d5/evidence/blind-review-design-D5/cost-configuration-D5.md)、[未取得単価](../reports/2026-10-02-d5/evidence/blind-review-design-D5/quote-completeness.csv)|請求額でも下限でもない|
|D4→D5の設計変更と交絡要因|[変更表](../reports/2026-10-02-d5/evidence/d4-to-d5-change-table.csv)、[採点前開示](../reports/2026-10-02-d5/evidence/independent-review-D5/workflow-disclosure.md)|因果的なモデル比較を妨げる|
|53→72→69→78→77の系列と73の除外|[考察](../reports/2026-10-02-d5/DISCUSSION.ja.md)|73は継承系列に含めない|
|将来の比較方法|[最終報告 第9節](../reports/2026-10-02-final/FINAL-REPORT.ja.md)、[証拠注記](../reports/2026-10-02-final/EVIDENCE.ja.md)|提案であり承認ではない|

## 範囲の欠落

- 索引は主要な出典を選んだもので、アーカイブ全体を再掲していない。D5の180ファイルの完全なアーカイブは非公開で保管されている。
- D1〜D3の個別の時刻は非公開で、不明として扱う。
- 別の73点は公開引継ぎ経由でのみ知られる。元のパケット、項目、ゲート、実行環境、時刻は非公開で、日付と構成は報告された文脈であり、検証済みの事実ではない。
- すべての設計者・レビュアーについて、実際の実行モデルと推論設定は不明であり、要求した名称は能力の証拠にならない。
- 9月の案内は9/17に編集された（[コミット](https://github.com/moruku36/cloud-validation-level3-architect/commit/44876806639ecaffb7e139cd9cd6985be58c79ef)）。D5公開のマージコミット時刻は10/3 01:17:44 JST = 10/2 16:17:44 UTCである（[PR26マージコミット](https://github.com/moruku36/cloud-validation-level3-architect/commit/0d67081cb994b69d10551df4346ab3757851ff2f)）。どちらも新たな実験実施日ではない。
- 机上結果は、実インフラの受入れ、SLO実測、削除完了、実際の請求額、法令適合を証明していない。過去報告にある次工程の文言は履歴であり、承認ではない。
- 研究概要を読んでからコードを確認する場合は、[過去のC-1ローカル検証ガイド](../../infra/c1/README.md)へ進む。オフライン試験はガードの検証であり、クラウド性能や実効IAMの証明ではない。
