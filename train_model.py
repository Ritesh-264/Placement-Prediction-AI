import pandas as pd
data = pd.read_csv("students.csv")
print(data.head())
print(data.shape)
print(data.columns)
print(data.dtypes)
print(data.describe())