import datetime

class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0.0):
        if not isinstance(account_number, str) or not account_number:
            raise ValueError("Account number must be a non-empty string.")
        if not isinstance(owner_name, str) or not owner_name:
            raise ValueError("Owner name must be a non-empty string.")
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")

        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = float(initial_balance)
        self.transactions = []
        self._record_transaction("Account Opened", initial_balance)

    def _record_transaction(self, transaction_type, amount, success=True, message=""):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append({
            "timestamp": timestamp,
            "type": transaction_type,
            "amount": amount,
            "balance_after": self.balance,
            "success": success,
            "message": message
        })

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            self._record_transaction("Deposit (Failed)", amount, success=False, message="Deposit amount must be positive.")
            return False, "Deposit amount must be positive."
        self.balance += amount
        self._record_transaction("Deposit", amount)
        return True, f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            self._record_transaction("Withdrawal (Failed)", amount, success=False, message="Withdrawal amount must be positive.")
            return False, "Withdrawal amount must be positive."
        if amount > self.balance:
            self._record_transaction("Withdrawal (Failed)", amount, success=False, message="Insufficient funds.")
            return False, "Insufficient funds."
        self.balance -= amount
        self._record_transaction("Withdrawal", amount)
        return True, f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"

    def get_balance(self):
        return self.balance

    def get_summary(self):
        summary = f"--- Bank Account Summary ---\n"
        summary += f"Account Number: {self.account_number}\n"
        summary += f"Account Holder: {self.owner_name}\n"
        summary += f"Current Balance: ${self.balance:.2f}\n"
        summary += f"----------------------------"
        return summary

    def get_transaction_history(self):
        history = ["--- Transaction History ---"]
        if not self.transactions:
            history.append("No transactions recorded.")
        else:
            for t in self.transactions:
                status = "SUCCESS" if t.get('success', True) else "FAILED"
                msg = f" ({t['message']})" if t.get('message') else ""
                history.append(
                    f"{t['timestamp']} | Type: {t['type']:<16} | Amount: ${t['amount']:.2f} | Balance After: ${t['balance_after']:.2f} | Status: {status}{msg}"
                )
        history.append("---------------------------")
        return "\n".join(history)

if __name__ == "__main__":
    # Create an account
    my_account = BankAccount("123456789", "Alice Smith", 1000.00)
    print(my_account.get_summary())
    print("\n")

    # Perform some transactions
    success, message = my_account.deposit(500.00)
    print(message)
    print(my_account.get_summary())
    print("\n")

    success, message = my_account.withdraw(200.00)
    print(message)
    print(my_account.get_summary())
    print("\n")

    # Attempt to withdraw more than available
    success, message = my_account.withdraw(1500.00)
    print(message)
    print(my_account.get_summary())
    print("\n")

    # Attempt invalid deposit
    success, message = my_account.deposit(-100.00)
    print(message)
    print("\n")

    # Attempt invalid withdrawal
    success, message = my_account.withdraw(0)
    print(message)
    print("\n")

    # Display transaction history
    print(my_account.get_transaction_history())
    print("\n")

    # Another account
    bob_account = BankAccount("987654321", "Bob Johnson")
    print(bob_account.get_summary())
    bob_account.deposit(75.50)
    bob_account.withdraw(25.00)
    print(bob_account.get_summary())
    print(bob_account.get_transaction_history())
    print("\n")

    # Account with zero initial balance
    zero_account = BankAccount("000000001", "Charlie Brown", 0.0)
    print(zero_account.get_summary())
    zero_account.deposit(10.00)
    print(zero_account.get_summary())
    print(zero_account.get_transaction_history())