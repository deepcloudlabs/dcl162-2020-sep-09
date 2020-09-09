from banking.domain import Account, CheckingAccount

accounts = [ # heterogeneous list
    Account("tr1", 10000),
    CheckingAccount("tr2", 20000, 1000),
    Account("tr3", 30000),
    CheckingAccount("tr4", 40000, 10000),
    Account("tr5", 50000)
]


def get_total_balance(accs):  # generic function
    total_balance = 0
    for account in accs:
        account.withdraw(1)  # withdraw(account, 10)
        total_balance += account.balance
    return total_balance


print(f"Total balance: {get_total_balance(accounts)}")
