### The trend of COVID-19 cases in Europe between 2020-2023


### Description:

This repository contains Python code for visualizing the total COVID-19 cases in Europe from 2020 to 2023 and it's trend. The data is sourced from [https://ourworldindata.org/covid-cases] which came in CSV format, i had to change it to json format using the pandas library specifically, then select the columns that would be relevant to my visualization also with the pandas library and handled missing data using pandas functions to check for and manage null or NaN values, techniques such as filling missing values with zeros or using interpolation were applied. Then my visualization uses a choropleth map created with Plotly Express, providing an interactive and dynamic representation of the pandemic's spread, i also implemented a heatmap to show the distribution and intensity of cases across countries and over time.

![project_image](https://github.com/PrincepaulIzuogu/The-trend-of-COVID-19-cases-in-Europe-over-time/assets/123191250/7f040bfd-8eea-4c6a-bb4d-0e45d7c7ab32)


## Key User Group

Our key user group includes:

**Researchers:** Analyzing the geographical spread of COVID-19 in Europe for academic purposes.
**Policymakers:** Making informed decisions based on the current state and trends of the pandemic.
**General Public:** Staying informed about the COVID-19 situation in their region and across Europe.

## User Objectives

Users aim to:

- Understand the overall trend of COVID-19 cases in Europe.
- Compare the total cases across different countries or regions.
- Identify patterns and variations in the spread of the virus over the selected timeframe.

## Visualization Strategy and how it help users achieve task effectively and efficiently

I use a choropleth map because:

- It provides a geographical representation of total cases.
- The animation feature allows for the observation of temporal changes.
- Users can interactively explore data for specific timeframes.

## Additional Features

- **Filtering Options:** Users can customize the timeframe for a more focused view.
- **Hover Information:** Interactive tooltips provide detailed information about each country's total cases.

## How to Use

1. Clone the repository.
2. Run the Python script (`covid19_visualization.py`) in a Jupyter Notebook or any Python environment.
3. Explore the interactive choropleth map and customize it as needed.
