#Unlike series data frames are two dimensional
import pandas as pd
data = {'Gender' : ['F', 'M', 'M'], 'Emp_ID' : [ 'E01', 'E02', 'E03'], 'Age' : [25, 27, 25]}
#Specify the order of the column and column parameters
dataframe = pd.DataFrame(data,columns = ['Emp_ID', 'Gender', 'Age'])
print(dataframe)