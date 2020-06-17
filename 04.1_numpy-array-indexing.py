import numpy as np

# create 2D array
a  = np.array([[1,2,3],[4,5,6],[7,8,9]])

# slicing array
p = a[1:3,:2]
print("Slicing p = a[1:3,:2] = ",p)

# change p array
p[1,1]= 50
print("Change p[1,1]=50, values of a = ", a)

# create an array [0,2],[1,1],[2,0] from a
print("New array by indexing a[[0,1,2],[2,1,0]] = ",a[[0,1,2],[2,1,0]])

# Return the boolean from a
b = a > 2
print("The Boolean state of b = a>2 = ", b)