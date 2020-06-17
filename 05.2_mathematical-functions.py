import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[6,5,4],[3,2,1]])

# Perform sum of all values of array
print("sum(a) = ", np.sum(a))

# Perform sum of values in each column
print("Sum of each column (axis=0) = ", np.sum(a,axis=0))

# Perform sum of values in each row
print("Sum of each row (axis=1) = ", np.sum(a,axis=1))

# Perform transpose of array
print("Tranpose of a = ", a.T)

# Perform dot product of 2D array/matrix
x = np.array([[1,2],[3,4]])
y = np.array([[5],[6]])
print("Dot productr of np.dot(x,y) = ", np.dot(x,y))
