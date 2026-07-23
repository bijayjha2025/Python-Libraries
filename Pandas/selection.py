#In this session, we will learn about selection in pandas. Selection is an important aspect of data analysis, as it allows us to extract specific rows and columns from a DataFrame based on certain conditions or criteria. Pandas provides various methods and techniques for selecting data, including indexing, slicing, boolean indexing, and using the loc and iloc functions.

import pandas as pd
df = pd.read_csv(r"C:\Users\pc\Desktop\New\Pandas\Data\data.csv")

print(df.columns) #This will print the column labels of the DataFrame, allowing us to see the available columns for selection.
print(df.head()) #This will print the first few rows of the DataFrame, giving us a glimpse of the data and its structure.

print(df[' Name']) #This will select the 'Name' column from the DataFrame and print its values. We can also use df.Name to achieve the same result.

print(df[' Name'].to_string(index=False)) #This will print the values of the 'Name' column without displaying the index.

print(df[[' Name', ' Age']]) #This will select multiple columns, 'Name' and 'Age', from the DataFrame and print their values.

print(df[[' Name', ' Age', ' City']]) #This will select multiple columns, 'Name', 'Age', and 'City', from the DataFrame and print their values.

print(df[[' Name', ' Age', ' City', ' Country']]) #This will select multiple columns, 'Name', 'Age', 'City', and 'Country', from the DataFrame and print their values.


#Selecting by rows
#To perform selection by rows, we need to use the loc and iloc functions. The loc function allows us to select rows based on their labels, while the iloc function allows us to select rows based on their integer index positions. loc function is label-based, meaning that we have to specify the name of the row or column that we want to select. On the other hand, iloc function is integer position-based, meaning that we have to specify the index of the row or column that we want to select. Whereas, the loc function is inclusive of the specified labels, meaning that it will include the rows or columns with the specified labels in the selection. In contrast, the iloc function is exclusive of the specified index positions, meaning that it will exclude the rows or columns with the specified index positions from the selection.

#Example of selecting rows using loc and iloc functions:
print(df.loc[0]) #This will select the first row of the DataFrame using the loc function and print its values. The index label 0 corresponds to the first row in the DataFrame.
print(df.iloc[0]) #This will select the first row of the DataFrame using the iloc function and print its values. The index position 0 corresponds to the first row in the DataFrame.
print(df.loc[0:2]) #This will select the first three rows of the DataFrame using the loc function and print their values. The index labels 0, 1, and 2 correspond to the first three rows in the DataFrame.
print(df.iloc[0:2]) #This will select the first two rows of the DataFrame using the iloc function and print their values. The index positions 0 and 1 correspond to the first two rows in the DataFrame.
print(df.loc[[0, 2, 4]]) #This will select the rows with index labels 0, 2, and 4 from the DataFrame using the loc function and print their values.
print(df.iloc[[0, 2, 4]]) #This will select the rows with index positions 0, 2, and 4 from the DataFrame using the iloc function and print their values.
print(df.loc[df[' Age'] > 30]) #This will select the rows where the 'Age' column has values greater than 30 using the loc function and print their values.
print(df.iloc[df[' Age'] > 30]) #This will select the rows where the 'Age' column has values greater than 30 using the iloc function and print their values.
print(df.loc[df[' Age'] > 30, [' Name', ' Age']]) #This will select the rows where the 'Age' column has values greater than 30 and only the 'Name' and 'Age' columns using the loc function and print their values.
print(df.iloc[df[' Age'] > 30, [0, 1]]) #This will select the rows where the 'Age' column has values greater than 30 and only the first two columns using the iloc function and print their values.
print(df.loc[df[' Age'] > 30, [' Name', ' Age', ' City']]) #This will select the rows where the 'Age' column has values greater than 30 and only the 'Name', 'Age', and 'City' columns using the loc function and print their values.
print(df.iloc[df[' Age'] > 30, [0, 1, 2]]) #This will select the rows where the 'Age' column has values greater than 30 and only the first three columns using the iloc function and print their values.
print(df.loc[df[' Age'] > 30, [' Name', ' Age', ' City', ' Country']]) #This will select the rows where the 'Age' column has values greater than 30 and only the 'Name', 'Age', 'City', and 'Country' columns using the loc function and print their values.
print(df.iloc[df[' Age'] > 30, [0, 1, 2, 3]]) #This will select the rows where the 'Age' column has values greater than 30 and only the first four columns using the iloc function and print their values.
print(df.loc[df[' Age'] > 30, [' Name', ' Age', ' City', ' Country', ' Salary']]) #This will select the rows where the 'Age' column has values greater than 30 and only the 'Name', 'Age', 'City', 'Country', and 'Salary' columns using the loc function and print their values.
print(df.iloc[df[' Age'] > 30, [0, 1, 2, 3, 4]]) #This will select the rows where the 'Age' column has values greater than 30 and only the first five columns using the iloc function and print their values.
print(df.loc[df[' Age'] > 30, [' Name', ' Age', ' City', ' Country', ' Salary', ' Department']]) #This will select the rows where the 'Age' column has values greater than 30 and only the 'Name', 'Age', 'City', 'Country', 'Salary', and 'Department' columns using the loc function and print their values.
print(df.iloc[df[' Age'] > 30, [0, 1, 2, 3, 4, 5]]) #This will select the rows where the 'Age' column has values greater than 30 and only the first six columns using the iloc function and print their values.
print(df.loc[df[' Age'] > 30, [' Name', ' Age', ' City', ' Country', ' Salary', ' Department', ' Position']]) #This will select the rows where the 'Age' column has values greater than 30 and only the 'Name', 'Age', 'City', 'Country', 'Salary', 'Department', and 'Position' columns using the loc function and print their values.
print(df.iloc[df[' Age'] > 30, [0, 1, 2, 3, 4, 5, 6]]) #This will select the rows where the 'Age' column has values greater than 30 and only the first seven columns using the iloc function and print their values.