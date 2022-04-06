import numpy as np
import pandas as pd

def unwanted_column(data_frame):
    list_of_columns = list(data_frame.columns)
    temp = []
    for i in list_of_columns:
        columns_with_unique_number = (i,data_frame[i].nunique())
        temp.append(columns_with_unique_number)
    array_unique = np.array(temp)
    array_one_unique=array_unique[array_unique[:,1]=='1']
    temp_list = list(array_one_unique[:,0])
    return(temp_list)

def column_null(data):
     dataframe_null = pd.DataFrame(data.isnull().sum())
     dataframe_null['1'] = dataframe_null[0]/data.shape[0]*100 #adding percentage of null in a column 
     dataframe_null = dataframe_null[dataframe_null['1']>50] #selecting the list with greater than 50% 
     c = list(dataframe_null.index) # list of column names with more than 50% null 
     return (c)