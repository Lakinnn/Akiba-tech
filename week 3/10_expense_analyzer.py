print("==== Expense Analyzer ====")
def add_expense(expenses, description, category, amount):
    if not description.strip():
        raise ValueError("Description cannot be empty.")

    if not category.strip():
        raise ValueError("Category cannot be empty.")

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    expenses.append({
        "description": description,
        "category": category,
        "amount": amount
    })


def calculate_total_expenses(expenses):
    return sum(expense["amount"] for expense in expenses)


def spending_by_category(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    return totals


def find_largest_expense(expenses):
    if not expenses:
        return None

    return max(expenses, key=lambda expense: expense["amount"])


def expenses_above_threshold(expenses, threshold=300):
    return [
        expense for expense in expenses
        if expense["amount"] > threshold
    ]


def category_percentages(expenses):
    total = calculate_total_expenses(expenses)

    if total == 0:
        return {}

    category_totals = spending_by_category(expenses)

    return {
        category: (amount / total) * 100
        for category, amount in category_totals.items()
    }


def highest_spending_category(expenses):
    category_totals = spending_by_category(expenses)

    if not category_totals:
        return None

    return max(category_totals, key=category_totals.get)


def generate_spending_report(expenses, threshold=300):
    total = calculate_total_expenses(expenses)
    category_totals = spending_by_category(expenses)
    percentages = category_percentages(expenses)

    return {
        "total_expenses": total,
        "spending_by_category": category_totals,
        "category_percentages": percentages,
        "largest_expense": find_largest_expense(expenses),
        "above_threshold": expenses_above_threshold(
            expenses, threshold
        ),
        "highest_spending_category": highest_spending_category(expenses)
    }


# Example data
expenses = [
    {"description": "Lunch", "category": "Food", "amount": 180},
    {"description": "Taxi", "category": "Transport", "amount": 120},
    {"description": "Groceries", "category": "Food", "amount": 450},
    {"description": "Internet", "category": "Bills", "amount": 300}
]

add_expense(expenses, "Coffee", "Food", 80)

report = generate_spending_report(expenses, threshold=250)

print(f"Total expenses: {report['total_expenses']:.2f}")

print("\nSpending by category:")
for category, amount in report["spending_by_category"].items():
    percentage = report["category_percentages"][category]
    print(f"{category}: {amount:.2f} ({percentage:.2f}%)")

print("\nLargest expense:")
print(report["largest_expense"])

print("\nExpenses above threshold:")
for expense in report["above_threshold"]:
    print(expense)

print(
    "\nHighest spending category:",
    report["highest_spending_category"]
)
