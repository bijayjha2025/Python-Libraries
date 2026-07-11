'''
NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. It stands for Numerical Python. NumPy is open source. It is also one of the most fundamental packages for scientific computing with Python.

Why use NumPy?
In Python we have lists that fulfills the purpose of arrays, but are slow to process. NumPy aims to provide an array object that is up to 50x faster than traditional Python lists. The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

Why is NumPy faster than lists?
NumPy arrays are implemented in C, which makes them much faster than Python lists for numerical operations. They also use less memory and provide more convenient functions for mathematical operations.

It is mostly build using C/C++ because of which it is very fast. It is also a library that is used in almost all the fields of data science and machine learning. It is also used in image processing, natural language processing, and many other fields.
'''

import numpy as np
print(np.__version__) #checking if numpy is installed

myList = [1, 2, 3, 4, 5]
myList = myList * 2 #multiplying the list by 2
print(myList)

#If we use normal Python lists, instead of multiplying each element by 2, it will just concatenate the list with itself. To multiply each element by 2, we can use NumPy arrays. NumPy arrays are superior to Python lists in terms of performance and functionality.

array = np.array(myList) #converting the list to a numpy array
print(array, type(array))
array = array * 2 #multiplying the numpy array by 2
print(array)

#What is the difference between a list and an array?
#1. Lists can contain elements of different data types, while arrays can only contain elements of the same data type.
#2. Lists are slower than arrays for numerical operations.

