import pandas as pd
import openpyxl
df = pd.read_csv('pokemon_data.csv')
#Get a quick overview of the data
print(df.describe())
print(' ')

#Sorting the values
ascending = df.sort_values('Name')
print(ascending)
print(' ')
descending = df.sort_values('Name', ascending = False)
print(descending)
print(' ')

#You can also sort multiple columns 
sort_columns= df.sort_values(['Type 1', 'HP'], ascending = False)
print(sort_columns)
print(' ')
sort_columns2 = df.sort_values(['Type 1', 'HP'], ascending = [1,0])
print(sort_columns2)
print(' ')
