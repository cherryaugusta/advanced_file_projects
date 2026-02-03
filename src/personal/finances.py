from dataclasses import dataclass
from pathlib import Path
from file_projects.common.io import read_lines

INCOME_KEYS = {"Salary", "Freelance"}
EXPENSE_KEYS = {"Rent", "Utilities", "Groceries", "Entertainment", "Savings"}

@dataclass(frozen=True)
class Budget:
    income: int
    expenses: int

    @property
    def balance(self) -> int:
        return self.income - self.expenses

def parse_budget(path: Path) -> Budget:
    income = 0
    expenses = 0

    for line in read_lines(path):
        if "$" not in line:
            continue

        try:
            amount = int(line.split("$", 1)[1])
        except ValueError:
            continue

        if any(key in line for key in INCOME_KEYS):
            income += amount
        elif any(key in line for key in EXPENSE_KEYS):
            expenses += amount

    return Budget(income=income, expenses=expenses)
