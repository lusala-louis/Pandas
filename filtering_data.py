import pandas as pd
import openpyxl
df = pd.read_csv('pokemon_data.csv')

#Filter out specific columns
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
print(new_df)
print(' ')

#Resetting the index of the new data
reset_df = new_df.reset_index()
reset_df = reset_df.drop(columns = ['HP', 'Sp. Atk', 'Generation'])  #did this so the data could fit on my screen
print(reset_df)
print(' ')

#Accesssing specific strings in the data
with_mega = df.loc[df['Name'].str.contains('Mega')]
print(with_mega)
print(' ')
without_mega = df.loc[~df['Name'].str.contains('Mega')]
print(without_mega.head(20))
print(' ')