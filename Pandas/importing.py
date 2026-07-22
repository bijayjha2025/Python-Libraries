#In this, we will learn how to work with importing data in pandas. Importing data is a crucial step in data analysis, as it allows us to bring external data into our Python environment for further processing and analysis. Pandas provides various functions to import data from different file formats, such as CSV, Excel, SQL databases, and more.

#To import data from a CSV file, we can use the read_csv() function provided by pandas. This function takes the file path of the CSV file as an argument and returns a DataFrame object containing the data from the CSV file. We can also specify additional parameters to customize the importing process, such as specifying the delimiter, handling missing values, and selecting specific columns.


import pandas as pd
df = pd.read_csv(r"C:\Users\pc\Desktop\New\Pandas\Data\data.csv")
#Here, read_csv("data.csv") is a function that reads the CSV file located at the specified file path and returns a DataFrame object containing the data from the CSV file. The resulting DataFrame will have columns corresponding to the headers in the CSV file and rows corresponding to the data entries.

print(df)


df1 = pd.read_json(r"C:\Users\pc\Desktop\New\Pandas\Data\data.json", orient="records")
print(df1)

#Here, orient = records specifies that the JSON data is in a list of records format, where each record is represented as a dictionary. The resulting DataFrame will have columns corresponding to the keys in the dictionaries and rows corresponding to the individual records.