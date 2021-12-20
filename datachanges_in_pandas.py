import pandas as pd
import openpyxl
df = pd.read_csv('pokemon_data.csv')

#Dropping a column from the data
df = df.drop(columns = ['Type 2', 'Generation'])
print(df.head(7))
print(' ')

#Adding a column to the data METHOD !
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def']  + df['Speed'] 
print(df.head(7))
print(' ')

#Adding a column to the data METHOD 2
df['Total'] = df.iloc[: , 3:9].sum(axis = 1)
print(df.head(10))
print(' ')

#Saving the new modified data as a separate file
#You cannot save to two new formats at the same time so you'll have to save one at a time 
#df = df.to_csv('modified.csv')
#df = df.to_excel('modified.xlsx')
df = df.to_csv('modified.txt', sep = '\t')