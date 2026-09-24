expenses = []

def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    for expense in expenses:
        print("\nAmount:", expense["amount"])
        print("Category:", expense["category"])
        print("Description:", expense["description"])


def total_expense():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expense:", total)


while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")
