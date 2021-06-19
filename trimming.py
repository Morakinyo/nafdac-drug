import pandas as pd

def trim_all_columns(df):
    """
    Trim whitespace from ends of each value across all series in dataframe
    """

    trim_strings = lambda x: x.strip() if isinstance(x, str) else x
    return df.applymap(trim_strings)