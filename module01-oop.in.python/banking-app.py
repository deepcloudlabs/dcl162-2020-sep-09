from banking.domain import Account, InsufficientBalance

try:
    account1 = Account("tr1", 10000)
    account1.iban = "tr2"
    print(str(account1))
    account1.deposit(2500)
    print(repr(account1))
    account1.withdraw(7500)
    print(account1)
    account1.withdraw(3500)
    print(account1)
    account1.withdraw(5000)
    print(account1)
except ValueError as err:
    print(err)
except InsufficientBalance as err:
    print(f"{err.message}: deficit= {err.deficit}")