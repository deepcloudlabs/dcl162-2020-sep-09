class InsufficientBalance(Exception):
    def __init__(self, deficit):
        self.deficit = deficit


class Account:
    def __init__(self, iban, balance):
        self._iban = iban
        self._balance = balance

    @property
    def iban(self):
        return self._iban

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self._balance:
            raise InsufficientBalance(amount - self._balance)
        self._balance -= amount


class CheckingAccount(Account):
    def __init__(self, iban, balance, overdraft_amount):
        pass
