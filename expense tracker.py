import json
import os

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = {}

    def add_expense(self, amount, description, category):
        self.expenses.append({"amount": amount, "description": description, "category": category})

    def save_expenses(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.expenses, file)

    def load_expenses(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.expenses = json.load(file)

    def categorize_expenses(self):
        for expense in self.expenses:
            category = expense["category"]
            if category not in self.categories:
                self.categories[category] = []
            self.categories[category].append(expense)

    def monthly_summary(self):
        monthly_expenses = {}
        for expense in self.expenses:
            month = expense["date"].split("-")[1]
            if month not in monthly_expenses:
                monthly_expenses[month] = 0
            monthly_expenses[month] += expense["amount"]
        return monthly_expenses

    def category_summary(self):
        self.categorize_expenses()
        return self.categories

    def print_expenses(self):
        for expense in self.expenses:
            print(f"Amount: {expense['amount']}, Description: {expense['description']}, Category: {expense['category']}")

# Example usage:
expense_tracker = ExpenseTracker()
expense_tracker.add_expense(50, "Groceries", "Food")
expense_tracker.add_expense(30, "Transportation", "Transportation")
expense_tracker.save_expenses("expenses.json")
expense_tracker.load_expenses("expenses.json")
expense_tracker.print_expenses()
print("Monthly Summary:", expense_tracker.monthly_summary())
print("Category Summary:", expense_tracker.category_summary())
