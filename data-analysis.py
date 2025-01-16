import pandas as pd
import pytest
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.optimize import curve_fit

# Load EV data
ev_df = pd.read_csv('Electric_Vehicle_Population_Data.csv')
print(ev_df.head())



# Horizontal bar chart showing the distrubution of EVs by county
county_counts = ev_df['County'].value_counts().reset_index()
county_counts.columns = ['County', 'EV_Count']
total_evs = county_counts['EV_Count'].sum()
county_counts['Percentage'] = (county_counts['EV_Count'] / total_evs * 100)
top_counties = county_counts.head(15)

colors = ['#08306b','#08419c','#0b4db3','#0d59ca','#0f66e2','#1174f0','#2182f4','#3190f8','#419efc','#51acff','#61baff','#71c8ff','#81d6ff','#91e4ff','#a1f2ff']  

plt.figure(figsize=(12, 8))

bars = plt.barh(top_counties['County'], top_counties['EV_Count'],color=colors)

for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + 100, i, f'{top_counties["Percentage"].iloc[i]:.1f}%', va='center', ha='left')  

plt.xlabel('Number of Electric Vehicles', fontsize=12, fontweight='bold')
plt.ylabel('County', fontsize=12, fontweight='bold')
plt.title('Electric Vehicle Distribution Across Washington Counties (Top 15 Counties by Adoption)')

ax = plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

plt.savefig('Distrubution of EVs by County')




# Boxplot comapring the distrubution of price of BEVs comapred to PHEVs
ev_df_reRead =  pd.read_csv('Electric_Vehicle_Population_Data.csv')
ev_df_reRead = ev_df_reRead[(ev_df_reRead['Base MSRP'] != 0) & (ev_df_reRead['Base MSRP'] != 845000)].copy()

ev_df_reRead['Vehicle Type'] = ev_df_reRead['Electric Vehicle Type'].map({'Battery Electric Vehicle (BEV)': 'BEV','Plug-in Hybrid Electric Vehicle (PHEV)': 'PHEV'})

fig, ax = plt.subplots(figsize=(12, 8))

sns.boxplot(x='Vehicle Type', y='Base MSRP', data=ev_df_reRead, palette=['#084594', '#2171b5'], width=0.5, showfliers=False, ax=ax)  


ax.set_title('Price Distribution: BEV vs PHEV (Excluding Outliers)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Vehicle Type', fontsize=12, fontweight='bold')
ax.set_ylabel('Base MSRP ($)', fontsize=12, fontweight='bold')

fig.savefig('Boxplot of Vehicle Type Against Price')


#Filtered dataset for the number of each vehicle type eligible for CAFV
ev_df = pd.read_csv('Electric_Vehicle_Population_Data.csv')
phev_cafv = ev_df[(ev_df['Electric Vehicle Type'] == 'Plug-in Hybrid Electric Vehicle (PHEV)') & (ev_df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'] == 'Clean Alternative Fuel Vehicle Eligible')].shape[0]
bev_cafv = ev_df[(ev_df['Electric Vehicle Type'] == 'Battery Electric Vehicle (BEV)') & (ev_df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'] == 'Clean Alternative Fuel Vehicle Eligible')].shape[0]
total_phev = ev_df[ev_df['Electric Vehicle Type'] == 'Plug-in Hybrid Electric Vehicle (PHEV)'].shape[0]
total_bev = ev_df[ev_df['Electric Vehicle Type'] == 'Battery Electric Vehicle (BEV)'].shape[0]
summary_df = pd.DataFrame({'Vehicle Type': ['PHEV', 'BEV'],'CAFV Eligible Count': [phev_cafv, bev_cafv],'Total Vehicles':[total_phev,total_bev]})
summary_df['Total Vehicles'] = [total_phev, total_bev]
print(summary_df.head())



# Exponential predictive model

# Preperation of data
bev_counts = ev_df[ev_df['Electric Vehicle Type'] == 'Battery Electric Vehicle (BEV)']['Model Year'].value_counts().sort_index()
bev_counts = bev_counts[bev_counts.index ]
years = bev_counts.index.values
counts = bev_counts.values

# Defining of the exponential model
def exp_model(x, a, b, c): 
    return a * np.exp(b * (x - years.min())) + c
params, _ = curve_fit(exp_model, years, counts, p0=[100, 0.1, 100])

# Predictions
future_years = np.linspace(years.min(), 2030, 100)
predictions = exp_model(future_years, *params)

plt.figure(figsize=(12, 7))
plt.plot(years, counts, 'b-', label='Historical Data', linewidth=2, marker='o',color='#0b4db3')
plt.plot(future_years, predictions, 'r--', label='Prediction', linewidth=2,color='red')
plt.axvline(x=2025, color='gray', linestyle=':', alpha=0.5, label='Current Year')

plt.title('BEV Growth: Historical Data and Future Predictions',fontsize=14, fontweight='bold')
plt.xlabel('Year',fontsize=12, fontweight='bold')
plt.ylabel('Number of BEVs',fontsize=12, fontweight='bold')

plt.legend()
plt.xticks(np.arange(min(years), 2032, 2), rotation=45)
plt.savefig('Exponential Regression Model')



# Plot of residuals 
bev_counts = ev_df[ev_df['Electric Vehicle Type'] == 'Battery Electric Vehicle (BEV)']['Model Year'].value_counts().sort_index()
years = bev_counts.index.values
counts = bev_counts.values


def exp_model(x, a, b, c): 
    return a * np.exp(b * (x - years.min())) + c

params, _ = curve_fit(exp_model, years, counts, p0=[100, 0.1, 100])


predictions = exp_model(years, *params)
residuals = counts - predictions

# Create residual plot
plt.figure(figsize=(12, 7))
plt.scatter(years, residuals, color='#0b4db3')
plt.axhline(y=0, color='red', linestyle='--')
plt.grid(True, alpha=0.2)

plt.title('Residual Plot: BEV Growth Model', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Residual Value (Actual - Predicted)', fontsize=12, fontweight='bold')
plt.savefig('Residuals Plot')