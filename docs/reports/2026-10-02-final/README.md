# Level3 クラウド設計思考実験 最終まとめ

# Level3 Cloud Architecture Thought Experiment Final Summary

2026年10月2日（日本時間）版。 / Edition of 2 October 2026, Japan time.

[日本語](#日本語) | [English](#english)

## 日本語

**結論：思考実験としての調査・比較・報告をここで完了する。実サービスの採用、予算適合、復旧性能の受入は未確定であり、本番導入を承認するものではない。**

個人情報の国内保存、東西リージョンの自動復旧、90日バックアップ等の追加条件を反映した。3社の構成候補と価格を比較したが、認証・復旧制御の適合証拠と全込み見積が揃わないため、クラウドの勝者は選定していない。過去のD4評価78/100・HOLDは旧条件の履歴として保持し、新条件の点数には転用しない。

最終報告第9節に、53→72→69→78という4つの要求設定の履歴と考察を追加した。初回から25点改善したが、単調改善でもモデル能力だけの比較でもない。実ランタイムモデルと適用設定は未確認。将来のより強いモデルが合格へ近づく可能性は、外部証拠と同条件での再検証が必要な仮説として扱い、時期や合格を保証しない。合格には80点以上だけでなく必須ゲート等も必要である。

### 読む順番

1. [最終報告](FINAL-REPORT.ja.md)：結論、確定条件、3社比較、復旧・削除・運用の限界、実証が必要な項目、結果の考察と将来の可能性
2. [価格モデル](COST-MODEL.ja.md)：同一条件で比較できる範囲、条件付き部分計算、未価格項目、算定式
3. [出典と証拠](EVIDENCE.ja.md)：原要件の固定版、評価履歴、公式資料、価格確認方法、未取得情報

### 範囲

公開資料・既存成果物に基づく机上検討のみ。今回、クラウド資源の作成、課金、実負荷試験、障害注入、実データ削除、実フェイルオーバーは行っていない。公開されているコードや手順があっても、本報告はその実行や実測成功を意味しない。

本資料の元入力はコミット `73ac52670aa4c8848b6f565236dd6094377c5613`。出典リンクは改名後のリポジトリを指す。リンク先の履歴と、2026年10月2日に追加された設計条件は区別して読む。

英語版は下記3文書の全文対応訳であり、要約のみではない。日本語版を保持し、両言語の結論・数値・留保・出典を一致させた。歴史的な全リポジトリの翻訳は対象外。英訳と考察の追加による新しい採点・実験は行っていない。

## English

**Conclusion: The research, comparison, and reporting for this thought experiment are complete. Adoption for a live service, budget compliance, and acceptance of recovery performance remain unresolved; this report does not authorize production deployment.**

The report incorporates additional conditions including domestic storage of personal data, automated recovery between eastern and western Japanese regions, and 90-day backups. Architecture candidates and prices from three providers were compared, but no winner was selected because evidence of suitable authentication and recovery controls and complete all-inclusive estimates remain missing. The historical D4 assessment of 78/100 and HOLD is retained as a result under the earlier conditions, not reused as a score for the new conditions.

Section 9 of the final report adds the history and interpretation of four requested configurations, with scores of 53 → 72 → 69 → 78. The final score improved by 25 points from the first, but the improvement was neither monotonic nor an isolated comparison of model ability. Actual runtime models and applied settings were unverified. The possibility of stronger future models moving toward a pass is treated as a hypothesis requiring external evidence and retesting under the same conditions, with no guarantee of timing or success. Passing requires mandatory gates and other conditions as well as a score of at least 80.

### Reading Order

1. [Final report](FINAL-REPORT.en.md): conclusion, confirmed conditions, three-provider comparison, recovery/deletion/operations limits, required demonstrations, interpretation, and future possibilities
2. [Cost model](COST-MODEL.en.md): what can be compared under matching conditions, conditional partial calculations, unpriced items, and formulas
3. [Sources and evidence](EVIDENCE.en.md): pinned original requirements, assessment history, official documentation, price-verification methods, and missing information

### Scope

This is a desk study based on public material and existing deliverables only. No cloud resources were created, charges incurred, live load tests run, faults injected, real data deleted, or real failovers executed in this work. The existence of published code or procedures does not mean that this report executed them or demonstrated their success through measurement.

The original input for this material is commit `73ac52670aa4c8848b6f565236dd6094377c5613`. Source links point to the renamed repository. Distinguish the linked historical records from the design conditions added on 2 October 2026.

The English editions are full counterparts of the three documents below, not summaries. The Japanese editions are preserved, with conclusions, numbers, caveats, and sources aligned across languages. Translation of the entire historical repository is outside scope. Adding the translation and discussion does not constitute new scoring or experimentation.

## 日英対応文書 Language Counterparts

| 日本語 | English |
|---|---|
| [最終報告](FINAL-REPORT.ja.md) | [Final report](FINAL-REPORT.en.md) |
| [価格モデル](COST-MODEL.ja.md) | [Cost model](COST-MODEL.en.md) |
| [出典と証拠](EVIDENCE.ja.md) | [Sources and evidence](EVIDENCE.en.md) |

[SHA256SUMS](SHA256SUMS)：本案内と6文書の内容照合用。採点・測定の証拠ではない。 / Content checksums for this guide and the six documents, not evidence of scoring or measurement.
