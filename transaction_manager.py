from datetime import datetime
from calendar import month_name

class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add(self, transaction):
        self.transactions.append(transaction)

    def get_all(self):
        return self.transactions

    def show_monthly_summary(self, year, month):
        income = 0
        expense = 0
        found = False

        for t in self.transactions:
            if t.date.year == year and t.date.month == month:
                found = True
                if t.type == "Income":
                    income += t.amount
                elif t.type == "Expense":
                    expense += t.amount

        print(f"\nMonthly Summary for {month_name[month]} {year}")
        if not found:
            print("No transactions found for this month.")
            return

        print(f"Total Income  : ₹{income:.2f}")
        print(f"Total Expense : ₹{expense:.2f}")
        print(f"Net Savings   : ₹{income - expense:.2f}")

    def has_income_for_month(self, year, month):
        for t in self.transactions:
            if t.type == "Income" and t.date.year == year and t.date.month == month:
                return True
        return False