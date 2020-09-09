from banking.domain import Account

accounts = [
    Account("tr1", 10000),
    Account("tr2", 20000),
    Account("tr3", 30000),
    Account("tr4", 40000),
    Account("tr5", 50000)
]

total_balance = 0
for account in accounts:
    account.withdraw(10)  # withdraw(account, 10)
    total_balance += account.balance
print(f"Total balance: {total_balance}")
