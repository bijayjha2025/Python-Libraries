import numpy as np

arr = np.array([1,2,3,4,5])
newarr = np.array_split(arr, 3) #This will split the array arr into 3 equal parts. The array_split() function takes two arguments: the array to be split and the number of parts to split it into. If the array cannot be split evenly, the last part will contain the remaining elements.
print(newarr) #This will print a list of 3 arrays, each containing a part of the original array. The first two arrays will contain 2 elements each, and the last array will contain 1 element.

print(newarr[0]) #This will print the first part of the split array, which is an array containing the first 2 elements of the original array.
print(newarr[1]) #This will print the second part of the split array, which is an array containing the next 2 elements of the original array.
print(newarr[2]) #This will print the third part of the split array, which is an array containing the last element of the original array.
print(newarr[0][0]) #This will print the first element of the first part of the split array, which is the first element of the original array.
print(newarr[1][1]) #This will print the second element of the second part of the split array, which is the fourth element of the original array.
print(newarr[2][0]) #This will print the first element of the third part of the split array, which is the fifth element of the original array.
