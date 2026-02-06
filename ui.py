# ui.py - User Interface and Input Handl
from expense import validate_input, Expense
from reports import generate_total_report, generate_average_report, generate_category_report, print_all_expenses
from file_handler import save_expenses  # if needed here

def display_menu():
    """Print the main menu."""
    print("\n" + "="*50)
    print("Personal Finance Manager")
    print("="*50)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Generate Total Report")
    print("4. Generate Average Report")
    print("5. Category-Wise Report")
    print("6. Backup Data")
    print("7. Restore from Backup")
    print("8. Exit")
    print("="*50)

def get_user_choice():
    """Get validated menu choice (1-8)."""
    while True:
        try:
            choice = int(input("Enter your choice (1-8): "))
            if 1 <= choice <= 8:
                return choice
            else:
                print("Please enter a number between 1 and 8.")
        except ValueError:
            print("Please enter a valid number.")

def add_expense_ui(expenses):
    try:
        amount = validate_input("Enter amount (e.g., 100.50): ", lambda x: x)
        category = validate_input("Enter category (e.g., Food): ", lambda x: x)
        date = validate_input("Enter date (YYYY-MM-DD): ", lambda x: x)
        description = validate_input("Enter description: ", lambda x: x)
        
        expense = Expense(amount, category, date, description)
        expenses.append(expense)
        print(f"Added: {expense}")
        
        # THIS LINE WAS MISSING OR COMMENTED BEFORE – NOW ACTIVE
        save_expenses(expenses)          # Save right after adding
        
    except ValueError as e:
        print(f"Failed to add expense: {e}")