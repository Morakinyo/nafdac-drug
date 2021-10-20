import pandas as pd
from fuzzywuzzy import fuzz

def func(input_list):
    for i in range(len(input_list)):
        for j in range(len(input_list)):
            if i < j and fuzz.ratio(input_list[i], input_list[j]) >= 70:
                input_list[i] = input_list[j] # Keep the last encountered item
                # use following line to keep the first encountered item
                #input_list[j] = input_list[i]

df = pd.read_excel('drug-data-list.xlsx',sheet_name='Manufacturers')
result = []
for column in list(df):
    column_values = list(df[column])
    first_words = [x[:x.index(" ")] if " " in x else x for x in column_values]
    result.append(func(first_words))
new_df = pd.DataFrame(result).transpose()
new_df.columns = list(df)

print(new_df)

