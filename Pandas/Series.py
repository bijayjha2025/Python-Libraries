#Series in Pandas is a one-dimensional labeled array that can hold any data type, such as integers, floats, strings, or Python objects. Each element in a Series has an associated index, which allows for easy access and manipulation of the data. Series can be created from lists, dictionaries, or NumPy arrays. In physical analogy, a Series can be thought of as a single column in a spreadsheet or a database table, where the index represents the row labels and the values represent the data in that column.

import pandas as pd

data = [100, 101, 102, 103, 104]
series = pd.Series(data) #Here, Series(data) is a constructor that creates a new Series object from the provided data. The data can be a list, NumPy array, or dictionary. In this case, we are passing a list of integers to create a Series.

print(series) #This will print the Series object, displaying the index and the corresponding values. The index is automatically generated as a range of integers starting from 0, and the values are the elements of the original data list.

data1 = ["A", "B", "C", "D", "E"]
series1 = pd.Series(data1) #Here, Series(data1) is a constructor that creates a new Series object from the provided list. The index is automatically generated as a range of integers starting from 0, and the values are the elements of the original data list.
print(series1) #This will print the Series object, displaying the index and the corresponding values.


data2 = [True, False, True, False, True]
series2 = pd.Series(data2) #Here, Series(data2) is a constructor that creates a new Series object from the provided list. The index is automatically generated as a range of integers starting from 0, and the values are the elements of the original data list.
print(series2) #This will print the Series object, displaying the index and the corresponding values.