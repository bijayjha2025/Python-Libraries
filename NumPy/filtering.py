'''
Filtering is a process of selecting a subset of data based on certain criteria. In NumPy, filtering can be performed using boolean indexing, where a boolean array is used to select elements from another array. This allows for efficient and flexible data manipulation.
'''

import numpy as np

ages = np.array([[21, 25, 30, 35, 40, 17, 19, 23, 12],
                 [22, 26, 31, 36, 41, 15, 99, 24, 13]])

teenagers = ages[ages < 18] #This will create a boolean array where each element is True if the corresponding element in ages is less than 18, and False otherwise. The resulting boolean array is then used to index the ages array, selecting only the elements that are less than 18.
print(teenagers) #This will print the ages of all teenagers in the array.
print(ages) #we still have the original ages array intact, as filtering does not modify the original array.

adults = ages[(ages >=18) & (ages <= 50)] #This will create a boolean array where each element is True if the corresponding element in ages is greater than or equal to 18 and less than or equal to 50, and False otherwise. The resulting boolean array is then used to index the ages array, selecting only the elements that are between 18 and 50 (inclusive).

print(adults) #This will print the ages of all adults in the array.

# | is the logical OR operator, which can be used to combine multiple conditions. For example, if we want to select all ages that are either less than 18 or greater than 50, we can use the following code:

seniors = ages[(ages < 18) | (ages > 50)] #This will create a boolean array where each element is True if the corresponding element in ages is less than 18 or greater than 50, and False otherwise. The resulting boolean array is then used to index the ages array, selecting only the elements that are either less than 18 or greater than 50.
print(seniors) #This will print the ages of all seniors in the array.


evens = ages[ages % 2 == 0] #This will create a boolean array where each element is True if the corresponding element in ages is even, and False otherwise. The resulting boolean array is then used to index the ages array, selecting only the even ages.
print(evens) #This will print the even ages in the array.

odds = ages[ages % 2 != 0] #This will create a boolean array where each element is True if the corresponding element in ages is odd, and False otherwise. The resulting boolean array is then used to index the ages array, selecting only the odd ages.
print(odds) #This will print the odd ages in the array.

#where function: The np.where() function can be used to filter an array based on a condition. It returns the indices of the elements that satisfy the condition. It is useful when we want to find the indices of elements that meet a certain criteria, rather than the elements themselves.

adultsNew = np.where(ages >=18, ages, 0) #This will create a new array where each element is the corresponding element in ages if it is greater than or equal to 18, and 0 otherwise. The np.where() function takes three arguments: the condition, the value to return if the condition is True, and the value to return if the condition is False.
print(adultsNew) #This will print the new array with adults' ages and 0s for non-adults.

adultsNew2 = np.where(ages >=18, ages, -1) #This will create a new array where each element is the corresponding element in ages if it is greater than or equal to 18, and -1 otherwise. The np.where() function takes three arguments: the condition, the value to return if the condition is True, and the value to return if the condition is False.
print(adultsNew2) #This will print the new array with adults' ages and -
