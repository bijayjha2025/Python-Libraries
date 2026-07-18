#Loc in Pandas: It is a method used to access a group of rows and columns in a DataFrame by labels or a boolean array. It allows for label-based indexing, which means you can select data based on the row and column labels rather than their integer positions. The loc method is particularly useful when you want to filter data based on specific conditions or when you want to select a subset of the DataFrame.

import pandas as pd

data = [105, 106, 107, 108, 109]
series = pd.Series(data, index= ['a', 'b', 'c', 'd', 'e']) #Here, Series(data, index=['a', 'b', 'c', 'd', 'e']) is a constructor that creates a new Series object from the provided data and custom index. The data is a list of integers, and the index is a list of labels corresponding to each element in the data list.
print(series['a'])
print(series['b'])
print(series['c'])
print(series['d'])
# print(series['f']) #This will raise a KeyError because 'f' is not a valid index label in the Series. The loc method only allows access to existing labels, and if you try to access a label that does not exist, it will result in an error.

series.loc['d'] = 110  #This will update the value at index 'd' in the Series to 110. The loc method allows for label-based indexing, so you can directly assign a new value to a specific index label. In this case, the value at index 'd' is changed from 108 to 110.
print(series) #This will print the updated Series object, displaying the index and the corresponding values. The value at index 'd' has been updated to 110, while the other values remain unchanged.

#Accessing elements is similar to accessing elements in an array or a list, but with the added benefit of using labels instead of integer positions. This makes it easier to work with data that has meaningful labels, such as names, dates, or categories.

