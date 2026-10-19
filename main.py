
import json
import os
from datetime import date

DATA_FILE = "expenses.json"

DEFAULT_DATA = {
    "budget": 0.0,
    "expenses": []
}


def load_data(file_path=DATA_FILE):
    """Load saved budget and expenses from a JSON file."""
    if not os.path.exists(file_path):
        return {
            "budget": 0.0,
            "expenses": []
        }

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("Invalid data format.")

        if not isinstance(data.get("expenses", []), list):
            raise ValueError("Invalid expenses format.")

        return {
            "budget": float(data.get("budget", 0.0)),
            "expenses": data.get("expenses", [])
        }

    except (json.JSONDecodeError, ValueError, TypeError):
        print("Warning: Saved data could not be read.")
        print("Starting with an empty tracker.")
        return {
            "budget": 0.0,
            "expenses": []
        }


def save_data(data, file_path=DATA_FILE):
    """Save the current data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def add_expense(data, amount, category, description="",
                expense_date=None):
    """Validate and add one expense."""
    try:
        amount = float(amount)
    except (ValueError, TypeError):
        raise ValueError("Amount must be a valid number.")

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    category = category.strip()
    description = description.strip()

    if not category:
        raise ValueError("Category cannot be empty.")

    if expense_date is None:
        expense_date = date.today().isoformat()

    expense = {
        "amount": round(amount, 2),
        "category": category,
        "description": description,
        "date": expense_date
    }

    data["expenses"].append(expense)
    return expense


def set_budget(data, amount):
    """Set a non-negative budget."""
    try:
        amount = float(amount)
    except (ValueError, TypeError):
        raise ValueError("Budget must be a valid number.")

    if amount < 0:
        raise ValueError("Budget cannot be negative.")

    data["budget"] = round(amount, 2)


def get_total_expenses(data):
    """Calculate the total amount spent."""
    return round(
        sum(expense["amount"] for expense in data["expenses"]),
        2
    )


def get_category_totals(data):
    """Calculate spending totals for each category."""
    totals = {}

    for expense in data["expenses"]:
        category = expense["category"]
        totals[category] = (
            totals.get(category, 0) + expense["amount"]
        )

    return {
        category: round(amount, 2)
        for category, amount in totals.items()
    }


def get_remaining_budget(data):
    """Calculate the remaining budget."""
    return round(
        data["budget"] - get_total_expenses(data),
        2
    )


def read_positive_amount(prompt, allow_zero=False):
    """Read and validate a monetary amount from the user."""
    while True:
        try:
            amount = float(input(prompt))

            if amount < 0 or (amount == 0 and not allow_zero):
                print("Please enter a valid non-negative amount.")
                if not allow_zero:
                    print("The amount must be greater than zero.")
                continue

            return round(amount, 2)

        except ValueError:
            print("Invalid input. Please enter a number.")


def add_expense_menu(data):
    print("\n--- Add New Expense ---")

    amount = read_positive_amount("Amount: ")
    category = input("Category (Food, Transport, Study...): ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    description = input("Description (optional): ").strip()

    add_expense(data, amount, category, description)
    save_data(data)

    print("Expense added and saved successfully!")


def view_expenses(data):
    print("\n--- All Expenses ---")

    if not data["expenses"]:
        print("No expenses recorded yet.")
        return

    for index, expense in enumerate(data["expenses"], start=1):
        print(
            f"{index}. {expense['date']} | "
            f"{expense['category']} | "
            f"{expense['amount']:.2f} EGP"
        )

        if expense["description"]:
            print(f"   Description: {expense['description']}")

    print(f"\nTotal spent: {get_total_expenses(data):.2f} EGP")


def show_summary(data):
    total = get_total_expenses(data)
    budget = data["budget"]
    remaining = get_remaining_budget(data)

    print("\n--- Budget Summary ---")
    print(f"Budget:   {budget:.2f} EGP")
    print(f"Spent:    {total:.2f} EGP")
    print(f"Remaining: {remaining:.2f} EGP")

    if budget == 0:
        print("Set a budget to start tracking your spending.")
    elif remaining < 0:
        print(f"Warning: You exceeded your budget by {-remaining:.2f} EGP!")
    elif remaining == 0:
        print("You have used your entire budget.")
    else:
        percentage = (total / budget) * 100
        print(f"Budget used: {percentage:.1f}%")

        if percentage >= 80:
            print("Warning: You are approaching your budget limit.")


def show_category_summary(data):
    print("\n--- Spending by Category ---")

    totals = get_category_totals(data)

    if not totals:
        print("No expenses recorded yet.")
        return

    for category, amount in sorted(
        totals.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        print(f"{category}: {amount:.2f} EGP")


def main():
    data = load_data()

    while True:
        print("\n" + "=" * 38)
        print("         EXPENSE TRACKER")
        print("=" * 38)
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. View budget summary")
        print("4. Set or update budget")
        print("5. View spending by category")
        print("6. Exit")

        choice = input("\nChoose an option (1-6): ").strip()

        if choice == "1":
            try:
                add_expense_menu(data)
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            view_expenses(data)

        elif choice == "3":
            show_summary(data)

        elif choice == "4":
            budget = read_positive_amount(
                "Enter your budget in EGP (0 to reset): ",
                allow_zero=True
            )
            set_budget(data, budget)
            save_data(data)
            print(f"Budget saved: {budget:.2f} EGP")

        elif choice == "5":
            show_category_summary(data)

        elif choice == "6":
            save_data(data)
            print("Your data has been saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
