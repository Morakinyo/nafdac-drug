import os
import pandas as pd

drug_df = pd.DataFrame()
drug_excel = pd.ExcelFile('final-drug-2016-2020a.xlsx')
sheets = drug_excel.sheet_names
for sheet in sheets:
    df = drug_excel.parse(sheet_name=sheet, header=1, usecols='C:AJ')
    drug_df = drug_df.append(df, ignore_index=True)
drug_df.to_excel('drug-2016-2020a.xlsx')