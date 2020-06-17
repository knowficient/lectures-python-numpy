import numpy as np

# create 2D array
a  = np.array([[1,2,3],[4,5,6]])

# returns class type of array
print("Class Types = ",type(a))

# returns the shape of array
print("Shape of a = ",a.shape)

# return value of array
print("Value of a[0,1] = ",a[0,1])

# change value of array
a[0,1] = 9
print("The array a = ",a)

# returns the size of array
print("The size of a = ",a.size)

#return datatype of array
print("The datatype of a[0,1] = ",np.dtype(a[0,1]))