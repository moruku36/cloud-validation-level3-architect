# D5 継承改善報告 / D5 Inherited Improvement Report

2026-10-02. **77/100 — numerical FAIL / adoption HOLD.**

|読む順番 / Reading order|日本語|English|
|---|---|---|
|結果・根拠・未回答 / Results, grounds, unanswered matters|[最終報告](FINAL-REPORT.ja.md)|[Final report](FINAL-REPORT.en.md)|
|D4・別途報告73との比較の限界 / Limits of comparison with D4 and separately reported 73|[考察](DISCUSSION.ja.md)|[Discussion](DISCUSSION.en.md)|

要求設定は設計GPT-6.1 Sol High、独立レビューGPT-6.1 Sol Medium。実際に確認できたモデル・推論設定はUNKNOWNです。単一継承改善、凍結後レビュー・採点1回。Cost/Complexity3、G3/G4 HOLDを保持します。原評価・原保存ファイルを変更せず、公開用の編集・英訳・索引追加だけを行いました。

Requested configurations: designer GPT-6.1 Sol High; independent reviewer GPT-6.1 Sol Medium. Actual model/reasoning settings are UNKNOWN. One inherited revision, one post-freeze review/scoring pass. Cost/Complexity3 and G3/G4 HOLD are retained. This publication adds editorial adaptation, translation, and navigation without modifying original assessments or saved files.

旧入力は `73ac52670aa4c8848b6f565236dd6094377c5613`。新公開出典と新規独立評価者の影響は固定できず、公平なモデル比較ではありません。[追加条件の既存最終報告](../2026-10-02-final/README.md)は別の未採点資料として保持します。別途報告された全新規73点はD5入力・本公開の再採点対象ではなく、元凍結パケットは未収録です。

Earlier input commit: `73ac52670aa4c8848b6f565236dd6094377c5613`. New public evidence and a fresh independent reviewer are uncontrolled confounds; this is not a fair model comparison. The [existing final report on additional conditions](../2026-10-02-final/README.md) remains a separate unscored record. The separately reported clean-sheet 73 was not a D5 input or rescoring target; its frozen packet is not included here.

## 証拠 / Evidence

Evidence files retain their original language. The two reports and discussions are full corresponding bilingual documents, not separate assessments. / 証拠ファイルは原言語を保持し、報告・考察は全文対応の日英文書です。

|対象 / Subject|公開証拠 / Public evidence|
|---|---|
|24要件・正式回答・不変rubric / Requirements, formal answers, unchanged rubric|[要件台帳](evidence/blind-review-design-D5/requirements-ledger.csv) · [原入力](evidence/blind-review-design-D5/source/) · [rubric](evidence/blind-review-design-D5/rubric.md)|
|AWS/Azure/GCP・責任/障害境界 / Three providers and boundaries|[選択肢](evidence/blind-review-design-D5/architecture-options.md) · [provider adapters](evidence/blind-review-design-D5/provider-adapters.md) · [trust boundaries](evidence/blind-review-design-D5/trust-boundaries.md)|
|費用・数量・未知・工数 / Cost, quantities, unknowns, effort|[費用条件](evidence/blind-review-design-D5/cost-configuration-D5.md) · [bill of quantities](evidence/blind-review-design-D5/conditional-bill-of-quantities.csv) · [missing quotes](evidence/blind-review-design-D5/quote-completeness.csv) · [labor](evidence/blind-review-design-D5/operations-accounting.md)|
|削除・復旧 / Deletion and recovery|[copy ledger](evidence/blind-review-design-D5/deletion-proof-ledger.csv) · [restore predicate](evidence/blind-review-design-D5/recovery-ledger-predicate.md) · [recovery scenarios](evidence/blind-review-design-D5/scenario-recovery-D5.csv)|
|35独立シナリオ・採点・gate / Independent scenarios, scoring, gates|[scenario audit](evidence/independent-review-D5/scenario-audit.csv) · [review](evidence/independent-review-D5/review.md) · [scores](evidence/independent-review-D5/scoring.csv) · [gates](evidence/independent-review-D5/gates.csv)|
|モデル設定・時計・採点前開示 / Model settings, clocks, pre-score disclosure|[run manifest](evidence/provenance/run-manifest-public.json) · [designer clocks](evidence/provenance/designer-clocks-reader.json) · [review clocks](evidence/independent-review-D5/clocks.json) · [disclosure](evidence/independent-review-D5/workflow-disclosure.md)|
|元D4の78点と旧条件 / Original D4 78 and earlier conditions|[D4 design](evidence/inherited/blind-review-design-D4/) · [D4 review](evidence/inherited/independent-review-D4/step5-score.md) · [score-preserving clarification](evidence/inherited/independent-review-D4/step5-clarification.md)|
|設計・出典差分 / Design and source changes|[design changes](evidence/d4-to-d5-change-table.csv) · [source changes](evidence/changed-public-evidence-ledger.csv) · [original full-read inventory](evidence/complete-original-read-inventory.csv)|
|公開範囲・原本対応・ハッシュ / Publication scope, provenance, hashes|[publication manifest](PUBLICATION-MANIFEST.json) · [SHA256SUMS](SHA256SUMS) · [original D5 freeze manifest](evidence/blind-review-design-D5/SHA256SUMS.json)|

公開ファイル156件は元読者向けパケットからバイト同一で保持しています（D5凍結85件、独立レビュー14件、元D4入力51件、差分等4件、追加の入力ハッシュ・時計2件）。元レビューの成果物manifestはローカル運用パスを含むため公開せず、本公開manifestを使います。原180ファイルZIP・内部運用記録・保存ログ・内部skill指示・アカウント/session識別子は公開しません。原凍結ファイル内の「非公開」「公開していない」等は採点時点の履歴であり、現在の公開状態を指しません。

156 public files are byte-identical copies from the reader packet: 85 D5 freeze files, 14 independent-review files, 51 original D4 input files, four change/verification records, and two input-hash/clock records. The original review artifact manifest contains a local operational path and is excluded; use this publication's manifest. Complete private archives, internal operational records, upload logs, internal skill instructions, and account/session identifiers are excluded. Statements such as “private” or “no publication” inside frozen files describe their historical scoring-time state, not their current publication status.

原要件・rubric内の古い相対リンクは原文保全のため変更していません。[歴史的リンク対応表](HISTORICAL-LINK-MAP.json)から固定入力コミットの公開ファイルへ移動できます。原入力が伏せたリンクは復元せず、旧採点リンクをD5の採点根拠には使いません。

Older relative links inside original requirements/rubrics remain unchanged to preserve source bytes. The [historical link map](HISTORICAL-LINK-MAP.json) supplies destinations at the pinned public input commit. Deliberately redacted links remain redacted; historical score links are not used as D5 scoring evidence.

ハッシュ確認 / Hash verification:

```bash
cd docs/reports/2026-10-02-d5
sha256sum -c SHA256SUMS
```

この工程は文書公開のみ。机上結果は実測SLO・法令適合・請求実績・運用体制の証明ではなく、クラウド実行を承認しません。 / This stage only publishes documentation. Desk findings do not prove measured SLOs, legal compliance, actual bills, or staffing, and do not authorize cloud execution.
