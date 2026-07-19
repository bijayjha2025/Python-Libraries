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

print(series[series < 100]) #This will print an empty Series because there are no values in the Series that are less than 100. The condition series < 100 creates a boolean mask, and when applied to the Series, it filters out all values that do not meet the condition.

print(series[series > 100]) #This will print a Series containing all the values that are greater than 100. The condition series > 100 creates a boolean mask, and when applied to the Series, it filters out all values that do not meet the condition. In this case, all values in the Series are greater than 100, so the entire Series is returned.

#The same can be done using dictionary as well.

calories = {'day1': 1200, 'day2': 2250, 'day3': 3300, 'day4': 2350, 'day5': 4400}
seriesCal = pd.Series(calories) #Here, Series(calories) is a constructor that creates a new Series object from the provided dictionary. The keys of the dictionary become the index labels of the Series, and the corresponding values become the data in the Series.
print(seriesCal)

#Using loc to access elements in the Series created from a dictionary:
print(seriesCal.loc['day1']) #This will print the value associated with the index label 'day1', which is 1200. The loc method allows for label-based indexing, so you can directly access the value corresponding to a specific index label.
print(seriesCal.loc['day2']) #This will print the value associated with the index label 'day2', which is 2250. The loc method allows for label-based indexing, so you can directly access the value corresponding to a specific index label.

print(seriesCal.loc['day3']) #This will print the value associated with the index label 'day3', which is 3300. The loc method allows for label-based indexing, so you can directly access the value corresponding to a specific index label.
print(seriesCal.loc['day4']) #This will print the value associated with the index label 'day4', which is 2350. The loc method allows for label-based indexing, so you can directly access the value corresponding to a specific index label.
print(seriesCal.loc['day5']) #This will print the value associated with the index label 'day5', which is 4400. The loc method allows for label-based indexing, so you can directly access the value corresponding to a specific index label.

seriesCal.loc['day1'] = + 1300 #This will update the value at index 'day1' in the Series to 1300. The loc method allows for label-based indexing, so you can directly assign a new value to a specific index label. In this case, the value at index 'day1' is changed from 1200 to 1300.
print(seriesCal) #This will print the updated Series object, displaying the index and the corresponding values. The value at index 'day1' has been updated to 1300, while the other values remain unchanged.