import pandas as pd
import numpy as np
df = pd.read_csv("../data/starter_data.csv")

def get_summary_stats(df):
    means = df.select_dtypes(include=[np.number]).mean().to_numpy()
    
    
    return means





