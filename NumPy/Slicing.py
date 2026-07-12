import numpy as np

array = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]

print(np.array(array))
print(np.ndim(array))
#This is a 2 d array since it has 2 dimensions. The first dimension is the number of rows and the second dimension is the number of columns. The shape of the array can be accessed using the shape attribute of the numpy array. It will return a tuple of integers indicating the size of the array along each dimension.

#Methods of slicing in numpy are:
#array[start:stop:step]

print(array[0:3]) #This will return the first 3 rows of the array. The start index is 0, the stop index is 3 and the step is 1. It will return the rows from index 0 to index 2.
print(array[1:4]) #This will return the rows from index 1 to index 3. The start index is 1, the stop index is 4 and the step is 1. It will return the rows from index 1 to index 3.
print(array[1:]) #This will return the rows from index 1 to the end of the array. The start index is 1, the stop index is not specified and the step is 1. It will return the rows from index 1 to the end of the array.

print(array[0:4:2]) #This will return the rows from index 0 to index 3 with a step of 2. It will return the rows at indices 0 and 2.

print(array[::2]) #This will return the rows from index 0 to the end of the array with a step of 2. It will return the rows at indices 0 and 2.

