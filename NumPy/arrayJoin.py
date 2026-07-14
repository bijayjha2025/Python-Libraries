#In numpy, we can join two or more arrays using the numpy.concatenate() function. This function takes a sequence of arrays as input and concatenates them along a specified axis. The default axis is 0, which means that the arrays will be joined vertically (row-wise). If we want to join the arrays horizontally (column-wise), we can specify axis=1.

import numpy as np

arr1 = np.array([1, 2])
arr2 = np.array([5, 6])

arr = np.concatenate((arr1, arr2)) #This will concatenate the two arrays arr1 and arr2 along the default axis (axis=0), resulting in a new array that contains all the elements of both arrays.
print(arr)

#Join two 2-D arrays along rows (axis = 1):
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

#joining array using stack functions
arrNew = np.stack((arr1, arr2), axis = 1)
print(arrNew) #This will stack the two 2-D arrays arr1 and arr2 along the specified axis (axis=1), resulting in a new array that contains the elements of both arrays stacked vertically.


#Stacking along rows

arrNew2 = np.hstack((arr1, arr2)) #This will horizontally stack the two 2-D arrays arr1 and arr2, resulting in a new array that contains the elements of both arrays stacked side by side.
print(arrNew2)

#Stacking along columns
arrNew3 = np.vstack((arr1, arr2)) #This will vertically stack the two 2-D arrays arr1 and arr2, resulting in a new array that contains the elements of both arrays stacked on top of each other.
print(arrNew3)

#Stacking along depth
arrNew4 = np.dstack((arr1, arr2)) #This will depth-wise stack the two 2-D arrays arr1 and arr2, resulting in a new array that contains the elements of both arrays stacked along the third dimension.
print(arrNew4)