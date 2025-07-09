def calculate_final_balance(initial_balance, transactions):
    current_balance = initial_balance
    for amount in transactions:
        current_balance += amount
    return current_balance

if __name__ == "__main__":
    initial_balance_1 = 1000.00
    transactions_1 = [500.00, -200.00, 150.00, -50.00]
    final_balance_1 = calculate_final_balance(initial_balance_1, transactions_1)
    print(f"Final Balance 1: {final_balance_1}")

    initial_balance_2 = 500.00
    transactions_2 = []
    final_balance_2 = calculate_final_balance(initial_balance_2, transactions_2)
    print(f"Final Balance 2: {final_balance_2}")

    initial_balance_3 = 750.00
    transactions_3 = [-100.00, -50.00, -200.00]
    final_balance_3 = calculate_final_balance(initial_balance_3, transactions_3)
    print(f"Final Balance 3: {final_balance_3}")

    initial_balance_4 = 0.00
    transactions_4 = [100.00, -20.00, 50.00]
    final_balance_4 = calculate_final_balance(initial_balance_4, transactions_4)
    print(f"Final Balance 4: {final_balance_4}")

    initial_balance_5 = 200
    transactions_5 = [50, -30, 10]
    final_balance_5 = calculate_final_balance(initial_balance_5, transactions_5)
    print(f"Final Balance 5: {final_balance_5}")