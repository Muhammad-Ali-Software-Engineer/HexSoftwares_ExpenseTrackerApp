
# ================= Expense Tracker App =================

from colorama import Fore,Style,init

init(autoreset=True)
heading = Fore.YELLOW
success = Fore.GREEN
warning = Fore.RED
inputt = Fore.LIGHTCYAN_EX 
blue = Fore.BLUE
reset = Fore.RESET

def AddExpense():
    date = input("Enter date(dd-mm-yyyy): ")
    category = input("Enter Category: ")
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print(warning + "Invalid amount. Please enter numeric value.")

    description = input("Enter description:")
    with open("expenses.csv","a") as file:
        file.write(f"{date},{category},{amount},{description}\n")

def ViewAllExpenses():
    try:
        with open("expenses.csv") as file:
            lines = file.readlines()

            if not lines:
                print("No expenses recorded yet.")
                return

        print(reset+ "-" * 50)
        print(f"{'Date':<13}{'Category':<15}{'Amount':<10}{'Description'}")
        print("-" * 50)
        for line in lines:
            line = line.strip().split(",")
            print(f"{line[0]:<13}{line[1]:<15}{line[2]:<10}{line[3]}")
        print("-" * 50)

    except FileNotFoundError:
        print("No expenses recorded yet.")

def ViewSummary():
    try:
        with open("expenses.csv") as file:
            data = file.readlines()
            if not data:
                print("No expenses recorded yet.")
                return
        
        totalExpense = 0
        category_total = {}
        for line in data:
            line = line.strip().split(",")
            category = line[1]
            amount = float(line[2])
            totalExpense += amount
            if category in category_total:
                category_total[category] += amount
            else:
                category_total[category] = amount
        print(heading + "\nTotal Expense:",totalExpense)
        print(heading + "\nCategory-wise summary:")
        for c in category_total:
            print(c,":",category_total[c])
        
        expense_count = len(data)
        print(heading + "\nTotal transactions:",expense_count)
    
    except FileNotFoundError:
        print("No expenses recorded yet.")

def DeleteExpense():
    try:
        with open("expenses.csv") as file:
            data = file.readlines()

        if not data:
            print("No expenses to delete.")
            return

        print(heading + "\nExpenses:")
        for i, line in enumerate(data, start=1):
            line = line.strip().split(",")
            print(f"{i}. {line[0]} | {line[1]} | {line[2]} | {line[3]}")

        num = int(input("\nEnter expense number to delete: "))

        if num < 1 or num > len(data):
            print(warning + "Invalid selection.")
            return

        data.pop(num - 1)

        with open("expenses.csv", "w") as file:
            file.writelines(data)

        print(success + "Expense deleted successfully.")

    except FileNotFoundError:
        print("No expenses recorded yet.")

def SearchExpense():
    keyword = input("Enter category/date/description to search: ").lower()

    try:
        with open("expenses.csv") as file:
            data = file.readlines()

        found = False

        for line in data:
            line_data = line.strip().split(",")

            if keyword in line.lower():
                if not found:
                    print(blue + "\nMatching Expenses:")
                    print("-"*50)
                    print(f"{'Date':<13}{'Category':<15}{'Amount':<10}{'Description'}")
                    print("-"*50)

                print(f"{line_data[0]:<13}{line_data[1]:<15}{line_data[2]:<10}{line_data[3]}")
                found = True

        if not found:
            print("No matching expense found.")

    except FileNotFoundError:
        print("No expenses recorded yet.")

def EditExpense():
    try:
        with open("expenses.csv") as file:
            data = file.readlines()

        if not data:
            print("No expenses to edit.")
            return

        print("\nExpenses List:")
        for i, line in enumerate(data, start=1):
            d = line.strip().split(",")
            print(f"{i}. {d[0]} | {d[1]} | {d[2]} | {d[3]}")

        num = int(input("\nEnter expense number to edit: "))

        if num < 1 or num > len(data):
            print(warning + "Invalid selection.")
            return

        selected = data[num-1].strip().split(",")

        print(heading + "\nWhat do you want to edit?")
        print("1. Date")
        print("2. Category")
        print("3. Amount")
        print("4. Description")

        choice = input("Enter choice: ")

        if choice == '1':
            selected[0] = input("Enter new date: ")

        elif choice == '2':
            selected[1] = input("Enter new category: ")

        elif choice == '3':
            selected[2] = input("Enter new amount: ")

        elif choice == '4':
            selected[3] = input("Enter new description: ")

        else:
            print(warning + "Invalid choice.")
            return

        data[num-1] = ",".join(selected) + "\n"

        with open("expenses.csv","w") as file:
            file.writelines(data)

        print(success + "Expense updated successfully!")

    except FileNotFoundError:
        print("No expenses recorded yet.")

def HighestSpendingCategory():
    try:
        with open("expenses.csv") as file:
            data = file.readlines()

        if not data:
            print("No expenses recorded yet.")
            return

        category_total = {}

        for line in data:
            line = line.strip().split(",")
            category = line[1]
            amount = float(line[2])

            if category in category_total:
                category_total[category] += amount
            else:
                category_total[category] = amount

        highest_category = max(category_total, key=category_total.get)

        print(heading + "\nHighest Spending Category:")
        print(highest_category, ":", category_total[highest_category])        

    except FileNotFoundError:
        print("No expenses recorded yet.")

def BudgetLimitWarning():
    try:
        budget = float(input("Enter your budget limit: "))

        with open("expenses.csv") as file:
            data = file.readlines()

        total = 0

        for line in data:
            line = line.strip().split(",")
            total += float(line[2])

        print("\nTotal Expense:", total) # ? change color

        if total > budget:
            print(warning + "⚠ Warning: Budget exceeded!")
        else:
            print(success + "You are within your budget.")

    except FileNotFoundError:
        print("No expenses recorded yet.")

def ExpensePercentageByCategory():
    try:
        with open("expenses.csv") as file:
            data = file.readlines()

        if not data:
            print("No expenses recorded yet.")
            return

        total_expense = 0
        category_total = {}

        for line in data:
            line = line.strip().split(",")
            category = line[1]
            amount = float(line[2])

            total_expense += amount
            if category in category_total:
                category_total[category] += amount
            else:
                category_total[category] = amount

        print(heading + "\nExpense Percentage by Category:")
        print("-" * 40)
        print(f"{'Category':<15}{'Amount':<10}{'Percentage'}")
        print("-" * 40)

        for category, amount in category_total.items():
            percentage = (amount / total_expense) * 100
            print(f"{category:<15}{amount:<10.2f}{percentage:.2f}%")

        print("-" * 40)
        print(f"Total Expense: {total_expense:.2f}")

    except FileNotFoundError:
        print("No expenses recorded yet.")

while True:
    print(inputt + "---------------------------------")
    print(inputt + "       Expense Tracker App")
    print(inputt + "---------------------------------")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Highest Spending Category")
    print("5. Expense Percentage by Category")
    print("6. Budget Check")
    print("7. Search Expense")
    print("8. Edit Expense")
    print("9. Delete Expense")
    print("10. Exit")

    choice = input(inputt + "Enter your choice(1 - 10): ")

    match choice:
        case '1':
            AddExpense()
        case '2':
            ViewAllExpenses()
        case '3':
            ViewSummary()
        case '4':
            HighestSpendingCategory()
        case '5':
            ExpensePercentageByCategory()
        case '6':
            BudgetLimitWarning()
        case '7':
            SearchExpense()
        case '8':
            EditExpense()
        case '9':
            DeleteExpense()
        case '10':
            print(heading + "App Closed.")
            break
        case _:
            print(warning + "Invalid input.")

