import csv
import os
from expense import Expense

FILENAME = 'expenses.csv'
BACKUP_FILENAME = 'backup.csv'

def save_expenses(expenses, filename='expenses.csv'):
    print("DEBUG SAVE START - count:", len(expenses))
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])
            print("DEBUG: Header written")
            
            for i, exp in enumerate(expenses, 1):
                print(f"DEBUG: Trying expense {i}")
                try:
                    print("  date       :", exp.date)
                    print("  category   :", exp.category)
                    print("  amount     :", exp.amount)
                    print("  description:", exp.description)
                    
                    row = [exp.date, exp.category, exp.amount, exp.description]
                    print("  Row ready  :", row)
                    
                    writer.writerow(row)
                    print("  Row written OK")
                except Exception as e:
                    print(f"  ERROR on expense {i}: {e}")
                    print("  Object str :", str(exp))
                    continue
            
            print("DEBUG: Save finished")
        print("Success message (file closed)")
    except Exception as e:
        print("File open/write failed:", e)

def load_expenses(filename=FILENAME):
    """Load expenses from CSV file into list of Expense objects."""
    expenses = []
    if not os.path.exists(filename):
        print(f"No {filename} found. Starting with empty data.")
        return expenses
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    expense = Expense(row['Amount'], row['Category'], row['Date'], row['Description'])
                    expenses.append(expense)
                except ValueError:
                    print(f"Skipping invalid row: {row}")
        print(f"Loaded {len(expenses)} expenses from {filename}.")
    except (IOError, KeyError) as e:
        print(f"Error loading file: {e}. Starting with empty data.")
    return expenses

def backup_data():
    """Create a backup of the current expenses CSV."""
    if not os.path.exists(FILENAME):
        print("No data to backup.")
        return
    try:
        import shutil
        shutil.copy2(FILENAME, BACKUP_FILENAME)
        print("Backup created as backup.csv.")
    except IOError as e:
        print(f"Error creating backup: {e}")

def restore_data():
    """Restore from backup CSV."""
    if not os.path.exists(BACKUP_FILENAME):
        print("No backup found.")
        return load_expenses()
    try:
        import shutil
        shutil.copy2(BACKUP_FILENAME, FILENAME)
        print("Data restored from backup.csv.")
        return load_expenses()
    except IOError as e:
        print(f"Error restoring backup: {e}")
        return load_expenses()