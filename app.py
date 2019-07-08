# -*- coding: utf-8 -*-
#Simple Linear Regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing the Datasets
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 1].values

#Splitting the Dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y , test_size = 1/3,random_state = 0)

#Feature Scaling -- Not needed python libraries will take care of it.

#Fiting Simple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predicting the Test Set Results
y_pred = regressor.predict(X_test)

# Visualizing the Training Set Results.
plt.scatter(X_train, Y_train, color = 'red')                    # Real Values
plt.plot(X_train, regressor.predict(X_train) , color = 'blue')  # predicted Values
plt.title('Salary Vs Experience(Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
# Visualizing the Test Set Results.
plt.scatter(X_test, Y_test, color = 'red')                    # Real Values
plt.plot(X_train, regressor.predict(X_train) , color = 'blue')  # predicted Values
plt.title('Salary Vs Experience(Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
