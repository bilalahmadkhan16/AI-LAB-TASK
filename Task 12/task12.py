import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

import matplotlib.pyplot as plt

#data set titanic
df = pd.read_csv("titanic.csv")

if 'Age' in df.columns:
    avg = df['Age'].mean()
    df['Age'] = df['Age'].fillna(avg)

if 'Embarked' in df.columns:
    common = df['Embarked'].mode()[0]
    df['Embarked'] = df['Embarked'].fillna(common)

if 'Cabin' in df.columns:
    df.drop('Cabin', axis=1, inplace=True)

obj_cols = df.select_dtypes(include=['object']).columns

for col in obj_cols:
    df[col] = pd.factorize(df[col])[0]


X = df.drop('Survived', axis=1)
y = df['Survived']

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2)

model_list = []
model_list.append(("LR", LogisticRegression(max_iter=200)))
model_list.append(("RF", RandomForestClassifier()))
model_list.append(("NB", GaussianNB()))
model_list.append(("DT", DecisionTreeClassifier()))
model_list.append(("KNN", KNeighborsClassifier()))

results = {}
names = []
values = []

for name, model in model_list:
    model.fit(X_tr, y_tr)
    pred = model.predict(X_te)
    
    score = accuracy_score(y_te, pred)
    
    print(name, "accuracy:", score)
    
    results[name] = score
    names.append(name)
    values.append(score)

#graph line
plt.figure()
plt.plot(names, values, marker='o')
plt.title("Accuracy comparison")
plt.xlabel("Models")
plt.ylabel("Score")
plt.xticks(rotation=25)
plt.show()
#graph bar
plt.figure()
plt.bar(names, values)
plt.title("Accuracy bar chart")
plt.xlabel("Models")
plt.ylabel("Score")
plt.xticks(rotation=25)
plt.show()