import pandas as pd

df = pd.DataFrame([
    ["tr1", "jack bauer", 100000],
    ["tr2", "kate austen", 200000],
    ["tr3", "jin kwon", 300000],
    ["tr4", "sun kwon", 400000]
] , columns=["iban", "full name", "balance"])

df.to_csv("bank_accounts.csv")