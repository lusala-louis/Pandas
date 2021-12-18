import pandas as pd
import openpyxl
df = pd.read_csv('pokemon_data.txt', delimiter = '\t')
#Getting all the column names
columns = df.columns
print(columns)
print(' ')
#Reading data from a specific column
name_column1 = df['Name']  #Gets all the items in the name column
name_column2 = df.Name  #Gets all the items in the name column (This only works on columns with one word names)
name_column3 = df['Name'][0:6]  #Gets the items in the column name from index 0 to index 6
print(name_column1)
print(' ')
print(name_column2)
print(' ')
print(name_column3)
print(' ')
#Reading data from multiple columns
multicolumn = df[['Name', 'Type 1', 'HP']]
print(multicolumn)
print(' ')
