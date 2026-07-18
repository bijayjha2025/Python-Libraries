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

workingData = [100, 101, 102, 103, 104]
#In normal, the index of a Series is automatically generated as a range of integers starting from 0. However, you can also specify a custom index for the Series by providing a list of labels.

series = pd.Series(workingData, index= ['a', 'b', 'c', 'd', 'e']) #Here, Series(workingData, index=['a', 'b', 'c', 'd', 'e']) is a constructor that creates a new Series object from the provided data and custom index. The data is a list of integers, and the index is a list of labels corresponding to each element in the data list.
print(series) #This will print the Series object, displaying the custom index and the corresponding values

#By this technique, we can create a Series with a custom index, which allows for more meaningful labels and easier access to the data. The custom index can be any hashable type, such as strings, integers, or tuples.

#This helps in better organization and understanding of the data, especially when working with larger datasets or when the default integer index is not sufficient for the analysis.

seriesNew = pd.Series(workingData, index= ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']) #Here, Series(workingData, index=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']) is a constructor that creates a new Series object from the provided data and custom index. The data is a list of integers, and the index is a list of labels corresponding to each element in the data list.
print(seriesNew) #This will print the Series object, displaying the custom index and the corresponding values. The custom index represents the days of the week, and the values are the elements of the original data list.

