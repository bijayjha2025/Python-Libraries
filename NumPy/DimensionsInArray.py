'''
Dimensions means the number of axes or the rank of the array. In NumPy, an array can have multiple dimensions, and each dimension corresponds to a different axis. For example, a 1D array has one dimension, a 2D array has two dimensions (like a matrix), and a 3D array has three dimensions (like a cube). The number of dimensions can be accessed using the `ndim` attribute of a NumPy array.
'''

import numpy as np
array = np.array(42)
print(array.ndim) #ndim means number of dimensions which is a inbuilt attribute of numpy array. It will return the number of dimensions of the array.

#This is an example of 0 D array. It has no dimensions, and it is a scalar value.

arraynext = np.array('A')
print(arraynext.ndim) #This is an example of 0 D array. It has no dimensions, and it is a scalar value.


arrayThree = np.array([1, 2, 3, 4, 5]) #It has list of elements.
print(arrayThree.ndim) #This is an example of 1 D array. It has one dimension.

arrayFour = np.array([[1, 2, 3],
                      [4, 5, 6]]) #It has a list of lists.
print(arrayFour.ndim) #This is an example of 2 D array. It has two dimensions.

arrayFive = np.array([[['A', 'B', 'C'],['D', 'E', 'F'],
                      ['G', 'H', 'I'], ['J', 'K', 'L']]])

print(arrayFive.ndim) #This is an example of 3 D array. It has three dimensions.
print(arrayFive.shape) #This will return the shape of the array. It will return a tuple of integers indicating the size of the array along each dimension.

#The output (1,4,3) means that the array has 1 block, 4 rows and 3 columns. The first dimension is the number of blocks, the second dimension is the number of rows, and the third dimension is the number of columns.

array00 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', 'A']]])
print(array00.shape) #This will return the shape of the array. It will return a tuple of integers indicating the size of the array along each dimension. It gives 3,3,3 which means that the array has 3 blocks, 3 rows and 3 columns. The first dimension is the number of blocks, the second dimension is the number of rows, and the third dimension is the number of columns.

#To access any elements in list previously, we used indexing or chain indexing like array[0][0][0]

#Example,
print(array00[0][0][0]) #This will return the first element of the first block, first row and first column which is 'A'.

#But in numpy, we can access using multidimensional indexing which is more efficient and faster.
#The same thing can be done using:

print(array00[0,0,0])
print(array00[1,2,1])
print(array00[0,2,1])
print(array00[1,1,1])