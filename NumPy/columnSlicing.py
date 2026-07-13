#Slicing by columns
import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

print(array[:,0]) #This will return the first column of the array. The start index is 0, the stop index is not specified and the step is 1. It will return the elements from index 0 to the end of the array.

print(array[:,1]) #This will return the second column of the array. The start index is 1, the stop index is not specified and the step is 1. It will return the elements from index 1 to the end of the array.

print(array[:,2]) #This will return the third column of the array. The start index is 2, the stop index is not specified and the step is 1. It will return the elements from index 2 to the end of the array.

print(array[:,3]) #This will return the fourth column of the array. The start index is 3, the stop index is not specified and the step is 1. It will return the elements from index 3 to the end of the array.

print(array[:,0:2]) #This will return the first two columns of the array. The start index is 0, the stop index is 2 and the step is 1. It will return the elements from index 0 to index 1.

print(array[:, -1]) #This will return the last column of the array. The start index is -1, the stop index is not specified and the step is 1. It will return the elements from index -1 to the end of the array.

print(array[:, -2]) #This will return the second last column of the array. The start index is -2, the stop index is not specified and the step is 1. It will return the elements from index -2 to the end of the array.

print(array[:, 0:3:2]) #This will return the first and third columns of the array. The start index is 0, the stop index is 3 and the step is 2. It will return the elements from index 0 to index 2 with a step of 2.

print(array[:, 1:4]) #This will return the second, third and fourth columns of the array. The start index is 1, the stop index is 4 and the step is 1. It will return the elements from index 1 to index 3.

print(array[:, ::2]) #This will return the first and third columns of the array. The start index is 0, the stop index is not specified and the step is 2. It will return the elements from index 0 to the end of the array with a step of 2.

print(array[:, 1::2]) #This will return the second and fourth columns of the array. The start index is 1, the stop index is not specified and the step is 2. It will return the elements from index 1 to the end of the array with a step of 2.

print(array[:, ::-2]) #This will return the last and second last columns of the array. The start index is -1, the stop index is not specified and the step is -2. It will return the elements from index -1 to the end of the array with a step of -2.

print(array[0:2, 0:2]) #This will return the first two rows and first two columns of the array. The start index for rows is 0, the stop index for rows is 2, the start index for columns is 0 and the stop index for columns is 2. It will return the elements from index 0 to index 1 for both rows and columns.

print(array[2:, 0:2]) #This will return the last two rows and first two columns of the array. The start index for rows is 2, the stop index for rows is not specified, the start index for columns is 0 and the stop index for columns is 2. It will return the elements from index 2 to the end of the array for rows and from index 0 to index 1 for columns.