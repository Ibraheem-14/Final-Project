# Exploring the progress of Washingtons state green vehicle objective

---
## 1. Overview
This repository contains the analysis and visualisations of a dataset aimed at the apoption of electric / hybrid vehicles. The dataset contains various  The dataset contains various information of the different vehicles registered such as the make, model, county of registration and price. I examined the distrubution of the number of EVs in each state and the distrubution of the price of vehicle types (BEVs,PHEVs). I also looked into the trajectory of the move to full electric by 2030. These analytics gave great insights to where Washington is headed and what chnages could be made to make sure targets are hit.

The hypothesis investigated was:
> "The current trajectory of the move to all electric vehicles by 2030 and the possible factors that are inhibiting it"

---

## 2. Project Structure
- **`.circleci/`**: Configuration files for CircleCI integration for testing every commit.
- **`Visualisations/`**: Stores all visualisations related to the analysis.
- **`tests/`**: Includes all test files ran by CircleCI for every commit.
- **`Electric_Vehicle_Population_Data.csv`**: The dataset used for the analysis.
- **`README.md`**: Project documentation.
- **`data_analysis.py`**: Python script for data cleaning, data analysis, and creating visualisations.
- **`requirements.txt`**: Lists Python dependencies needed to run the analysis.

---

## 3. Dataset
The dataset was sourced from the Missing Migrants Project, by the International Organization For Migration:
- **Size**: 17,474 rows and 25 columns before preprocessing.
- **Pre-processing**: Removed unnecessary columns, handled null values, and filtered data for analysis.

The dataset provides information on:
- Incident date, migration routes, and causes of death.
- Demographic details such as gender and age.
- Total number of dead and missing.

---

## 4. How to Run
To run the analysis locally:
1. Clone the repository:
   ```bash
   git clone https://github.com/Ibraheem-14/Final-Project.git
   cd Final-Project
 2. Install the required libraries from 'requrements.txt':
    ```bash
    pip install -r requirements.txt

4. Run the data analysis script - 'data_analysis.py':
   ```bash
   python data_analysis.py

6. To execute the test suite:
    ```bash
    pytest tests

7. View the visualisations:

   Navigate inside the 'Visualisations' folder to do so.