import os
import pandas as pd


def load_data():
    data = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    return data

#ev_df = pd.read_csv('Electric_Vehicle_Population_Data.csv')
def test_filteredData_isEmpty():
    ev_df = load_data()
    county_counts = ev_df['County'].value_counts().reset_index()
    county_counts.columns = ['County', 'EV_Count']
    total_evs = county_counts['EV_Count'].sum()
    county_counts['Percentage'] = (county_counts['EV_Count'] / total_evs * 100)
    top_counties = county_counts.head(15)

     # Test if grouped data is empty
    assert not top_counties.empty, "Grouped data is empty."




def test_distrubution_of_evs_visualisationValid():
    # Test if file was created
    assert os.path.exists('Distrubution of EVs by County.png'), "The file was not created."



     
