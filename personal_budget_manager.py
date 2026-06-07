# Personal Budget Manager
# Author: Qhamkile Mkhize

def calculate_budget():
    print("\n=== Personal Budget Manager ===")

    salary = float(input("Enter monthly salary (R): "))
    expenses = float(input("Enter monthly expenses (R): "))
    water_usage = float(input("Enter water usage (kL): "))
    product_price = float(input("Enter product price (R): "))
    money_available = float(input("Enter available money (R): "))
    transaction_amount = float(input("Enter transaction amount (R): "))

    # Disposable income
    disposable_income = salary - expenses

    # Water bill
    if water_usage <= 50:
        water_bill = 15
    else:
        water_bill = 25

    # Purchasing power
    if product_price > 0:
        items = int(money_available // product_price)
    else:
        items = 0

    # Transaction validation
    valid_transaction = (
        transaction_amount % 10 == 0
        and transaction_amount != 0
    )

    # Financial status
    if disposable_income > 0:
        financial_status = "Healthy"
    else:
        financial_status = "Financial Distress"

    print("\n=== BUDGET REPORT ===")
    print(f"Disposable Income: R{disposable_income:.2f}")
    print(f"Water Bill: R{water_bill:.2f}")
    print(f"Items Affordable: {items}")
    print(f"Transaction Valid: {valid_transaction}")
    print(f"Financial Status: {financial_status}")

    return {
        "salary": salary,
        "expenses": expenses,
        "disposable_income": disposable_income,
        "water_bill": water_bill
    }


budget_history = []

while True:

    print("\n===== PERSONAL BUDGET MANAGER =====")
    print("1. Create Budget Report")
    print("2. View Number of Reports")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        report = calculate_budget()
        budget_history.append(report)

    elif choice == "2":
        print(
            f"\nReports Created: {len(budget_history)}"
        )

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
