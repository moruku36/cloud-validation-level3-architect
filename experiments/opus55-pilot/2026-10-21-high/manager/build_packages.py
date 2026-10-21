"""Build the designer input package and the evaluator package for the Opus 5.5 High pilot.

Run from the repository root: python -I experiments/opus55-pilot/2026-10-21-high/manager/build_packages.py
Extraction is section/row based only; retained text is copied verbatim.
"""
import csv
import hashlib
import io
import json
import pathlib
import re

ROOT = pathlib.Path.cwd()
EXP = ROOT / "experiments/opus55-pilot/2026-10-21-high"
BA = ROOT / "docs/sources/business-answers-2026-09-08.md"
SUP = ROOT / "docs/sources/supplement-2026-09-08.md"
REQ = ROOT / "docs/requirements.md"
RUBRIC = ROOT / "evaluation/rubric.md"
GATES = ROOT / "docs/reports/2026-10-02-d5/evidence/blind-review-design-D5/review-gates.csv"


def sha(b):
    return hashlib.sha256(b).hexdigest()


def sections(text):
    """Split markdown into (heading, block) by '## ' headings; preamble has heading None."""
    out, head, buf = [], None, []
    for line in text.splitlines(keepends=True):
        if line.startswith("## "):
            out.append((head, "".join(buf)))
            head, buf = line.strip(), [line]
        else:
            buf.append(line)
    out.append((head, "".join(buf)))
    return out


def keep_sections(text, drop):
    kept, dropped = [], []
    for head, block in sections(text):
        (dropped if head in drop else kept).append((head, block))
    return "".join(b for _, b in kept), [h for h, _ in dropped]


def req_table(text):
    lines = text.splitlines(keepends=True)
    start = next(i for i, l in enumerate(lines) if l.startswith("|要件ID|"))
    end = start
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    rows = lines[start:end]
    assert len(rows) == 26, len(rows)  # header + separator + REQ-01..24
    return "".join(rows)


ba = BA.read_text(encoding="utf-8")
sup = SUP.read_text(encoding="utf-8")
req = REQ.read_text(encoding="utf-8")

BA_DROP = {"## 今回の処理範囲"}
SUP_DROP = {"## 評価", "## 人間の介入", "## GitHub集約", "## 今回の範囲"}
ba_kept, ba_dropped = keep_sections(ba, BA_DROP)
sup_kept, sup_dropped = keep_sections(sup, SUP_DROP)
table = req_table(req)

designer_inputs = (
    "# 入力1：正式業務回答（2026-09-08）\n\n" + ba_kept.split("\n", 1)[1].lstrip("\n")
    + "\n\n# 入力2：正式補足要件（2026-09-08）\n\n" + sup_kept.split("\n", 1)[1].lstrip("\n")
    + "\n\n# 入力3：要件一覧（REQ-01〜REQ-24）\n\n" + table
)

# Rubric for the evaluator: drop the sentence that links to historical A-3 scores.
rubric = RUBRIC.read_text(encoding="utf-8")
rubric_clean = re.sub(r"A-3の採点結果は\[初回・修正後\]\([^)]*\)に保存。", "", rubric)
rubric_clean = rubric_clean.replace("[補足要件](../docs/sources/supplement-2026-09-08.md)", "補足要件（入力2）")
assert "](" not in rubric_clean

# Gates: keep only gate_id and the unchanged criterion column.
gate_rows = list(csv.DictReader(io.StringIO(GATES.read_text(encoding="utf-8"))))
gbuf = io.StringIO()
w = csv.writer(gbuf, lineterminator="\n")
w.writerow(["gate_id", "criterion"])
for r in gate_rows:
    w.writerow([r["gate_id"], r["unchanged_criterion"]])
gates_clean = gbuf.getvalue()

pkg = EXP / "packages"
pkg.mkdir(parents=True, exist_ok=True)
files = {
    "designer/inputs.md": designer_inputs,
    "evaluator/source-business-answers-2026-09-08.md": ba,
    "evaluator/source-supplement-2026-09-08.md": sup,
    "evaluator/requirements-REQ01-24.md": "# 要件一覧（REQ-01〜REQ-24）\n\n" + table,
    "evaluator/rubric.md": rubric_clean,
    "evaluator/gates.csv": gates_clean,
}
verbatim = {
    "evaluator/source-business-answers-2026-09-08.md": BA,
    "evaluator/source-supplement-2026-09-08.md": SUP,
}
for rel, content in files.items():
    p = pkg / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    if rel in verbatim:
        p.write_bytes(verbatim[rel].read_bytes())  # byte-identical copy
    else:
        p.write_text(content, encoding="utf-8", newline="\n")

record = {
    "source_commit": "ef8b022372c46b9f589ca5d06b2c4b4dae435921",
    "sources_sha256": {str(p.relative_to(ROOT)).replace("\\", "/"): sha(p.read_bytes()) for p in (BA, SUP, REQ, RUBRIC, GATES)},
    "designer_package": {
        "business_answers_sections_dropped": ba_dropped,
        "supplement_sections_dropped": sup_dropped,
        "requirements_md": "only the REQ-01..REQ-24 table rows (header+separator+24) copied verbatim; preamble, mermaid diagram, notes and links dropped",
        "retained_text": "verbatim; only per-file title lines replaced by package headings; line endings normalized CRLF->LF",
    },
    "evaluator_package": {
        "sources": "business answers and supplement byte-identical copies (complete); REQ table rows verbatim",
        "rubric": "evaluation/rubric.md with the sentence linking to historical A-3 scores removed and the supplement link replaced by a package reference",
        "gates": "review-gates.csv columns gate_id + unchanged_criterion only; D5 design-plan, boundary and author_result columns dropped",
    },
    "package_sha256": {rel: sha((pkg / rel).read_bytes()) for rel in files},
}
(EXP / "manager/extraction-record.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(record["package_sha256"], indent=2))
