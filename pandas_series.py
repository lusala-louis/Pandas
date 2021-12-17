#Lusala Louis
#Panda series
# Creating a series by passing a list of values, and a custom index label.
import pandas as pd
import numpy as np
s = pd.Series([1,2,3,np.nan,5,6], index=['A','B','C','D','E','F'])
print (s)