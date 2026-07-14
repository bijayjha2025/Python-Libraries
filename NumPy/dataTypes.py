#Data types in NumPy: In NumPy, data types are used to define the type of elements in an array. NumPy provides a wide range of data types, including integers, floating-point numbers, complex numbers, and more. The data type of an array can be specified when creating the array or can be inferred from the input data.

import numpy as np

x = np.array([1,2,3])
print(type(x), x.dtype) #This will print the type of the array and its data type. The dtype attribute of the array object returns the data type of the elements in the array.

arr = np.array(["bat", "cat", "dog"])
print(arr.dtype) #It gives U3 meaning that the array contains Unicode strings of length 3. The dtype attribute of the array object returns the data type of the elements in the array.

arr1 = np.array(["apple", "banana", "cherry"])
print(arr1.dtype) #It gives U6 meaning that the array contains Unicode strings of length 6. The dtype attribute of the array object returns the data type of the elements in the array.

y = np.array([1.0, 2.0, 3.0])
print(type(y), y.dtype) #This will print the type of the array and its data type. The dtype attribute of the array object returns the data type of the elements in the array.

#Creating arrays with a defined data type
arra = np.array([1, 2, 3], dtype='int32') #This will create an array of integers with a data type of int32. The dtype argument specifies the desired data type for the elements in the array.
print(arra.dtype) #This will print the data type of the array, which is int32.

array4 = np.array([1, 2, 3], dtype='float32') #This will create an array of floating-point numbers with a data type of float32. The dtype argument specifies the desired data type for the elements in the array.
print(array4.dtype) #This will print the data type of the array, which is float32.

array5 = np.array([1, 2, 3], dtype='complex64') #This will create an array of complex numbers with a data type of complex64. The dtype argument specifies the desired data type for the elements in the array.
print(array5.dtype) #This will print the data type of the array, which is complex64.

array6 = np.array([1, 2, 3], dtype='bool') #This will create an array of boolean values with a data type of bool. The dtype argument specifies the desired data type for the elements in the array.
print(array6.dtype) #This will print the data type of the array, which is bool

array7 = np.array([1, 2, 3], dtype='str') #This will create an array of strings with a data type of str. The dtype argument specifies the desired data type for the elements in the array.
print(array7.dtype) #This will print the data type of the array, which is str as U1

