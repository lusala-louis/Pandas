import pandas as pd
import openpyxl
df = pd.read_csv('pokemon_data.txt', delimiter = '\t')
#Getting all the column names
columns = df.columns
print(columns)
print(' ')   #Prints out an empty line to space the output 
print(' ')

#Reading data from a specific column
name_column1 = df['Name']  #Gets all the items in the name column
name_column2 = df.Name  #Gets all the items in the name column (This only works on columns with one word names)
name_column3 = df['Name'][0:6]  #Gets the items in the column name from index 0 to index 6
print(name_column1)
print(' ')  #Prints out an empty line to space the output better
print(name_column2)
print(' ') 
print(name_column3)
print(' ')  
#Reading data from multiple columns
multicolumn = df[['Name', 'Type 1', 'HP']]
print(multicolumn)
print(' ')  

#Reading data from specific rows
row = df.iloc[1]
print(row)
print(' ')  
rows = df.iloc[1:4]
print(rows)
print(' ')  
row2_1 = df.iloc[2, 1]  #Gets the data from the third row the second column
print(row2_1)
print(' ')
#Iterating through rows
for index, row in df.iterrows() :
    print(index, row)
print(' ')

#Getting the location of specific items in the data
location = df.loc[df['Type 1'] == 'Fire']
print(location)
print(' ')
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
