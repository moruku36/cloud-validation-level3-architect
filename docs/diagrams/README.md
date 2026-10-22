# Diagrams / 図

Mermaid sources (`*.mmd`) and the SVGs rendered from them with [Pele](https://pele.run/) (MIT license, CSS-variable theming). The SVGs use Pele's default light palette.
図はMermaidで記述（`*.mmd`）し、[Pele](https://pele.run/)でSVGに変換したものです。SVGはPeleの既定のライトテーマです。

| Diagram | Source / SVG | Used in |
|---|---|---|
| Evaluation flow / 評価の流れ | `evaluation-flow.{en,ja}` | README |
| Opus 5.5 pilot flow / pilotの流れ | `pilot-comparison.{en,ja}` | README |
| Architecture proposed in the frozen pilot answer (GCP) / 凍結答案の提案構成 | `gcp-architecture.{en,ja}` | README. A desk design under assessment, not adopted or deployed. 評価対象の机上設計で、採用・構築はされていない |
| Requirements decomposition / 要件の分解 | `requirements-tree.ja` | [requirements](../requirements.md) |

The architecture diagram is a simplified view of section 3.1 of the [frozen answer](../../experiments/opus55-pilot/2026-10-21-high/frozen-answer/design-02.md); it omits CI/CD, logging, secrets, and the external monitor. The original is preserved and unchanged.
アーキテクチャ図は[凍結答案](../../experiments/opus55-pilot/2026-10-21-high/frozen-answer/design-02.md)3.1節の簡略版で、CI/CD・ログ・秘密情報・外部監視は省略しています。原本は変更していません。

## Regenerate / 再生成

```js
import { render } from 'pele';   // npm install pele
import { readFileSync, writeFileSync } from 'node:fs';
const name = 'evaluation-flow.en';
writeFileSync(`${name}.svg`, render(readFileSync(`${name}.mmd`, 'utf8')).svg);
```

Edit the `.mmd`, regenerate the matching `.svg`, and commit both. / `.mmd`を編集したら対応する`.svg`も再生成して一緒にコミットします。
