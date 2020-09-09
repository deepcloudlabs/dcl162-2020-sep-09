from banking.domain import Account, InsufficientBalance

try:
    account1 = Account("tr1", 10000)
    print(f"balance: {account1.balance}")
    account1.deposit(2500)
    print(f"balance: {account1.balance}")
    account1.withdraw(7500)
    print(f"balance: {account1.balance}")
    account1.withdraw(3500)
    print(f"balance: {account1.balance}")
    account1.withdraw(5000)
    print(f"balance: {account1.balance}")
except ValueError as err:
    print(err)
except InsufficientBalance as err:
    print(f"{err.message}: deficit= {err.deficit}")
