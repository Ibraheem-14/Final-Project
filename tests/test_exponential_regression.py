import pandas as pd
import os 
from scipy.optimize import curve_fit
import numpy as np

def load_data():
    data = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    return data



def exp_model(x, a, b, c): 
    ev_df=load_data()
    bev_counts = ev_df[ev_df['Electric Vehicle Type'] == 'Battery Electric Vehicle (BEV)']['Model Year'].value_counts().sort_index()
    bev_counts = bev_counts[bev_counts.index ]
    years = bev_counts.index.values
    return a * np.exp(b * (x - years.min())) + c



def test_exponential_model_data_prediction():
    ev_df=load_data()
    bev_counts = ev_df[ev_df['Electric Vehicle Type'] == 'Battery Electric Vehicle (BEV)']['Model Year'].value_counts().sort_index()
    bev_counts = bev_counts[bev_counts.index ]
    years = bev_counts.index.values
    counts = bev_counts.values
    params, _ = curve_fit(exp_model, years, counts, p0=[100, 0.1, 100])
    future_years = np.linspace(years.min(), 2030, 100)
    predictions = exp_model(future_years, *params)

    # Test BEV counts
    assert len(bev_counts) > 0, "No BEV data found after filtering"

    # Test that years and counts align
    assert len(years) == len(counts), "Years and counts arrays have different lengths"
    
    #Test predictions length
    assert len(predictions) == len(future_years), "Predictions array length doesn't match future years"






