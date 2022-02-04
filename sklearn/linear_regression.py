from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import matplotlib.pyplot as plt

boston=datasets.load_boston()
x=boston.data 
y=boston.target

lreg_model=linear_model.LinearRegression()

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model=lreg_model.fit(x_train,y_train)
predictions=model.predict(x_test)
print(f"r2 value: {lreg_model.score(x,y)}")
print(f"coefficient factor: {lreg_model.coef_}")