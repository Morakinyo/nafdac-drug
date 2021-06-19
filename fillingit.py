#df[['','',....]].fillna(value='the value', inplace=True) # this however throws up SettingWithCopyWarning.
#df.fillna({"":"","":"",....}, inplace=True) 

#df.loc[df['col'].isnull(), 'col']='the renamed_value'
