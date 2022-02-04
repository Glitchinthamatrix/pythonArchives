from sklearn.datasets import load_breast_cancer
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score 
from sklearn.preprocessing import scale 
import pandas as pd 


bc=load_breast_cancer()
x=bc.data
y=bc.target

x_test,x_train,y_test,y_train=train_test_split(x,y,test_size=0.2)
model=KMeans(n_clusters=2,random_state=0)

model.fit(x_train)
predictions=model.predict(x_test)
labels=model.labels_
print("accuracy: ",accuracy_score(y_test,predictions))