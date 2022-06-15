import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

train = pd.read_csv("train.csv")

print(train.head())

print(train.count())

print(sns.countplot(x='Survived', hue='Pclass', data=train))


# data wrangling

def add_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        return int(train[train["Pclass"] == Pclass]["Age"].mean())
    else:
        return Age

train["Age"] = train[["Age", "Pclass"]].apply(add_age,axis=1)

train.drop("Cabin", inplace=True, axis=1)
train.dropna(inplace=True)
"""

embarked = pd.get_dummies(train["Embarked"], drop_first=True)
embarked = pd.get_dummies(train["Pclass"], drop_first=True)
train.drop(["PassengerId","Pclass","Name","Sex","Ticket","Embarked"], axis=1, inplace=True)

x = train.drop("Survived", axis=1)
y = train["Survived"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101 )

from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)


predictions = logmodel.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test, predictions))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, predictions))

"""
# commented on purpose

"""
1. Find servived passengers when Pclass = 1 and Genger = Male
2.  "" when age>40 & sibsp = 0
3. count no of family member travelling together 
4. when Pclass=3 & gender = Female & age <12
5. Improve your confusion matrix by parameter re-engineering
7:33
"""

# db_read = pd.read_csv("train.csv")

# def missing_age(cols):
#     Age = cols[0]
#     Pclass = cols[1]
#     if pd.isnull(Age):
#         return int(train[train["Pclass"] == Pclass]["Age"].mean())
#     else:
#         return Age

# db_read["Age"] = db_read[["Age", "Pclass"]].apply(missing_age,axis=1)

db_read = train

# for que 1
interestedrows_1 = db_read.loc[db_read["Survived"] == 1]
interestedrows_1 = interestedrows_1[interestedrows_1["Sex"] == "male"]
interestedrows_1 = interestedrows_1[interestedrows_1["Pclass"] == 1]
print(interestedrows_1["Survived"].value_counts())

# for que 2
interestedrows_2 = db_read.loc[db_read["Survived"] == 1]
interestedrows_2 = interestedrows_2[interestedrows_2["Age"] > 40]
interestedrows_2 = interestedrows_2[interestedrows_2["SibSp"] == 0]
print(interestedrows_2["Survived"].value_counts())

interestedrows_2_2 = db_read[(db_read["Survived"] == 1) & (db_read["SibSp"] == 0) & (db_read["Age"] > 40)]
print("Compare: ", interestedrows_2_2["Survived"].count())


# for que 3
family_members = pd.DataFrame()
family_members["Members"] = db_read["SibSp"] + db_read["Parch"] + 1
print(sns.countplot(x = 'Members', data = family_members))
print(family_members)


# for que 4
interestedrows_4 = db_read.loc[(db_read["Survived"] == 1) & (db_read["Pclass"] == 3) & (db_read["Sex"] == "female") & (db_read["Age"] < 12)]
# interestedrows_4 = interestedrows_4[interestedrows_4["Pclass"] == 3]
# interestedrows_4 = interestedrows_4[interestedrows_4["Sex"] == "female"]
# interestedrows_4 = interestedrows_4[interestedrows_4["Age"] < 12]
print(interestedrows_4["Survived"].value_counts())

# for que 5
