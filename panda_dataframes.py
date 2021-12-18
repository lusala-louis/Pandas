#Unlike series data frames are two dimensional
import pandas as pd
import openpyxl
#Entering data in the dataframe
data = {'Gender' : ['F', 'M', 'M'], 'Emp_ID' : [ 'E01', 'E02', 'E03'], 'Age' : [25, 27, 25]}
#Specify the order of the column and column parameters
dataframe = pd.DataFrame(data,columns = ['Emp_ID', 'Gender', 'Age'])
print(dataframe)
print(' ')  #Prints out an empty line to space the output better
#Loading data(csv format) into the pandas library from a file
df = pd.read_csv('pokemon_data.csv')
print(df) #Loads in all the data
print(' ')
print(df.head(5)) #Loads in only the top 5 rows of the data 
print(' ')
print(df.tail(5)) #Loads in only the bottom 5 rows of the data
print(' ')
#Loading data(xlsx format) into the pandas library from a file
df_xlsx = pd.read_excel('pokemon_data.xlsx')
print(df_xlsx.head(4))
print(' ')
#Loading data(txt format) into the pandas library from a file
df_txt = pd.read_csv('pokemon_data.txt', delimiter = '\t')
print(df_txt.head(4))
print(' ')