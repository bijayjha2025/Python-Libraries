import numpy as np

#Iterating over arrays: In NumPy, we can iterate over arrays using various methods, such as for loops, the nditer() function, and the flat attribute. Iterating over arrays allows us to access and manipulate individual elements or subarrays.

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

for x in arr:
    print(x) #This will print each row of the array as a separate array.

arrSimple = np.array([1, 2, 3, 4, 5])
for x in arrSimple:
    print(x) #This will print each element of the array as a separate value.


#If we iterate on a n-D array, it will go through n-1 iterations, and in the last iteration, it will iterate through the last axis.

#Iterate on each scalar element of the 2-D array:
for x in arr:
    for y in x:
        print(y) #This will print each element of the 2-D array as a separate value.


#Iterating 3-D arrays: In NumPy, we can also iterate over 3-D arrays using nested for loops. Each iteration will go through the first two dimensions, and in the last iteration, it will iterate through the last dimension.

arr3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in arr3D:
    for y in x:
        for z in y:
            print(z) #This will print each element of the 3-D array as a separate value.

#or simply:
for x in arr3D:
    print(x) #This will print each 2-D subarray of the 3-D array as a separate array.


#Iterating using nditer(): The nditer() function in NumPy provides a flexible way to iterate over arrays. It allows us to iterate over multi-dimensional arrays in a more efficient manner.

arr2D = np.array([[1, 2, 3], [4, 5, 6]])
for x in np.nditer(arr2D):
    print(x) #This will print each element of the 2-D array as a separate value.


#Iterating with different data types: The nditer() function also allows us to specify the data type of the elements during iteration. This can be useful when we want to perform operations on the elements with a specific data type.

arrFloat = np.array([[1.1, 2.2], [3.3, 4.4]])
for x in np.nditer(arrFloat, flags=['buffered'], op_dtypes=['float64']):
    print(x) #This will print each element of the 2-D array as a separate value, with the specified data type of float64.

arrInt = np.array([[1, 2], [3, 4]])
for x in np.nditer(arrInt, flags=['buffered']):
    print(x) #This will print each element of the 2-D array as a separate value, with the specified data type of int32.

arrComplex = np.array([[1+2j, 3+4j], [5+6j, 7+8j]])
for x in np.nditer(arrComplex, flags=['buffered'], op_dtypes=['complex128']):
    print(x) #This will print each element of the 2-D array as a separate value, with the specified data type of complex128.


arrStr = np.array([['apple', 'banana'], ['cherry', 'date']])
for x in np.nditer(arrStr, flags=['buffered'], op_dtypes=['U6']):
    print(x) #This will print each element of the 2-D array as a separate value, with the specified data type of Unicode string of length 6.


#Enumerated iteration: The ndenumerate() function in NumPy allows us to iterate over an array while keeping track of the index of each element. This can be useful when we need to know the position of each element during iteration.

for idx, x in np.ndenumerate(arr2D):
    print(idx, x) #This will print the index and value of each element in the 2-D array. The idx variable contains the index of the current element, and the x variable contains the value of the current element.


#In 2d array
for idx, x in np.ndenumerate(arr3D):
    print(idx, x) #This will print the index and value of each element in the 3-D array. The idx variable contains the index of the current element, and the x variable contains the value of the current element.