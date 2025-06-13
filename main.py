from datetime import datetime, date
from transaction import Transaction
from transaction_manager import TransactionManager
import file_handler

FILENAME = "data/transactions.txt"

def get_valid_date():
    while True:
        try:
            date_str = input("Enter Date (yyyy-MM-dd): ")
            entered_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            if entered_date > date.today():
                print(" Future date not allowed.")
            else:
                return entered_date
        except ValueError:
            print(" Invalid date format.")

def main():
    manager = TransactionManager()
    manager.transactions = file_handler.load_from_file(FILENAME)

    while True:
        print("Expense Tracker ")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Monthly Summary")
        print("4. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            print("Choose category: 1. Salary  2. Business  3. Other")
            cat_choice = input("Enter choice: ")
            category = {"1": "Salary", "2": "Business", "3": "Other"}.get(cat_choice)
            if not category:
                print(" Invalid category.")
                continue
            amount = float(input("Enter Amount: "))
            date_val = get_valid_date()
            t = Transaction("Income", category, amount, date_val)
            manager.add(t)
            file_handler.save_to_file(manager.get_all(), FILENAME)
            print("Income added and saved.")

        elif choice == "2":
            date_val = get_valid_date()
            if not manager.has_income_for_month(date_val.year, date_val.month):
                print(f" No income for {date_val.strftime('%B %Y')}. Add income first.")
                continue
            print("Choose category: 1. Food  2. Rent  3. Travel  4. Other")
            cat_choice = input("Enter choice: ")
            category = {"1": "Food", "2": "Rent", "3": "Travel", "4": "Other"}.get(cat_choice)
            if not category:
                print(" Invalid category.")
                continue
            amount = float(input("Enter Amount: "))
            t = Transaction("Expense", category, amount, date_val)
            manager.add(t)
            file_handler.save_to_file(manager.get_all(), FILENAME)
            print(" Expense added and saved.")

        elif choice == "3":
            year = int(input("Enter Year (e.g. 2025): "))
            month = int(input("Enter Month (1-12): "))
            manager.show_monthly_summary(year, month)

        elif choice == "4":
            print("Exiting... Your data is saved.")
            break

        else:
            print(" Invalid option. Try again.")

if __name__ == "__main__":
    main()