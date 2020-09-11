import json

bank_accounts = [
    {"iban": "tr1", "fullname": "jack bauer", "salary": 100000, "address": { "city": "ankara", "zip_code": 34444}},
    {"iban": "tr2", "fullname": "kate austen", "salary": 200000},
    {"iban": "tr3", "fullname": "jin kwon", "salary": 300000},
    {"iban": "tr4", "fullname": "sun kwon", "salary": 400000}
]

with open("accounts.json", "wt") as f:
    json.dump(bank_accounts, f)
