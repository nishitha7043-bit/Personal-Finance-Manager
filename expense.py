# expense.py - Updated Expense class with flexible date input

import re
from datetime import datetime

class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = self._validate_amount(amount)
        self.category = self._validate_category(category)
        self.date = self._validate_date(date)          # ← improved
        self.description = self._validate_description(description)
    
    def _validate_amount(self, amount):
        try:
            amt = float(amount)
            if amt <= 0:
                raise ValueError("Amount must be positive.")
            return round(amt, 2)
        except (ValueError, TypeError):
            raise ValueError("Amount must be a positive number (e.g., 100.50).")
    
    def _validate_category(self, category):
        if not category or not isinstance(category, str) or len(category.strip()) < 1:
            raise ValueError("Category must be a non-empty string (e.g., Food, Rent).")
        return category.strip().title()
    
    def _validate_date(self, date_input):
        date_input = date_input.strip()
        
        # Try standard format first (YYYY-MM-DD)
        try:
            dt = datetime.strptime(date_input, '%Y-%m-%d')
            return date_input  # already correct format
        except ValueError:
            pass
        
        # Try Indian/common format (DD-MM-YYYY) and convert
        try:
            dt = datetime.strptime(date_input, '%d-%m-%Y')
            return dt.strftime('%Y-%m-%d')  # convert to standard
        except ValueError:
            pass
        
        # Optional: you can add more formats here later (like %d/%m/%Y)
        
        raise ValueError(
            "Date must be in YYYY-MM-DD format (e.g., 2026-01-28) "
            "or DD-MM-YYYY format (e.g., 28-01-2026)."
        )
    
    def _validate_description(self, description):
        if not description or not isinstance(description, str) or len(description.strip()) < 1:
            raise ValueError("Description must be a non-empty string.")
        return description.strip()
    
    def __str__(self):
        return f"{self.date} | {self.category}: ₹{self.amount} - {self.description}"
    # expense.py

# ... your Expense class remains unchanged ...

def validate_input(prompt, validator_func):
    """General input validator with error handling."""
    while True:
        try:
            user_input = input(prompt).strip()
            return validator_func(user_input)
        except ValueError as e:
            print(f"Error: {e}. Please try again.")