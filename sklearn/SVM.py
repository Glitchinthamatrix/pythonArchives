#SVM: support vector machine
#effective in high-dimensional spaces, meaning it works well for data-sets having many features
#used for classification and regression
#it creates a line dividing the classes and it makes the line with the help of support vectors, support vectors are the data-points closer to the line, the line is drawn such that 
#the distance between the line and the support vectors on both sides is the same

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import datasets 
from sklearn.metrics import accuracy_score 


iris=datasets.load_iris()
x=iris.data
y=iris.target

classes=['Iris Setosa','Iris Versicolour','Iris Virginica']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

model=svm.SVC()

model.fit(x_train,y_train)
predictions=model.predict(x_test)
print(f"accuracy is {accuracy_score(y_test,predictions)*100}%")
for i in range(len(y)):
    prediction=model.predict(x)[i]
    print(f"actual value: {y[i]}, predicted: {prediction}, it is a {classes[prediction]}")
   