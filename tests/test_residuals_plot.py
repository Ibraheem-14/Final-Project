import pandas as pd
import os 



def test_boxplot_visualisation ():
    # Test that the visualisation has been made
    assert os.path.exists('Residuals Plot.png'), "The file was not created."
    