# Get details of the loan
money_owed = float(input("How much money do you owe, in dollars? "))  # Example: $50,000
apr = float(input("What is the annual percentage rate of the loan? "))  # Example: 3%
payment = float(input("How much will you pay off each month in dollars? "))  # Example: $1,000
months = int(input("How many months do you want to see the results for? "))  # Example: 24

# Convert APR to monthly interest rate
monthly_rate = apr / 100 / 12

# Simulate the loan repayment
print("\n--- Loan Repayment Schedule ---")
for month in range(1, months + 1):
    # Calculate interest for the month
    interest_paid = money_owed * monthly_rate

    # Add interest to the loan balance
    money_owed += interest_paid

    # Check if the monthly payment is more than the remaining balance
    if money_owed < payment:
        payment = money_owed  # Adjust the final payment to pay off the loan

    # Subtract the monthly payment
    money_owed -= payment

    # Display the result for the current month
    print(
        f"Month {month}: Paid ${payment:.2f}, of which ${interest_paid:.2f} was interest. Remaining balance: ${money_owed:.2f}")

    # If the loan is fully paid off, stop the loop
    if money_owed <= 0:
        print("\nCongratulations! You have fully paid off your loan.")
        break

# If the loan is not fully paid after the specified months
if money_owed > 0:
    print(f"\nAfter {months} months, you still owe: ${money_owed:.2f}")
