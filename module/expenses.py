# Define a dictionary to categorize and store expenses
expenses = {
    "Food": [10.50, 8],
    "Transport": [5, 20],
    "Entertainment": [15],
    "Other": [5, 3]
}


def calculate_total(expenses):
    """
    Calculate the total expenses by category and overall.
    """
    total_by_category = {category: sum(items) for category, items in expenses.items()}
    overall_total = sum(total_by_category.values())
    return total_by_category, overall_total


def display_expenses(expenses):
    """
    Display itemized expenses and their totals.
    """
    print("\n--- Expense Breakdown ---")
    for category, items in expenses.items():
        print(f"{category}: {', '.join(f'${item:.2f}' for item in items)}")
    print("-------------------------")


def main():
    """
    Main function to calculate and display expenses.
    """
    # Display the itemized expenses
    display_expenses(expenses)

    # Calculate totals
    total_by_category, overall_total = calculate_total(expenses)

    # Display total expenses by category
    print("\n--- Totals by Category ---")
    for category, total in total_by_category.items():
        print(f"{category}: ${total:.2f}")

    # Display overall total
    print("-------------------------")
    print(f"Overall Total: ${overall_total:.2f}")


if __name__ == "__main__":
    main()
