
#Aggregation refers to the process of summarizing or combining data in a DataFrame to obtain meaningful insights. In Pandas, we can perform aggregation using various methods such as `groupby()`, `agg()`, and built-in aggregation functions like `sum()`, `mean()`, `count()`, etc. It take multiple rows of data and condenses them into a single value or a smaller set of values based on specified criteria.

import pandas as pd
df = pd.read_csv(r"C:\Users\pc\Desktop\New\Pandas\Data\data.csv")
print(df) #This will print the original DataFrame.

df_grouped = df.groupby(' City') #This will group the DataFrame by the 'City' column.
#We can then apply aggregation functions to the grouped DataFrame to obtain summary statistics for each group.
#Example: Calculate the mean of the 'Age' column for each group in the 'City' column.
mean_age_per_city = df_grouped[' Age'].mean() #This will calculate the mean of the 'Age' column for each group in the 'City' column.
print(mean_age_per_city) #This will print the mean of the 'Age' column for each group in the 'City' column.

#We can also use the `agg()` method to apply multiple aggregation functions to the grouped DataFrame.
#Example: Calculate the mean and sum of the 'Age' column for each group in the 'City' column.
mean_sum_age_per_city = df_grouped[' Age'].agg(['mean', 'sum']) #This will calculate the mean and sum of the 'Age' column for each group in the 'City' column.
print(mean_sum_age_per_city) #This will print the mean and sum of the 'Age' column for each group in the 'City' column.

#We can also use built-in aggregation functions like `count()`, `min()`, `max()`, etc. to obtain summary statistics for each group.
#Example: Calculate the count, minimum, and maximum of the 'Age' column for each group in the 'City' column.
count_min_max_age_per_city = df_grouped[' Age'].agg(['count', 'min', 'max']) #This will calculate the count, minimum, and maximum of the 'Age' column for each group in the 'City' column.
print(count_min_max_age_per_city) #This will print the count, minimum, and maximum of the 'Age' column for each group in the 'City' column.

#We can also use the `transform()` method to apply aggregation functions to the grouped DataFrame and return a DataFrame with the same shape as the original DataFrame.
#Example: Calculate the mean of the 'Age' column for each group in the 'City' column and return a DataFrame with the same shape as the original DataFrame.
mean_age_per_city_transform = df_grouped[' Age'].transform('mean') #This will calculate the mean of the 'Age' column for each group in the 'City' column and return a DataFrame with the same shape as the original DataFrame.
print(mean_age_per_city_transform) #This will print the mean of the 'Age' column for each group in the 'City' column and return a DataFrame with the same shape as the original DataFrame.