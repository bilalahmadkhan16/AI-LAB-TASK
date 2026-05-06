import pandas as pd
data = pd.read_csv("titanic.csv")
print("First 5 rows:")
print(data.head())
print("\nLast 5 rows:")
print(data.tail())

rows = data.shape[0]
cols = data.shape[1]

print("\nTotal Rows:", rows)
print("Total Columns:", cols)

print("\nMissing values in dataset:")
print(data.isnull().sum())
#fil with mean
data1 = data.fillna(data.mean(numeric_only=True))

#fil with median
data2 = data.fillna(data.median(numeric_only=True))

#fil with mode
data3 = data.fillna(data.mode().iloc[0])

print("\nMissing values ko mean, median aur mode se fill kar diya.")
#dataa type chck
print("\nColumn data types:")
print(data.dtypes)