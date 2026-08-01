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