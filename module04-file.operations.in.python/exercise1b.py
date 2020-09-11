import pickle

bank_accounts = [
    ["tr1", "jack bauer", 100000],
    ["tr2", "kate austen", 200000],
    ["tr3", "jin kwon", 300000],
    ["tr4", "sun kwon", 400000]
]
with open("accounts.pkl", mode="wb") as f:
    pickle.dump(bank_accounts, f)
