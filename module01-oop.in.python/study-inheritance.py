from banking.domain import CheckingAccount, InsufficientBalance

try:
    acc1 = CheckingAccount("tr1", 10000, 2500)
    acc1.withdraw(10000)
    print(acc1)
    acc1.withdraw(2500)
    print(acc1)
    acc1.withdraw(1)
except ValueError as err:
    print(err)
except InsufficientBalance as err:
    print(f"{err.message}: deficit= {err.deficit}")

