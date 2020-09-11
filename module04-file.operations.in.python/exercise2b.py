import pickle

with open("accounts.pkl", mode="rb") as f:
    bank_accounts = pickle.load(f)
    print(bank_accounts)
