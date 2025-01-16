import os 
import pandas as pd

def test_FileRead():
    ev_df = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    assert not ev_df.empty,"Dataset has not been read"

    
def test_isEmpty():
    ev_df = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    assert len(ev_df) > 0,"Dataset has no data"



