
#Scalar arithmetic

import numpy as np

array = np.array([1.56, 2.45, 3.78])
print(array + 1) #This will add 1 to each element of the array.
print(array - 1) #This will subtract 1 from each element of the array.
print(array * 2) #This will multiply each element of the array by 2.
print(array / 4) #This will divide each element of the array by 4.
print(array ** 5) #This will raise each element of the array to the power of 5.
print(array % 2) #This will return the remainder of each element of the array when divided by 2.


#Vectorized math functions
print(np.sqrt(array)) #This will return the square root of each element of the array.
print(np.exp(array)) #This will return the exponential of each element of the array.
print(np.round(array)) #This will round each element of the array to the nearest integer.
print(np.floor(array)) #This will return the largest integer less than or equal to each element of the array.
print(np.ceil(array)) #This will return the smallest integer greater than or equal to each element of the array.
print(np.pi) #This will return the value of pi.
print(np.sin(array)) #This will return the sine of each element of the array.   
print(np.cos(array)) #This will return the cosine of each element of the array.


#Practice Question
radii = np.array([1, 2, 3, 4, 5])
print(np.pi * radii ** 2)


length = np.array([3.4, 5.6, 7.8])
print(np.floor(length) * np.ceil(length))


#Element wise arithmetic
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2) #This will add the corresponding elements of the two arrays.
print(array1 - array2) #This will subtract the corresponding elements of the two arrays.
print(array1 * array2) #This will multiply the corresponding elements of the two arrays.
print(array1 / array2) #This will divide the corresponding elements of the two arrays.
print(array1 ** array2) #This will raise the corresponding elements of the two arrays to the power of each other.
print(array1 % array2) #This will return the remainder of the corresponding elements of the two arrays when divided by each other.

#Comparison operators
scores = np.array([85, 90, 78, 92, 88, 100, 34, 46, 56, 64])
print(scores > 80) #This will return a boolean array indicating which elements of the scores are greater than 80.
print(scores < 90) #This will return a boolean array indicating which elements of the scores are less than 90.
print(scores == 88) #This will return a boolean array indicating which elements of the scores are equal to 88.
print(scores != 78) #This will return a boolean array indicating which elements of the scores are not equal to 78.
print(scores == 100) #This will return a boolean array indicating which elements of the scores are equal to 100.
print(scores >= 34) #This will return a boolean array indicating which elements of the scores are greater than or equal to 34.

scores[scores < 70] = 0 #
print(scores)