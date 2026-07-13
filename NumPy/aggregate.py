'''
Aggregate functions: It is a function that takes an array as input and returns a single value as output. It is used to perform operations on the entire array and return a summary statistic. Some common aggregate functions in NumPy include sum, mean, median, min, max, and std (standard deviation).
'''

import numpy as np

array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

print(np.sum(array)) #This will return the sum of all elements in the array.
print(np.mean(array)) #This will return the mean of all elements in the array.
print(np.median(array)) #This will return the median of all elements in the array.
print(np.min(array)) #This will return the minimum value in the array.
print(np.max(array)) #This will return the maximum value in the array.
print(np.std(array)) #This will return the standard deviation of all elements in the array.
print(np.var(array)) #This will return the variance of all elements in the array.
print(np.prod(array)) #This will return the product of all elements in the array.
print(np.cumsum(array)) #This will return the cumulative sum of all elements in the array.
print(np.argmin(array)) #This will return the index of the minimum value in the array.
print(np.argmax(array)) #This will return the index of the maximum value in the array.


#To perform aggregate functions along a specific axis, we can use the axis parameter. The axis parameter specifies the axis along which the operation is performed. For example, if we want to calculate the sum of each row in a 2D array, we can set axis=1. If we want to calculate the sum of each column, we can set axis=0.

print(np.sum(array, axis=0)) #This will return the sum of each column in the array.
print(np.sum(array, axis=1)) #This will return the sum of each row in the array.
print(np.mean(array, axis=0)) #This will return the mean of each column in the array.
print(np.mean(array, axis=1)) #This will return the mean of each row in the array.
print(np.median(array, axis=0)) #This will return the median of each column in the array.
print(np.median(array, axis=1)) #This will return the median of each row in the array.  