#Removing DataFrame row in Pandas based on column value.
#df = df[df.col/[] != value of interest in the column]


def filter_rows_by_values(df, col, values):
    return df[df[col].isin(values) == False]

#newdf = df.drop_duplicates(subset = ['','',...], keep = 'last').reset_index(drop = True)
