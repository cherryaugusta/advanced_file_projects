from file_projects.common.paths import personal
from file_projects.personal.finances import parse_budget

def main() -> None:
    budget_file = personal("finances") / "budget.txt"
    budget = parse_budget(budget_file)

    print(f"Income: ${budget.income}")
    print(f"Expenses: ${budget.expenses}")
    print(f"Balance: ${budget.balance}")

if __name__ == "__main__":
    main()
