import json

with open("accounts.json", "rt") as f:
    bank_accounts = json.load(f)
    print(bank_accounts)
