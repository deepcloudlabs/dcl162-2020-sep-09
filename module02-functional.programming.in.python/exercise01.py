from functools import reduce
from operator import add

from banking.domain import Account, CheckingAccount

accounts = [  # heterogeneous list
    Account("tr1", 10000),
    CheckingAccount("tr2", 20000, 1000),
    Account("tr3", 30000),
    CheckingAccount("tr4", 40000, 10000),
    Account("tr5", 50000)
]
total_balance = 0
for acc in accounts:  # external loop
    if isinstance(acc, CheckingAccount):
        total_balance += acc.balance
print(f"Total Balance in Checking Account's: {total_balance}")

x = 42
y = False
name = "jack"
acc = Account("tr6", 600000)

if_checking_account = lambda acc: isinstance(acc, CheckingAccount)
checking_accounts = list(filter(if_checking_account, accounts))
for acc in checking_accounts:
    print(acc)

balances = list(map(lambda a: a.balance, filter(if_checking_account, accounts)))
for bal in balances:
    print(bal)

# Filter/Map/Reduce: Hadoop ( HDFS + MapReduce )
to_balance = lambda a: a.balance
total_balance = reduce(add, map(to_balance, filter(if_checking_account, accounts)), 0)
print(f"Total Balance: {total_balance}")
