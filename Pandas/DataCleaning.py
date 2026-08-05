#Data Cleaning: Data cleaning is the process of identifying and correcting errors, inconsistencies, and inaccuracies in a dataset to ensure that the data is accurate, complete, and reliable. In Pandas, we can perform data cleaning using various methods such as `dropna()`, `fillna()`, `replace()`, and `astype()`. It involves handling missing values, removing duplicates, correcting data types, and standardizing data formats.

import pandas as pd
df = pd.read_csv(r"C:\Users\pc\Desktop\New\Pandas\Data\data.csv")
print(df) #This will print the original DataFrame.

#We can use the `dropna()` method to remove rows with missing values from the DataFrame.
#Example: Remove rows with missing values from the DataFrame.
df_dropped_na = df.dropna() #This will remove rows with missing values from the DataFrame.
print(df_dropped_na) #This will print the DataFrame after removing rows with missing values.

#We can use the `fillna()` method to fill missing values in the DataFrame with a specified value or method.
#Example: Fill missing values in the 'Age' column with the mean of the 'Age' column.
mean_age = df[' Age'].mean() #This will calculate the mean of the 'Age' column.
df_filled_na = df.fillna({' Age': mean_age}) #This will fill missing values in the 'Age' column with the mean of the 'Age' column.
print(df_filled_na) #This will print the DataFrame after filling missing values in the 'Age' column with the mean of the 'Age' column.

#We can use the `replace()` method to replace specific values in the DataFrame with new values.
#Example: Replace all occurrences of 'New York' in the 'City' column with 'NYC'.
df_replaced = df.replace({' City': {'New York': 'NYC'}}) #This will replace all occurrences of 'New York' in the 'City' column with 'NYC'.
print(df_replaced) #This will print the DataFrame after replacing all occurrences of 'New York' in the 'City' column with 'NYC'.

#We can use the `astype()` method to change the data type of a column in the DataFrame.
#Example: Change the data type of the 'Age' column from float to int.

df[' Age'] = df[' Age'].astype(int) #This will change the data type of the 'Age' column from float to int.
print(df.dtypes) #This will print the data types of the columns in the DataFrame.

