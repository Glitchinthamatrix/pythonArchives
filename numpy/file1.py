import numpy as np

#initialise an array of ints
# ints=np.array([1,2,3])
# print(ints)

#initialise an array of floats
# floats=np.array([1.2,30.4])
# print(floats)

#if you initialise an array with ints and floats both, it'll take the ints as floats
# intsandfloats=np.array([2,4.5,2,2.4])
# print(intsandfloats)

#2-dimensional array, however the below method is deprecated
# twodim=np.array([[2.0,3.0,3.0,2.0],[2.0,3.0,4.0]])
# print(twodim.ndim)


#this is the right method for initialising a multidimensional array, declare and define it inside a function
# def foo():
#     twodim=np.array([[3,3,3],[3,3,3]])
#     print(twodim)
#     return twodim.ndim
# print(f"how many dimensions in foo? => {foo()}") 


#get the number of dimensions and shape of arrays
# def foo():
#     arr=np.array([[2,2,2],[3,3,3]])
#     print(f"number of dimensions: {arr.ndim}")
#     print(f"shape of the array: {arr.shape}")
# foo()    


#get the data-type of array elements
# arr=np.array([3,3,3])
#or
# arr=np.array([3,3,3],dtype="int8")
# print(arr.dtype)


#get the size of array items or the whole array in bytes
# arr=np.array([3,3,3],dtype="int16")
# print(f"the item size is: {arr.itemsize}")
# print(f"the size of whole array is: {arr.nbytes}")


#get a specifc item
# arr=np.array([[3,3,3,3,3,3,3,3],[4,4,4,6,4,4,4,4],[5,5,5,5,5,5,5,5]])
# #to get 6 type 
# print(arr[1,3])#index starts from 0


#get a specific row    
# arr=np.array([[3,3,3,3,3,3,3,3],[4,4,4,6,4,4,4,4],[5,5,5,5,5,5,5,5]])
#to get 2nd type 
# print(arr[1,:])#index starts from 0


#get a column  
# arr=np.array([[3,3,3,3,3,3,3,3],[4,4,4,6,4,4,4,4],[5,5,5,5,5,5,5,5]])
# # to get 2nd type 
# print(arr[:,3])#gets the 4th item from all arrays, array[row,column]


#getting a lil fancy, get items at a distance of some steps, basic array traversal
# arr=np.array([[3,4,5,6,7,8,9,10],[4,5,6,7,8,9,10,11],[5,6,7,8,9,10,11,12]])
# print(arr[:,1:6:2]) #gives 2nd 4th and 6th items form all rows,specify the row to get items from that row only


#set values just like you set array values
# arr=np.array([[3,4,5,6,7,8,9,10],[4,5,6,7,8,9,10,11],[5,6,7,8,9,10,11,12]])
# arr[1,4] = 20 #sets the 5th value in second row to 20
# print(arr)


#replace a row
# arr=np.array([[3,4,5,6,7,8,9,10],[4,5,6,7,8,9,10,11],[5,6,7,8,9,10,11,12]])
# arr[0,:]=5 #replaces the first row with 5s
# print(arr)

# arr[:,0]=6 #replaces the first column with 6s
# print(arr)

# arr[0,:]=[1,2,3,4,5,6,7,8] #replaces the first row with the specified array, provide an array with the same length as the the preexisiting array
# print(arr)

# arr[:,1]=[1,2,3]#replace the second column with this array
# print(arr)



#a tridimensional array, gets confiusing as dimensions increase
# arr=np.array([[[1,2],[3,4],[5,6],[7,8]],[[9,10],[11,12],[13,14],[15,16]]])
# arr[0,1,1]=166
# print(arr)



#intialise different arrays
# arr=np.zeros(5) #initialises a 5-item array of zeros 
# print(arr)

#for complex shapes, double parentheses
# arr=np.ones((3,4)) #initialises a 2-dimnesional array of ones 
# print(arr)


#for complex shapes, double parentheses
# arr=np.ones((3,4),dtype="int8") #initialises a 2-dimnesional array of ones that take 9 bits of memory
# print(arr)
# print(f"item size is {arr.itemsize}")


#for items other than 0 and 1
# arr=np.full((5),88,dtype="int8") #np.full((length),value,datatype)
# print(arr)


#take the shape of another array and create an array like it
# arr=np.array([[3,4,5,6,7,8,9,10],[4,5,6,7,8,9,10,11],[5,6,7,8,9,10,11,12]])
# arr2=np.full_like(arr,5)
# print(arr2)

# or can do the same thing with the full method
# arr2=np.full(arr.shape,4)
# print(arr2)



#initialise an array with random numbers
# arr=np.random.rand(3,2) #np.random.rand(row,column)
# print(arr)


#initialise an array with random floats, copying the shape of another array
# arr=np.array([[3,4,5,6,7,8,9,10],[4,5,6,7,8,9,10,11],[5,6,7,8,9,10,11,12]])
# arr=np.random.random_sample(arr.shape) #np.random.rand(row,column)
# print(arr)


#initialise an array with random integers, copying the shape of another array
# arr=np.array([[3,4,5,6,7,8,9,10],[4,5,6,7,8,9,10,11],[5,6,7,8,9,10,11,12]])
# arr=np.random.randint(1,7,size=(3,4)) #np.random.randint(lowest_value,highest_value,size, actually shape)
# print(arr)


#create an identity matrix
# arr=np.identity(5) #creates an identity matrix of floats, identity matrices have the same number of rows and dcolumns
# print(arr)



#make arrays by repitition of some values
# sample_arr=np.array([[1,2,3]]) #repeats the inner part
# arr=np.repeat(sample_arr,3,axis=0) #np.repeat(sample_arr,no_of_times_to_copy,axis=how the repititon would look like)
# print(arr)


#printing an array like this
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1
#the hard way
# arr=np.random.randint(0,2,size=(5,5))
# arr[0,:]=1 #first row of every column
# arr[4,:]=1 #last row of every column
# arr[:,0]=1 #first column of every row
# arr[:,4]=1 #last column of every row
# arr[1,1:4]=0 #in second row, from second to 4th column
# arr[3,1:4]=0 #in 4th row, from 1st to 4th column
# arr[1:4,1]=0 #from second row to 4th row, in second column
# arr[2,2]=9
# print(arr)
#the easy way
# ones=np.ones((5,5))
# zeros=np.zeros((3,3))
# zeros[1,1]=9
# ones[1:-1,1:-1]=zeros
# print(ones)



#if you copy arrays, dont do it like this=> a=array; b=a;, as arays are passed by reference, which means if you chnage b , a also changes, instead use the method copy to copy arrays
# a=np.array([2,2,2,3])
# b=a.copy()
# b[1]=33
# print(b)
# print(a)


#---mathematics-----
#arithmetic operations are done to each item in the array
# a=np.array([1,2,3])
# # print(a+1) #addas one to each element
# print(a/(1/2)) #divides each element by 0.5


#operations with two arrays
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# print(b//a)
# print(a+b)
# print(a*b)
# print(a**b)



#get trigonometric values of array items
# arr=np.array([1,2,3])
# sins=np.sin(arr)
# coss=np.cos(arr)
# tans=np.tan(arr)
# print(tans)



#
