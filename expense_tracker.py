"""
Personal Expense Tracker

Author: Danilo Vunza
Course: COSC 1436

Description:
Tracks personal expenses and calculates
remaining balance and savings percentage.
"""


def get_valid_number(prompt):
    """
    Get valid numeric input from user.
    """

    while True:

        try:
            value = float(input(prompt))

            if value < 0:
                print("Please enter a positive number.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_total_expenses(expenses):
    """
    Calculate total expenses.
    """

    return sum(expenses)


def calculate_savings_percentage(income, remaining_balance):
    """
    Calculate savings percentage.
    """

    if income == 0:
        return 0

    return (remaining_balance / income) * 100


def main():

    print("=" * 50)
    print("PERSONAL EXPENSE TRACKER")
    print("=" * 50)

    income = get_valid_number(
        "Enter your monthly income: "
    )

    food = get_valid_number(
        "Enter food expenses: "
    )

    transport = get_valid_number(
        "Enter transport expenses: "
    )

    rent = get_valid_number(
        "Enter rent expenses: "
    )

    entertainment = get_valid_number(
        "Enter entertainment expenses: "
    )

    expenses = [
        food,
        transport,
        rent,
        entertainment
    ]

    total_expenses = calculate_total_expenses(
        expenses
    )

    remaining_balance = income - total_expenses

    savings_percentage = (
        calculate_savings_percentage(
            income,
            remaining_balance
        )
    )

    print("\nEXPENSE REPORT")
    print("-" * 50)

    print(f"Monthly Income:      ${income:.2f}")
    print(f"Total Expenses:      ${total_expenses:.2f}")
    print(f"Remaining Balance:   ${remaining_balance:.2f}")
    print(f"Savings Percentage:  {savings_percentage:.2f}%")

    print("-" * 50)


main()
