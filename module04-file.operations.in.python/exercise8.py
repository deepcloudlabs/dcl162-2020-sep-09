import pandas as pd

df = pd.read_csv('accounts.csv')
print(df.index)
print(df.columns)
print(df)