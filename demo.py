import pandas as pd
from flask import Flask

app =  Flask()
df =pd.read_csv("customers.csv")
print(df.head())
print('done')
assert 7==7

#second branch does different things