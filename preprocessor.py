import pandas as pd
import numpy as np

def preprocess(w_data):
    # Let's replace the empty strings with NaN values
    w_data = w_data.replace(' ', np.nan)
    
    # Let's replace the question marks (?) with NaN values
    w_data = w_data.replace('?', np.nan)
    
    # Let's replace the question marks (.) with NaN values
    w_data = w_data.replace('.', np.nan)
    
    # Let's replace \N (always add an extra forward class)-> (\\N) with NaN values
    w_data = w_data.replace('\\N', np.nan)
    
    return w_data