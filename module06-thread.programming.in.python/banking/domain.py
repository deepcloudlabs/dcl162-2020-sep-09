from enum import Enum
from threading import Lock


class InsufficientBalance(Exception):
    def __init__(self, message, deficit):
        self.message = message
        self.deficit = deficit


class AccountStatus(Enum):
    CLOSED = 100
    ACTIVE = 200
    BLOCKED = 300


"""
    Account is a domain (analysis) class
    Account is an entity class => class with identity
"""


class Account:  # Thread-safe Account
    def __init__(self, iban, balance=10, status=AccountStatus.ACTIVE):
        self._iban = iban
        self._balance = balance
        self._status = status
        self.lck = Lock()

    # iban -> property : read-write
    @property
    def iban(self):
        with self.lck:
            return self._iban

    @property  # read-only property
    def balance(self):
        with self.lck:
            print("def balance(self) is running...")
            return self._balance

    @iban.setter
    def iban(self, iban):
        with self.lck:
            self._iban = iban

    @property
    def status(self):
        with self.lck:
            return self._status

    @status.setter
    def status(self, status):
        with self.lck:
            self._status = status

    def deposit(self, amount=5):
        with self.lck:
            if amount <= 0:  # validation
                raise ValueError("amount must be positive")
            if self._status == AccountStatus.ACTIVE:
                self._balance = self._balance + amount

    def withdraw(self, amount):
        with self.lck:
            print("Account::withdraw() is running...")
            if amount <= 0:  # validation
                raise ValueError("amount must be positive")
            if amount > self._balance:  # business rule
                raise InsufficientBalance("your balance does not cover your expenses", amount - self._balance)
            if self._status == AccountStatus.ACTIVE:
                self._balance = self._balance - amount

    def __str__(self):  # str(x)
        with self.lck:
            return f"Account [iban: {self.iban}, balance: {self.balance}, status: {self.status}]"

    def __repr__(self):  # repr(x)
        with self.lck:
            return self._iban


"""
CheckingAccount : Derived Class, Sub-class
Account         : Base Class, Super-class
"""


class CheckingAccount(Account):
    def __init__(self, iban, balance, overdraft_amount=500):
        super().__init__(iban, balance)  # calls super class' constructor (__init__)
        self._overdraft_amount = overdraft_amount

    @property
    def overdraft_amount(self):
        with self.lck:
            return self._overdraft_amount

    # overriding
    def withdraw(self, amount):
        with self.lck:
            print("CheckingAccount::withdraw() is running...")
            if amount <= 0:  # validation
                raise ValueError("amount must be positive")
            if amount > (self.balance + self._overdraft_amount):  # business rule
                raise InsufficientBalance("your balance does not cover your expenses",
                                          amount - self.balance - self._overdraft_amount)
            self._balance = self.balance - amount

    # overriding
    def __str__(self):  # str(x)
        with self.lck:
            return f"CheckingAccount [iban: {self.iban}, balance: {self.balance}, status: {self.status}, overdraftAmount: {self.overdraft_amount}]"
