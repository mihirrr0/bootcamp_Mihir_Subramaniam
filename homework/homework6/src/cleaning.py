import pandas as pd
import numpy as np

def fill_missing_median(df, columns):
    df_copy = df.copy()
    for col in columns:
        if col in df_copy.columns:
            median_value = df_copy[col].median()
            df_copy[col] = df_copy[col].fillna(median_value)
        else:
            print(f"warning: column: '{col}' not found in DataFrame")
    return df_copy

def drop_missing(df, threshold=0.5):
    df_copy = df.copy()
    missing_proportion = df_copy.isna().mean(axis=1)
    return df_copy[missing_proportion <= threshold]

def normalize_data(df, columns):
    df_copy = df.copy()
    for col in columns:
        if col in df_copy.columns:
            col_min = df_copy[col].min()
            col_max = df_copy[col].max()
            if col_max != col_min:  
                df_copy[col] = (df_copy[col] - col_min) / (col_max - col_min)
            else:
                print(f"warning: Ccolumn: '{col}' has no variance, skipping normalization")
        else:
            print(f"warning: column: '{col}' not found in DataFrame")
    return df_copy