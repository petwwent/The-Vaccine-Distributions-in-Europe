### The Distribution of Vaccines Across Countries in Europe between 2021-2023


### Description:

This repository contains Python code for visualizing the distribution of vaccines across all the countries in Europe from 2021 to 2023 and it's trend. The data is sourced from [https://ourworldindata.org/covid-cases] which came in CSV format, i had to change it to json format using the pandas library specifically, select the continent relevant to my project which is Europe and save it in a different json file, then select the columns that would be relevant to my visualization also with the pandas library and handled missing data using pandas functions to check for and manage null or NaN values, techniques such as filling missing values with zeros or using interpolation were applied. Then my visualization uses a stacked bar chart created with Plotly Express, providing an interactive and dynamic representation of the vaccination distributions across European countries and over time.

![chart-video](https://github.com/PrincepaulIzuogu/The-Vaccine-Distributions-in-Europe/assets/123191250/6b1d7898-82bd-42f8-aa64-6c67b090eba8)
![newplot (2)](https://github.com/PrincepaulIzuogu/The-Vaccine-Distributions-in-Europe/assets/123191250/7697c5df-3928-4bc3-bea4-ae044cb6aec5)
![Screenshot 2023-12-06 194511](https://github.com/PrincepaulIzuogu/The-Vaccine-Distributions-in-Europe/assets/123191250/bfcead94-de45-46a2-946c-a51ee64470f0)
![Screenshot 2023-12-06 194600](https://github.com/PrincepaulIzuogu/The-Vaccine-Distributions-in-Europe/assets/123191250/35c4a1af-7e7d-48d4-ae89-34e92b61c939)



## Key User Group



 
**The Director of European Centre for Disease Prevention and Control:** The Director of ECDC is responsible for leading the ECDC’s work in strengthening Europe’s defence against infectious disease.

## A Problem the The Director of ECDC Encouters

To compare the distribution of (2021-2023) without going through the database or raw data.

## My Solution

This project is the solution to this problem, The Director of ECDC can use this choropleth map to easily understand the distribution of vaccines across different European countries within the specified period of time, due to the data i selected for this visualization, it is easier for the Director of ECDC to identify the following: 
    countries,
    date,
    total_cases,
    population,
    total_vaccinations,
    people_vaccinated,
    people_fully_vaccinated,
    total_vaccinations_per_hundred,
    people_vaccinated_per_hundred, and
    people_fully_vaccinated_per_hundred for each and every European countries.

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
- Compare the total cases and vaccine distribution across different countries or regions.
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
2. Install the requirements
3. Run the uvicorn on Python environment or run in github codespaces
4. Explore the interactive choropleth map and customize it as needed.
