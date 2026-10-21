print("=== EXPENSE TRACKER ===")
exp = float(input("Enter your starting budget: $"))
remaining = exp
expenses = []
while True:
    print("1. Add Expense")
    print("2. View Budget")
    print("3. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        expense_name = input("Expense name: ")
        rembud = float(input("Expense amount: $"))

        if rembud <= 0:
            print("Expense must be greater than zero!")
        elif rembud > remaining:
            print("Insufficient budget!")
        else:
            remaining = remaining - rembud
            expenses.append([expense_name, rembud])
            print(f"Remaining budget: ${remaining:.2f}")
            print(f"{expense_name} expense of ${rembud:.2f} recorded!")
    elif choice == "2":
        print(f"Starting budget: ${exp:.2f}")
        print(f"Total spent: ${exp - remaining:.2f}")
        print(f"Remaining budget: ${remaining:.2f}")
        print("=== EXPENSE HISTORY ===")
        for item in expenses:
            print(f"{item[0]}: ${item[1]:.2f}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")