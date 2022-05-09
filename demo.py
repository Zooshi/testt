import pandas as pd

df =pd.read_csv("customers.csv")
print(df.head())
print('done')
assert 5 == 5