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