### The Distribution of Vaccines Across Countries in Europe between 2020-2023


### Description:

This repository contains Python code for visualizing the distribution of vaccines across all the countries in Europe from 2020 to 2023 and it's trend. The data is sourced from [https://ourworldindata.org/covid-cases] which came in CSV format, i had to change it to json format using the pandas library specifically, select the continent relevant to my project which is Europe and save it in a different json file, then select the columns that would be relevant to my visualization also with the pandas library and handled missing data using pandas functions to check for and manage null or NaN values, techniques such as filling missing values with zeros or using interpolation were applied. Then my visualization uses a choropleth map created with Plotly Express, providing an interactive and dynamic representation of the pandemic's spread, i also implemented a heatmap to show the distribution and intensity of cases across countries and over time.
![Screenshot 2023-11-19 203714](https://github.com/PrincepaulIzuogu/The-trend-of-COVID-19-cases-in-Europe-over-time/assets/123191250/71723f59-186c-4c2a-9139-bc5ed0f76fee)
![Screenshot 2023-11-19 204529](https://github.com/PrincepaulIzuogu/The-trend-of-COVID-19-cases-in-Europe-over-time/assets/123191250/2ff91535-d9a1-42f3-ab43-8c25c038bc15)
![Screenshot 2023-11-19 204655](https://github.com/PrincepaulIzuogu/The-trend-of-COVID-19-cases-in-Europe-over-time/assets/123191250/39cf2ea1-50de-4a83-85a9-ae8f15d9f47f)



## Key User Group


**European Policymakers:** My key user for this project are the European policymakers, they can use this choropleth map to easily understand the distribution of vaccines across different European countries within the specified period of time, due to the data i selected for this visualization, it is easier for these European policymakers to identify the following: 
    countries
    date
    total_cases
    population
    total_vaccinations
    people_vaccinated
    people_fully_vaccinated
    total_vaccinations_per_hundred
    people_vaccinated_per_hundred
    people_fully_vaccinated_per_hundred

| iso_code | continent | location |       date      | total_cases | population | total_vaccinations | people_vaccinated | fully_vaccinated | Total_v_per_100 | vaccinated_per_100 | fully_vaccinated_per100|
|----------|-----------|----------|-----------------|--------------|------------|---------------------|-------------------|-------------------|-----------------|--------------------|---------------------|
|   ALB    |  Europe   | Albania  | 1578009600000   |     NaN      |  2842318   |        NaN          |        NaN        |        NaN        |       NaN       |        NaN         |           NaN       |
|   ALB    |  Europe   | Albania  | 1578096000000   |     NaN      |  2842318   |        NaN          |        NaN        |        NaN        |       NaN       |        NaN         |           NaN       |
|   ALB    |  Europe   | Albania  | 1578182400000   |     NaN      |  2842318   |        NaN          |        NaN        |        NaN        |       NaN       |        NaN         |           NaN       |
|   ALB    |  Europe   | Albania  | 1578268800000   |     NaN      |  2842318   |        NaN          |        NaN        |        NaN        |       NaN       |        NaN         |           NaN       |
|   ALB    |  Europe   | Albania  | 1578355200000   |     NaN      |  2842318   |        NaN          |        NaN        |        NaN        |       NaN       |        NaN         |           NaN       |




## User Objectives

Users aim to:

- Understand the overall distribution of vaccines in Europe.
- Understand the overall trend of COVID-19 cases in Europe.
- Compare the total cases and vaccine distribution across different countries or regions.
- Identify patterns and variations in the spread of the virus over the selected timeframe.
- compare the distributed vaccines to the total people fully vacinated.
- To identify or rather, calculate how the next distribution would be done.

## Visualization Strategy and how it help users achieve task effectively and efficiently

I use a choropleth map for the visualization and then heatmap for the colors, i think this visualization pattern i chose is the best because:

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
