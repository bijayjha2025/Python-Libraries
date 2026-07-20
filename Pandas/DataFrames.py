# Data Frames are two-dimensional labeled data structures with columns of potentially different types. You can think of them like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object. Like Series, DataFrame accepts many different kinds of input such as: Dict of 1D ndarrays, lists, dicts, or Series; 2-D numpy.ndarray; Structured or record ndarray; A Series; Another DataFrame. The DataFrame has both a row and column index; it can be thought of as a dict-like container for Series objects. It is generally the most commonly used pandas object.

import pandas as pd

data = {
    "Name": ["Tom", "Jerry", "Mickey", "Donald"],
    "Age": [20, 21, 19, 18],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}

#Converting dictionary to DataFrame
df = pd.DataFrame(data) #Here, DataFrame(data) is a constructor that creates a new DataFrame object from the provided dictionary. The keys of the dictionary become the column labels of the DataFrame, and the corresponding values become the data in the DataFrame.
print(df) #This will print the DataFrame object, displaying the column labels and the corresponding data. The DataFrame has three columns: "Name", "Age", and "City", and four rows corresponding to the entries in the dictionary.

#Index can be customized as well. By default, pandas assigns an integer index starting from 0 to the rows of the DataFrame. However, you can specify a custom index by passing a list of labels to the index parameter when creating the DataFrame.
custom_index = ["Student1", "Student2", "Student3", "Student4"]
df = pd.DataFrame(data, index=custom_index) #Here, DataFrame(data, index=custom_index) is a constructor that creates a new DataFrame object from the provided dictionary and custom index. The keys of the dictionary become the column labels of the DataFrame, and the corresponding values become the data in the DataFrame. The custom index is a list of labels that will be used as the row labels for the DataFrame.
print(df) #This will print the DataFrame object with the custom index, displaying the column labels and the corresponding data. The DataFrame has three columns: "Name", "Age", and "City", and four rows corresponding to the entries in the dictionary, with the custom index labels "Student1", "Student2", "Student3", and "Student4".

#To access a single row, we can use loc
print(df.loc["Student1"]) #This will print the row corresponding to the index label "Student1". The loc method allows for label-based indexing, so you can directly access the row corresponding to a specific index label. In this case, it will return a Series object containing the data for "Student1", with the column labels as the index of the Series.
print(df.loc["Student2"]) #This will print the row corresponding to the index label "Student2". The loc method allows for label-based indexing, so you can directly access the row corresponding to a specific index label. In this case, it will return a Series object containing the data for "Student2", with the column labels as the index of the Series.
print(df.loc["Student3"])
print(df.loc["Student4"])
#iloc is another way of accessing rows and columns in a DataFrame, but it uses integer-based indexing instead of label-based indexing. The iloc method allows you to access rows and columns by their integer positions, which can be useful when you want to select data based on their order in the DataFrame rather than their labels.
print(df.iloc[0]) #This will print the first row of the DataFrame, which corresponds to the index position 0. The iloc method allows for integer-based indexing, so you can directly access the row corresponding to a specific integer position. In this case, it will return a Series object containing the data for the first row, with the column labels as the index of the Series.
print(df.iloc[1])
print(df.iloc[2])


#To add new columns to the DataFrame, we can simply assign a new Series or list to a new column label. This will create a new column in the DataFrame with the specified label and populate it with the provided data.
df["isStudent"] = [True, True, True, True] #This will add a new column to the DataFrame with the label "isStudent" and populate it with the provided list of boolean values. The new column will have the same number of rows as the existing DataFrame, and each value in the list will correspond to a row in the DataFrame.
print(df) #This will print the updated DataFrame object, displaying the column labels and the corresponding data. The DataFrame now has four columns: "Name", "Age", "City", and "isStudent", and four rows corresponding to the entries in the dictionary, with the custom index labels "Student1", "Student2", "Student3", and "Student4".


df["Job"] = ["Engineer", "Doctor", "Artist", "Teacher"] #This will add a new column to the DataFrame with the label "Job" and populate it with the provided list of strings. The new column will have the same number of rows as the existing DataFrame, and each value in the list will correspond to a row in the DataFrame.
print(df) #This will print the updated DataFrame object, displaying the column labels and the corresponding data.


#Add a new row to the DataFrame using loc. The loc method allows you to add a new row by specifying a new index label and assigning a list or Series of values to it. The new row will have the same number of columns as the existing DataFrame, and each value in the list or Series will correspond to a column in the DataFrame.
new_row = pd.DataFrame([{"Name": "Minnie", "Age": 22, "City": "San Francisco", "isStudent": True, "Job": "Designer"}], index= ["Student5"])
df = pd.concat([df, new_row])

print(df) #This will print the updated DataFrame object, displaying the column labels and the corresponding data. The DataFrame now has five rows, with the new row corresponding to the index label "Student5" and the provided values for each column.

#Add new rows

new_rows = pd.DataFrame([
    {"Name": "Goofy", "Age": 23, "City": "Seattle", "isStudent": False, "Job": "Comedian"},
    {"Name": "Pluto", "Age": 24, "City": "Miami", "isStudent": False, "Job": "Dog"}
], index=["Student6", "Student7"])
df = pd.concat([df, new_rows])
print(df)

#In summary, DataFrames are two-dimensional labeled data structures that allow for easy manipulation and analysis of data. They can be created from various input types, including dictionaries, lists, and other DataFrames. The loc and iloc methods provide powerful ways to access and manipulate data based on labels or integer positions, respectively. Additionally, new columns and rows can be added to the DataFrame using simple assignment or concatenation methods.