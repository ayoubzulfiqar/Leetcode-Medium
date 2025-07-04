def calculate_running_total_by_gender(transactions):
    gender_totals = {}
    print("--- Running Totals by Gender ---")
    for i, transaction in enumerate(transactions):
        gender = transaction.get('gender')
        amount = transaction.get('amount')

        if gender is None or not isinstance(amount, (int, float)):
            print(f"Skipping invalid transaction at index {i}: {transaction}")
            continue

        if gender not in gender_totals:
            gender_totals[gender] = 0

        gender_totals[gender] += amount
        print(f"Transaction {i+1} (Gender: {gender}, Amount: {amount}):")
        for g, total in gender_totals.items():
            print(f"  {g}: {total}")
        print("-" * 30)

    print("\n--- Final Totals by Gender ---")
    for g, total in gender_totals.items():
        print(f"{g}: {total}")

if __name__ == "__main__":
    transactions_data = [
        {'name': 'Alice', 'gender': 'Female', 'amount': 100},
        {'name': 'Bob', 'gender': 'Male', 'amount': 50},
        {'name': 'Charlie', 'gender': 'Male', 'amount': 75},
        {'name': 'Diana', 'gender': 'Female', 'amount': 120},
        {'name': 'Eve', 'gender': 'Non-binary', 'amount': 30},
        {'name': 'Frank', 'gender': 'Male', 'amount': 200},
        {'name': 'Grace', 'gender': 'Female', 'amount': 80},
        {'name': 'Alex', 'gender': 'Non-binary', 'amount': 45},
        {'name': 'InvalidAmount', 'gender': 'Male', 'amount': 'abc'},
        {'name': 'MissingGender', 'amount': 10},
        {'name': 'ZeroAmount', 'gender': 'Female', 'amount': 0},
    ]

    calculate_running_total_by_gender(transactions_data)

    print("\n--- Another Example ---")
    transactions_data_2 = [
        {'gender': 'Male', 'amount': 10},
        {'gender': 'Female', 'amount': 20},
        {'gender': 'Male', 'amount': 15},
        {'gender': 'Female', 'amount': 25},
    ]
    calculate_running_total_by_gender(transactions_data_2)

    print("\n--- Empty List Example ---")
    calculate_running_total_by_gender([])