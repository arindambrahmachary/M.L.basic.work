# -*- coding: utf-8 -*-
"""knn2.ZOO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BYm8LS8uptX2CVVUkAsCLBZ2T7NzaPcP
"""

from google.colab import files

uploaded = files.upload()

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
df=pd.read_csv("Zoo.csv")
df

df.info()

df.isnull().sum()

sns.boxplot(df)
#very few out liers are their we will keep this thing

# Define the lower and upper bounds for clipping and capping
#lower_bound = X.quantile(0.25)
#upper_bound = X.quantile(0.75)

# Loop through each column (X variable) in the DataFrame
#for col in X.columns:
    #Clip and cap the data for each column
    #X[col] = np.clip(X[col], lower_bound[col], upper_bound[col])

"""i am working with this little outliers , if we want  to remove the outliers then we can run the above code

"""

df.describe()

df.isnull().sum()

df.hist()

Z=df.corr().values
Z= pd.DataFrame(Z)
Z.Columns=list(df)
Z

X= df.iloc[:, 1:17]
X

Y=df.iloc[:,-1]
Y

#data transformation
from sklearn.preprocessing import StandardScaler
SS = StandardScaler()
SS_X = SS.fit_transform(X)
SS_X = pd.DataFrame(SS_X)
SS_X.columns = list(X)
SS_X.head()

sns.boxplot(SS_X)

# Data partition
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test= train_test_split(SS_X,Y,test_size=0.3)

#model fitting with knn

from sklearn.neighbors import KNeighborsClassifier
KNN= KNeighborsClassifier(n_neighbors=5)

training_accuracies = []
test_accuracies = []

from sklearn.metrics import accuracy_score
for i in range(1,101):
    X_train,X_test,Y_train,Y_test = train_test_split(SS_X,Y, test_size=0.3, random_state=i)
    KNN.fit(X_train,Y_train)
    Y_pred_train  = KNN.predict(X_train)
    Y_pred_test   = KNN.predict(X_test)
    training_accuracies.append(accuracy_score(Y_train,Y_pred_train))
    test_accuracies.append(accuracy_score(Y_test,Y_pred_test))

print("Cross validation Training Accuracy: ",np.mean(training_accuracies).round(2))
print("Cross validation Test Accuracy: ",np.mean(test_accuracies).round(2))

#model fitting with knn

from sklearn.neighbors import KNeighborsClassifier
KNN= KNeighborsClassifier(n_neighbors=7)

training_accuracies = []
test_accuracies = []

from sklearn.metrics import accuracy_score
for i in range(1,101):
    X_train,X_test,Y_train,Y_test = train_test_split(SS_X,Y, test_size=0.3, random_state=i)
    KNN.fit(X_train,Y_train)
    Y_pred_train  = KNN.predict(X_train)
    Y_pred_test   = KNN.predict(X_test)
    training_accuracies.append(accuracy_score(Y_train,Y_pred_train))
    test_accuracies.append(accuracy_score(Y_test,Y_pred_test))

print("Cross validation Training Accuracy: ",np.mean(training_accuracies).round(2))
print("Cross validation Test Accuracy: ",np.mean(test_accuracies).round(2))

#model fitting with knn

from sklearn.neighbors import KNeighborsClassifier
KNN= KNeighborsClassifier(n_neighbors=9)

training_accuracies = []
test_accuracies = []

from sklearn.metrics import accuracy_score
for i in range(1,101):
    X_train,X_test,Y_train,Y_test = train_test_split(SS_X,Y, test_size=0.3, random_state=i)
    KNN.fit(X_train,Y_train)
    Y_pred_train  = KNN.predict(X_train)
    Y_pred_test   = KNN.predict(X_test)
    training_accuracies.append(accuracy_score(Y_train,Y_pred_train))
    test_accuracies.append(accuracy_score(Y_test,Y_pred_test))

print("Cross validation Training Accuracy: ",np.mean(training_accuracies).round(2))
print("Cross validation Test Accuracy: ",np.mean(test_accuracies).round(2))

#model fitting with knn

from sklearn.neighbors import KNeighborsClassifier
KNN= KNeighborsClassifier(n_neighbors=11)

training_accuracies = []
test_accuracies = []

from sklearn.metrics import accuracy_score
for i in range(1,101):
    X_train,X_test,Y_train,Y_test = train_test_split(SS_X,Y, test_size=0.3, random_state=i)
    KNN.fit(X_train,Y_train)
    Y_pred_train  = KNN.predict(X_train)
    Y_pred_test   = KNN.predict(X_test)
    training_accuracies.append(accuracy_score(Y_train,Y_pred_train))
    test_accuracies.append(accuracy_score(Y_test,Y_pred_test))

print("Cross validation Training Accuracy: ",np.mean(training_accuracies).round(2))
print("Cross validation Test Accuracy: ",np.mean(test_accuracies).round(2))

"""i checked with the different k values  after 5 when i tried  it' againg decresing its trainging accuracy and test accuracy as well, that's why i sttoped my  testing here"""

pd.crosstab(Y_test,Y_pred_test) # getting the 2 way table to understand the correct and wrong predictions



#di this hyperperemeter tuning to get the best value
from sklearn.model_selection import GridSearchCV
n_neighbors = np.array(range(1,15))
param_grid = dict(n_neighbors=n_neighbors)
KNN = KNeighborsClassifier()
grid = GridSearchCV(estimator=KNN, param_grid=param_grid)
grid.fit(X, Y)
print(grid.best_score_)
print(grid.best_params_)





