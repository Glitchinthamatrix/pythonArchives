import matplotlib.pyplot as plt 
import numpy as np 

x=[i for i in range(20)]
y=np.random.randint(0,10,size=(20))
plt.xlabel("x-axis")
plt.ylabel("y-axis")

#linegraph 
# plt.plt(x,y)


#scatter graph
plt.scatter(x,y)



plt.show()