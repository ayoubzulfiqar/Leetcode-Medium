class Bank:
    def __init__(self, balance: list[int]):
        self.balance = balance
        self.n = len(balance)

    def _is_valid_account(self, account: int) -> bool:
        return 1 <= account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._is_valid_account(account1) or not self._is_valid_account(account2):
            return False
        
        idx1 = account1 - 1
        idx2 = account2 - 1

        if self.balance[idx1] < money:
            return False
        
        self.balance[idx1] -= money
        self.balance[idx2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account):
            return False
        
        idx = account - 1
        self.balance[idx] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account):
            return False
        
        idx = account - 1
        if self.balance[idx] < money:
            return False
        
        self.balance[idx] -= money
        return True