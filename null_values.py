import pandas as pd
import numpy as np

#Counting the null rows
#is_NaN = df.isnull()
#row_has_NaN = is_NaN.any(axis=1)
#rows_with_NaN = df[row_has_NaN]

#Counting the null columns
#dataframe = pd.read_excel(filepath/name)
#null_columns = dataframe.columns[train.isnull().any()]
#train[null_columns].isnull().sum()

#To see the rows with a single null column of Interest
#print(dataframe[dataframe["column_name"].isnull()][null_columns])


#To return every row that contains at least one null value
#print(dataframe[dataframe.isnull().any(axis=1)][null_columns].head())

def nans(df):
    return df[df.isnull().any(axis=1)]

def nullcols(df):
    null_columns = df.columns[df.isnull().any()]
    return df[null_columns].isnull().sum()

#def nullcol(df,column=columns.values):
    #null_columns = df.columns[df.isnull().any()]
    #print(df[df[column].isnull()][null_columns])

# To select column where null values
#df.loc[df.column/[column].isnull(),:]

def nullqty(df, qty_of_nuls=1):
    return df.iloc[df[(df.isnull().sum(axis=1) >= qty_of_nuls)].index]

# Helper : Gets NaNs for some row
def row_nan_sums(df):
    sums = []
    for row in df.values:
        sum = 0
        for elk in row:
            if elk != elk: # np.nan is never equal to itself.
                sum+=1
        sums.append(sum)
    return sums 
# Returns a list of indices for rows with k+ nans
def query_k_plus_sums(df,k):
    sums = row_nan_sums(df)
    indices = []
    i = 0
    for sum in sums:
        if (sum >= k):
            indices.append(i)
        i += 1
    return indices

# drop the rows from the dataframe
#df.drop(query_k_plus_sums(df, 2), inplace=True)

# Reshuffle up data(if one does not do this, the indices won't reset)
#df = df.sample(frac=1).reset_index(drop=True)

