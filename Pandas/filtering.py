#Filtering: It is the process of selecting rows from a DataFrame based on some condition. In Pandas, filtering can be done using boolean indexing, the `query()` method, or the `loc[]` accessor.

import pandas as pd
df = pd.read_csv(r"C:\Users\pc\Desktop\New\Pandas\Data\data.csv")

#Filtering using boolean indexing
#Boolean indexing allows us to filter rows based on a condition that evaluates to True or False.

#Example: Filter rows where the 'Age' column has values greater than 30
filtered_df = df[df[' Age'] > 30]
print(filtered_df) #This will print the rows where the 'Age' column has values greater than 30.

#Filtering using the `query()` method
#The `query()` method allows us to filter rows using a string expression.
#Example: Filter rows where the 'Age' column has values greater than 30
filtered_df_query = df.query('` Age` > 30')
print(filtered_df_query) #This will print the rows where the 'Age' column has values greater than 30 using the `query()` method.

#Filtering using the `loc[]` accessor
#The `loc[]` accessor allows us to filter rows based on a condition and select specific columns at the same time.
#Example: Filter rows where the 'Age' column has values greater than 30 and select only the 'Name' and 'Age' columns
filtered_df_loc = df.loc[df[' Age'] > 30, [' Name', ' Age']]
print(filtered_df_loc) #This will print the rows where the 'Age' column has values greater than 30 and only the 'Name' and 'Age' columns using the `loc[]` accessor.


#Not only can we filter based on a single condition, but we can also filter based on multiple conditions using logical operators such as `&` (and), `|` (or), and `~` (not).

#Example: Filter rows where the 'Age' column has values greater than 30 and the 'City' column is 'New York'
filtered_df_multiple_conditions = df[(df[' Age'] > 30) & (df[' City'] == 'London')]
print(filtered_df_multiple_conditions) #This will print the rows where the 'Age' column has values greater than 30 and the 'City' column is 'New York'.

#Using or operator to filter rows where the 'Age' column has values greater than 30 or the 'City' column is 'New York'
filtered_df_or_condition = df[(df[' Age'] > 30) | (df[' City'] == 'London')]
print(filtered_df_or_condition) #This will print the rows where the 'Age' column has values greater than 30 or the 'City' column is 'New York'.

#Using not operator to filter rows where the 'Age' column does not have values greater than 30
filtered_df_not_condition = df[~(df[' Age'] > 30)]
print(filtered_df_not_condition) #This will print the rows where the 'Age' column does not have values greater than 30.

#Similarly, we have other operators like `isin()` to filter rows based on a list of values, and `between()` to filter rows based on a range of values, using which we can perform more complex filtering operations on our DataFrame.

#Example: Filter rows where the 'City' column is either 'New York' or 'Los Angeles'
filtered_df_isin = df[df[' City'].isin(['London', 'Los Angeles'])]
print(filtered_df_isin) #This will print the rows where the 'City' column is either 'New York' or 'Los Angeles'.

#Example: Filter rows where the 'Age' column is between 25 and 35
filtered_df_between = df[df[' Age'].between(25, 35)]
print(filtered_df_between) #This will print the rows where the 'Age' column is between 25 and 35.

#Example of other logical operators: We can also use other logical operators like `>`, `<`, `>=`, `<=`, and `!=` to filter rows based on different conditions.
#Example: Filter rows where the 'Age' column is not equal to 30
filtered_df_not_equal = df[df[' Age'] != 30]
print(filtered_df_not_equal) #This will print the rows where the 'Age' column is not equal to 30.

filtered_df_greater_equal = df[df[' Age'] >= 30]
print(filtered_df_greater_equal) #This will print the rows where the 'Age' column is greater than or equal to 30.

filtered_df_less_equal = df[df[' Age'] <= 30]
print(filtered_df_less_equal) #This will print the rows where the 'Age' column is less than or equal to 30.

filtered_df_less_than = df[df[' Age'] < 30]
print(filtered_df_less_than) #This will print the rows where the 'Age' column is less than 30. 