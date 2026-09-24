from functools import reduce


def main():
    expenses = []

    number_expenses = int(input("How many monthly expenses would you like to enter? "))

    for i in range(number_expenses):
        print("\nExpense", i + 1)

        expense_type = input("Enter the type of expense: ")
        amount = float(input("Enter the amount: $"))

        expenses.append([expense_type, amount])

    # Calculate the total of all expenses
    total = reduce(lambda x, expense: x + expense[1], expenses, 0)

    # Find the expense with the highest amount
    highest = reduce(
        lambda x, y: x if x[1] > y[1] else y,
        expenses
    )

    # Find the expense with the lowest amount
    lowest = reduce(
        lambda x, y: x if x[1] < y[1] else y,
        expenses
    )

    print("\nMonthly Expense Summary")
    print("-----------------------")
    print(f"Total expenses: ${total:.2f}")
    print(f"Highest expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest expense: {lowest[0]} - ${lowest[1]:.2f}")


main()