class ExpenseTracker:
    def __init__(self, filename="expenses.txt"):
        self.filename = filename

    def add_expense(self, amount, note):
        with open(self.filename, "a") as f:
            f.write(f"{amount},{note}\n")
        print("Expense added ✓")

    def view_expenses(self):
        print("\n----- Expense History -----")
        try:
            with open(self.filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    amount, note = line.strip().split(",")
                    print(f"₹{amount}  -  {note}")
        except FileNotFoundError:
            print("No expenses recorded yet.")
        print("---------------------------\n")

    def total_expense(self):
        total = 0
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    amount, _ = line.strip().split(",")
                    total += float(amount)
            print(f"Total Spent: ₹{total}")
        except FileNotFoundError:
            print("No expenses yet.")
    

# ------ MENU ------
tracker = ExpenseTracker()

while True:
    print("=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spent")
    print("4. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        amt = input("Enter amount: ")
        note = input("Enter note: ")
        tracker.add_expense(amt, note)

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.total_expense()

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice, try again.\n")
