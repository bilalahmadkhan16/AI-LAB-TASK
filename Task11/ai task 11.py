import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")

print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])

#chck nul vlues
print("\nMissing values:")
print(df.isnull().sum())

print("\nSex column ke values:")
print(df['Sex'].unique())

if 'Embarked' in df.columns:
    most_common = df['Embarked'].mode()[0]
    df['Embarked'] = df['Embarked'].fillna(most_common)

# Age
if 'Age' in df.columns:
    avg_age = df['Age'].mean()
    df['Age'] = df['Age'].fillna(avg_age)
#chnge dataa type
if 'Age' in df.columns:
    df['Age'] = df['Age'].astype(int)
#remove more colums
if 'Cabin' in df.columns:
    df.drop('Cabin', axis=1, inplace=True)

#chckdata tyypes
print("\nUpdated data types:")
print(df.dtypes)


X = df.iloc[:, :-1]
y = df.iloc[:, -1]

print("\nX shape:", X.shape)
print("y shape:", y.shape)

cols = X.select_dtypes(include=['object']).columns

for c in cols:
    X[c] = pd.factorize(X[c])[0]

print("\nAfter converting categorical data:")
print(X.head())