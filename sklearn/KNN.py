#KNN - K nearest neighbor where k is an integer, this classification method takes a data-point and classifies it 
# by the proximity it has with other K data points, if K nearest data-points are of class A, the given data-point 
#will be classified as A an
#1] uniform KNN: all the K data-poinsts will hold equal importance 
#2] distanec KNN: the nearest data-points will hold more importance than the farther ones, because proximity is the factor
#by which we classify the data 

import numpy as np
import pandas as pd
from sklearn import neighbors, metrics 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import LabelEncoder 

data=pd.read_csv('sklearn\car.data')

x=data[['buying','maint','safety']].values
y=data[['class']]
Le=LabelEncoder()

#converting the data in x
for i in range(len(x[0])):
    x[:,i]=Le.fit_transform(x[:,i])

label_mapping={
    'unacc':0,
    'acc':1,
    'good':2,
    'vgood':3
}   
y['class']=y['class'].map(label_mapping)
y=np.array(y)


knn=neighbors.KNeighborsClassifier(n_neighbors=25,weights="uniform")
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
knn.fit(x_train,y_train)
predictions=knn.predict(x_test)
accuracy=metrics.accuracy_score(y_test,predictions)
print(f"accuracy is {accuracy}")
print(f"testing the accuract")
print(f"actual value: {y[1727]}, predicted: {knn.predict(x)[1727]}")
