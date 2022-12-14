# -*- coding: utf-8 -*-
"""Titanic Disaster.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pFqA_LQV2kr0TdHpKMBFsRau7GWDK7ug

**Predict the survival on the titanic disaster Project**
"""

import pandas as pd

data = pd.read_csv('/content/train.csv')
data

data.shape

data.info()

data.isnull().sum()

# Dropping the cabin column

modified_data = data.drop(['Cabin','PassengerId','Ticket'],axis =1)
modified_data

data.shape

modified_data.shape

modified_data.info()

modified_data.isnull().sum()

#  removing the rows that contains NULL values

modified_data = modified_data.dropna()
modified_data

modified_data.isnull().sum()

# converting the text or object into numerical values

gender = pd.get_dummies(modified_data['Sex'])
gender

Embarked = pd.get_dummies(modified_data['Embarked'])
Embarked

a = pd.concat([modified_data,gender,Embarked],axis =1)
a

data_1 = a.drop(['Sex','Embarked','Name'],axis = 1)
data_1

y = data_1.iloc[ : ,0].values
y

y.ndim

type(y)

x = data_1.iloc[ : ,1: ].values
x

x.ndim

type(x)

import seaborn as sns
sns.displot(data_1['Age'])

sns.distplot(data_1['male'])

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0)

# importing the logistic regression algorithm

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(x_train,y_train)

y_predict = model.predict(x_test)
y_predict

y_test

from sklearn.preprocessing import MinMaxScaler

scale = MinMaxScaler()

x_train = scale.fit_transform(x_train)

x_train

x_test = scale.transform(x_test)

x_test

model = LogisticRegression()

model.fit(x_train,y_train)

y_pred = model.predict(x_test)
y_pred

from sklearn.metrics import accuracy_score

# when I applied trian test split and compare the y_test with the y_pred(with scaling and normalization),the accuarcy score is 0.6292134831460674

accuracy_score(y_test,y_pred)

# But when I compare the accuracy_score with y_test with y_predict(without scaling or normalization) it gives 0.7808988764044944 as the accuracy

accuracy_score(y_test,y_predict)

import matplotlib.pyplot as plt

import seaborn as sns

sns.displot(data_1['Age'])

sns.displot(data_1['Pclass'],kind = 'hist') 
# 'hist', 'kde', 'ecdf'

data_1['Age'].plot(figsize = (25,8))

sns.regplot(x = 'male',y='Pclass',data=data_1)
plt.figure(figsize=(20,10))

sns.regplot(x = 'female',y='Pclass',data=data_1)
plt.figure(figsize=(20,10))

sns.regplot(x = 'male',y='Age',data=data_1)
plt.figure(figsize=(20,10))

sns.distplot(data_1['Pclass'])
plt.show()

age = data_1.iloc[:,2]
age

Pclass= data_1.iloc[:,1]
Pclass

plt.plot(age,Pclass)

df1 = pd.DataFrame({'Actual':age,'Predicted':Pclass})
df1

df1.plot(figsize=(20,8),kind = 'bar')

male = data_1.iloc[:,7]
male

df1 = pd.DataFrame({'Actual':age,'Predicted':male})
df1

df1 = pd.DataFrame({'Actual':y_test,'Predicted':y_predict})
df1

df1.plot(figsize =(12,6),kind ='bar')

df1 = pd.DataFrame({'Actual':y_predict,'Predicted':y_pred})
df1

df1.plot(figsize = (14,5))