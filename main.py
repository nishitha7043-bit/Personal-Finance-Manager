from file_handler import save_expenses, load_expenses, backup_data, restore_data
from ui import display_menu, get_user_choice, add_expense_ui
from reports import generate_total_report, generate_average_report, generate_category_report, print_all_expenses

def main():
    expenses = load_expenses()  # Load existing data
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 1:
            add_expense_ui(expenses)
            save_expenses(expenses)  # Auto-save after add
        
        elif choice == 2:
            print_all_expenses(expenses)
        
        elif choice == 3:
            generate_total_report(expenses)
        
        elif choice == 4:
            generate_average_report(expenses)
        
        elif choice == 5:
            generate_category_report(expenses)
        
        elif choice == 6:
            backup_data()
        
        elif choice == 7:
            expenses = restore_data()
        
        elif choice == 8:
            save_expenses(expenses)  # Final save on exit
            print("Thank you! Data saved. Goodbye.")
            break
        
        input("\nPress Enter to continue...")  # Pause for readability

if __name__ == "__main__":
    main()

