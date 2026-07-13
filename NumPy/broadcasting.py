'''
In NumPy, broadcasting is a mechanism that allows to perform operations on arrays with different shapes. It allows so by virtually expanding dimensions of the smaller array to match the shape of the larger array without actually copying data. This enables efficient computation and memory usage.
'''
import numpy as np

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3], [4]])

print(array1.shape) #This will print the shape of array1, which is (1, 4).
print(array2.shape) #This will print the shape of array2, which is (4, 1).

#To be compatible for broadcasting, the dimensions of the arrays must either be equal or one of them must be 1. In this case, array1 has shape (1, 4) and array2 has shape (4, 1). The first dimension of array1 is 1, which allows it to be broadcasted to match the first dimension of array2, which is 4. The second dimension of array2 is 1, which allows it to be broadcasted to match the second dimension of array1, which is 4. Therefore, these two arrays are compatible for broadcasting.

print(array1 * array2) #This will perform element-wise multiplication of the two arrays using broadcasting. The result will be a 4x4 array where each element is the product of the corresponding elements from array1 and array2.

#Another example:
array3 = np.array([[1, 2, 3], [4, 5, 6]])
array4 = np.array([[1], [2]])

print(array3.shape) #This will print the shape of array3, which is (2, 3).
print(array4.shape) #This will print the shape of array4, which is (2, 1).

#To be compatible for broadcasting, the dimensions of the arrays must either be equal or one of them must be 1. In this case, array3 has shape (2, 3) and array4 has shape (2, 1). The first dimension of both arrays is 2, which allows them to be broadcasted to match each other. The second dimension of array4 is 1, which allows it to be broadcasted to match the second dimension of array3, which is 3. Therefore, these two arrays are compatible for broadcasting.

print(array3 + array4) #This will perform element-wise addition of the two arrays using broadcasting. The result will be a 2x3 array where each element is the sum of the corresponding elements from array3 and array4.

#Let's see an example where broadcasting is not possible:
array5 = np.array([[1, 2, 3], [4, 5, 6]])
array6 = np.array([[1, 2], [3, 4]])

print(array5.shape) #This will print the shape of array5, which is (2, 3).
print(array6.shape) #This will print the shape of array6, which is (2, 2).

#Here, the first dimensions of both arrays are equal (2), but the second dimensions are not equal (3 and 2). Since neither of the second dimensions is 1, these two arrays are not compatible for broadcasting. Therefore, attempting to perform an operation on these two arrays will result in a ValueError.

# print(array5 + array6) #This will raise a ValueError because the two arrays are not compatible for broadcasting.

#Practice Question:
arrayNew = np.array([[1,2,3,4,5,6,7,8,9,10]])
arrayNext = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(arrayNew.shape) #This will print the shape of arrayNew, which is (1, 10).
print(arrayNext.shape) #This will print the shape of arrayNext, which is (10, 1).

print(arrayNew * arrayNext) #This will perform element-wise multiplication of the two arrays using broadcasting. The result will be a 10x10 array where each element is the product of the corresponding elements from arrayNew and arrayNext.