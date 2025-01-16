import pandas as pd
import os 

def load_data():
    data = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    return data

def test_num_vehicles_eligible():
    ev_df = load_data()
    phev_cafv = ev_df[(ev_df['Electric Vehicle Type'] == 'Plug-in Hybrid Electric Vehicle (PHEV)') & (ev_df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'] == 'Clean Alternative Fuel Vehicle Eligible')].shape[0]
    bev_cafv = ev_df[(ev_df['Electric Vehicle Type'] == 'Battery Electric Vehicle (BEV)') & (ev_df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'] == 'Clean Alternative Fuel Vehicle Eligible')].shape[0]
    total_phev = ev_df[ev_df['Electric Vehicle Type'] == 'Plug-in Hybrid Electric Vehicle (PHEV)'].shape[0]
    total_bev = ev_df[ev_df['Electric Vehicle Type'] == 'Battery Electric Vehicle (BEV)'].shape[0]
    summary_df = pd.DataFrame({'Vehicle Type': ['PHEV', 'BEV'],'CAFV Eligible Count': [phev_cafv, bev_cafv],'Total Vehicles':[total_phev,total_bev]})
    summary_df['Total Vehicles'] = [total_phev, total_bev]

    # Test that vehicle column exists 
    assert not summary_df.empty, "Grouped data is empty."
     # Test Vehicle Type contains correct values
    assert set(summary_df['Vehicle Type']) == {'PHEV', 'BEV'}, "Vehicle Type column missing expected values"
 