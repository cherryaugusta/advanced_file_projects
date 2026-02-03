from pathlib import Path
from file_projects.personal.finances import parse_budget

def test_budget_parsing(tmp_path: Path):
    file = tmp_path / "budget.txt"
    file.write_text(
        "Salary: $3000\n"
        "Rent: $1200\n"
        "Groceries: $400\n",
        encoding="utf-8",
    )

    budget = parse_budget(file)
    assert budget.income == 3000
    assert budget.expenses == 1600
    assert budget.balance == 1400
