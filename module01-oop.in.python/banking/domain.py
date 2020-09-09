class InsufficientBalance(Exception):
    def __init__(self, message, deficit):
        self.message = message
        self.deficit = deficit

"""
    Account is a domain (analysis) class
    Account is an entity class => class with identity
"""
class Account:
    def __init__(self, iban, balance=10):
        self.iban = iban
        self.balance = balance

    def deposit(self, amount=5):
        if amount <= 0:  # validation
            raise ValueError("amount must be positive")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= 0:  # validation
            raise ValueError("amount must be positive")
        if amount > self.balance:  # business rule
            raise InsufficientBalance("your balance does not cover your expenses", amount - self.balance)
        self.balance = self.balance - amount
