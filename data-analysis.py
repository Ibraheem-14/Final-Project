import pandas as pd
import pytest
import matplotlib.pyplot as plt


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

