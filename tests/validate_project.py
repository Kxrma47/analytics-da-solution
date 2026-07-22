from __future__ import annotations

import ast
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "README.txt",
    "analytics_assignment/__init__.py",
    "analytics_assignment/python_tasks.py",
    "analytics_assignment/calculations.py",
    "analytics_assignment/report.py",
    "solutions/final_answers.txt",
    "solutions/block_1_probability_and_logic.txt",
    "solutions/block_2_python_complexity.txt",
    "solutions/block_3_sql.txt",
    "solutions/block_4_statistics_ab_tests.txt",
    "solutions/block_5_ml_base.txt",
    "sql/examination_rank.sql",
    "sql/purchases_under_5000.sql",
    "tests/test_python_tasks.py",
    "tests/validate_project.py",
]


TEXT_SUFFIXES = {".txt", ".sql", ".py"}


def main() -> int:
    check_required_files()
    check_removed_previous_task_files()
    check_answers()
    check_sql()
    check_clean_text()
    check_code_style()
    print("Checked required files: 15")
    print("Checked assignment answers and calculations.")
    print("Checked SQL files.")
    print("Checked clean wording and code style.")
    print("All project checks passed.")
    return 0


def check_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail("Missing files: " + ", ".join(missing))
    if (ROOT / "README.md").exists():
        fail("README.md must not be present.")


def check_removed_previous_task_files() -> None:
    obsolete_paths = [
        ROOT / "task_1_bpmn",
        ROOT / "task_2_marketplace_publication",
        ROOT / "task_3_registration_api",
    ]
    for path in obsolete_paths:
        if path.exists() and any(path.rglob("*")):
            fail(f"Obsolete folder is not empty: {path.name}.")


def check_answers() -> None:
    final_answers = (ROOT / "solutions/final_answers.txt").read_text(encoding="utf-8")
    required_tokens = [
        "3,99",
        "26,8",
        "63,2; 93,3",
        "минимально 30 и максимально 600 строк",
        "Верные утверждения: 2, 3 и 4",
        "0,75",
        "-0,85",
    ]
    for token in required_tokens:
        if token not in final_answers:
            fail(f"Answer token is missing: {token}.")


def check_sql() -> None:
    rank_sql = (ROOT / "sql/examination_rank.sql").read_text(encoding="utf-8").lower()
    purchases_sql = (ROOT / "sql/purchases_under_5000.sql").read_text(encoding="utf-8").lower()
    if "rank() over" not in rank_sql:
        fail("Rating query must use rank().")
    if "select" in purchases_sql[purchases_sql.find("from") + 4:]:
        fail("Purchases query must not use subqueries.")
    if " over " in purchases_sql:
        fail("Purchases query must not use window functions.")
    for token in ["left join", "group by", "having", "coalesce", "5000"]:
        if token not in purchases_sql:
            fail(f"Purchases query does not contain {token}.")


def check_clean_text() -> None:
    forbidden_patterns = [
        r"\b" + "chat" + "gpt" + r"\b",
        r"\b" + "open" + "a" + "i" + r"\b",
        r"\b" + "l" + "l" + "m" + r"\b",
        r"\b" + "language " + "model" + r"\b",
        r"\b" + "artificial " + "intelligence" + r"\b",
        r"\b" + "a" + "i" + r"[- ]?" + "gen" + "erated" + r"\b",
        r"\b" + "machine" + r"[- ]?" + "gen" + "erated" + r"\b",
        r"\b" + "gen" + "erated" + " by" + r"\b",
        r"\b" + "auto" + r"[- ]?" + "gen" + "erated" + r"\b",
        r"\b" + "place" + "holder" + r"\b",
        r"\b" + "lo" + "rem" + r"\b",
        r"\b" + "to" + "do" + r"\b",
        r"\b" + "fix" + "me" + r"\b",
        "искус" + r"ственн\w*\s+" + "интел" + r"лект\w*",
        "нейро" + r"сет\w*",
        "нейро" + r"нн\w*",
        "сгенер" + r"ирован\w*",
        "создано " + "автоматически",
        "автоматически " + r"создан\w*",
        "языков" + r"\w+\s+" + "модель" + r"\w*",
        "чат" + "гпт",
        "опен" + "аи",
        "за" + r"глушк\w*",
        "примерн" + r"\w+\s+" + "текст" + r"\w*",
        "чернов" + r"\w+\s+" + "текст" + r"\w*",
        "до" + "работать",
        "исправить " + "потом",
    ]
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix in TEXT_SUFFIXES:
            text = path.read_text(encoding="utf-8").lower()
            for pattern in forbidden_patterns:
                if re.search(pattern, text):
                    fail(f"Clean wording check failed in {path.relative_to(ROOT)}.")


def check_code_style() -> None:
    for path in list((ROOT / "analytics_assignment").glob("*.py")) + list((ROOT / "tests").glob("*.py")):
        source = path.read_text(encoding="utf-8")
        for line in source.splitlines():
            stripped = line.lstrip()
            if stripped.startswith("#"):
                fail(f"Code comment found in {path.relative_to(ROOT)}.")
        tree = ast.parse(source)
        if ast.get_docstring(tree):
            fail(f"Module docstring found in {path.relative_to(ROOT)}.")
        for node in ast.walk(tree):
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and ast.get_docstring(node):
                fail(f"Docstring found in {path.relative_to(ROOT)}.")
    for path in (ROOT / "sql").glob("*.sql"):
        text = path.read_text(encoding="utf-8")
        if "-" + "-" in text or "/" + "*" in text or "*" + "/" in text:
            fail(f"SQL comment found in {path.relative_to(ROOT)}.")


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


if __name__ == "__main__":
    raise SystemExit(main())
