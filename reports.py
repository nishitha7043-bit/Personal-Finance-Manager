from collections import defaultdict  # For category totals

def generate_total_report(expenses):
    """Calculate and print total expenses."""
    if not expenses:
        print("No expenses to report.")
        return
    total = sum(expense.amount for expense in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}")

def generate_average_report(expenses):
    """Calculate and print average expense."""
    if not expenses:
        print("No expenses to report.")
        return
    # Simple two-step calculation (works on all Python 3.7+ versions)
    total = sum(expense.amount for expense in expenses)
    avg = total / len(expenses)
    print(f"Average Expense: ₹{avg:.2f} (based on {len(expenses)} entries)")

def generate_category_report(expenses):
    """Category-wise expense breakdown."""
    if not expenses:
        print("No expenses to report.")
        return
    category_totals = defaultdict(float)
    for expense in expenses:
        category_totals[expense.category] += expense.amount
    
    print("\nCategory Breakdown:")
    print("-" * 40)
    for category, total in sorted(category_totals.items()):
        print(f"{category}: ₹{total:.2f}")
    print("-" * 40)

def print_all_expenses(expenses):
    """Display all expenses."""
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nAll Expenses:")
    print("-" * 60)
    for expense in expenses:
        print(expense)
    print("-" * 60)