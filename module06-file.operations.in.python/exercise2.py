with open("accounts.txt", mode="rt") as accounts:
    for account in accounts:
        iban, fullname, balance = account.split(",")
        print(f"{iban}\t{fullname}\t{balance}")
