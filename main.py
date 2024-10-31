# main.py
from database import Database
from visualization import Visualization
from notification import Notification

class BudgetTracker:
    def __init__(self):
        self.db = Database("budget.db")
        self.db.create_table()
        self.visualization = Visualization()
        self.notification = Notification()

    def run(self):
        while True:
            print("1. Add income")
            print("2. Add expense")
            print("3. View expenses")
            print("4. Visualize spending")
            print("5. Set notification limit")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                income = float(input("Enter income: "))
                # Store income in database
            elif choice == "2":
                date = input("Enter date (YYYY-MM-DD): ")
                category = input("Enter category: ")
                amount = float(input("Enter amount: "))
                self.db.insert_expense(date, category, amount)
            elif choice == "3":
                expenses = self.db.get_expenses()
                for expense in expenses:
                    print(expense)
            elif choice == "4":
                self.visualization.plot_expenses(self.db.get_expenses())
            elif choice == "5":
                limit = float(input("Enter notification limit: "))
                self.notification.set_limit(limit)
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    tracker = BudgetTracker()
    tracker.run()
