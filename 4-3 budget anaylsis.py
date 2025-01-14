amountBudget = int(input("Enter the budget amount"))
expenses = 0
total = 0
whatexpense = input("are there more expenses? yes or no")
while whatexpense == "yes":
    expenses = float(input("Enter amount for this expense"))
    total += expenses
    whatexpense = input("are there more expenses? yes or no")
if amountBudget < total:
    amountOverBudget = total - amountBudget
    print(f"you are {amountOverBudget} over the budget")
if amountBudget > total:
    amountUnderBudget = amountBudget - total
    print(f"you are {amountUnderBudget} amount under budget")

    