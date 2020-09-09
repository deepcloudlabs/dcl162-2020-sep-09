from random import random

from banking.domain import Account, CheckingAccount

account = None
if random() < 0.5:
    print("Head")
    account = Account("tr1", 10000)
else:
    print("Tail")
    account = CheckingAccount("tr2", 20000, 5000)

account.withdraw(10)
print(account)