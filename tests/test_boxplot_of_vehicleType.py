import pandas as pd
import os 

def load_data():
    data = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    return data

def test_boxplot_vehicleType():
    ev_df_reRead = load_data()
    ev_df_reRead =  pd.read_csv('Electric_Vehicle_Population_Data.csv')
    ev_df_reRead = ev_df_reRead[(ev_df_reRead['Base MSRP'] != 0) & (ev_df_reRead['Base MSRP'] != 845000)].copy()
    ev_df_reRead['Vehicle Type'] = ev_df_reRead['Electric Vehicle Type'].map({'Battery Electric Vehicle (BEV)': 'BEV','Plug-in Hybrid Electric Vehicle (PHEV)': 'PHEV'})
    # Test if grouped datas empty 
    assert not ev_df_reRead.empty, "Grouped data is empty."
    # Test that vehicle column exists 
    assert 'Vehicle Type' in ev_df_reRead.columns, "'Vehicle Type' column not found in DataFrame"
    # Test no invalid prices are present
    assert not any(ev_df_reRead['Base MSRP'].isin([0, 845000])), "Found forbidden MSRP values (0 or 845000)"

def test_boxplot_visualisation ():
    # Test that the visualisation has been made
    assert os.path.exists('Boxplot of Vehicle Type Against Price.png'), "The file was not created."
