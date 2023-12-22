### The Distribution of Vaccines Across Countries in Europe between 2021-2023


### Description:

This repository contains Python code for visualizing the distribution of vaccines across all the countries in Europe from 2021 to 2023 and it's trend. The data is sourced from [https://ourworldindata.org/covid-cases] which came in CSV format, i had to change it to json format using the pandas library specifically, select the continent relevant to my project which is Europe and save it in a different json file, then select the columns that would be relevant to my visualization also with the pandas library and handled missing data using pandas functions to check for and manage null or NaN values, techniques such as filling missing values with zeros or using interpolation were applied. Then my visualization uses a stacked bar chart created with Plotly Express, providing an interactive and dynamic representation of the vaccination distributions across European countries and over time.


https://github.com/PrincepaulIzuogu/The-Vaccine-Distributions-in-Europe/assets/123191250/cab34f81-bd2d-44ea-9eaa-a8b5cd8b7aff

![Screenshot 2023-12-22 145626](https://github.com/PrincepaulIzuogu/The-Vaccine-Distributions-in-Europe/assets/123191250/89527986-105b-490d-bf78-38ac2e46eb67)

![Screenshot 2023-12-22 145723](https://github.com/PrincepaulIzuogu/The-Vaccine-Distributions-in-Europe/assets/123191250/850deadc-a9de-4ecd-a779-b23200c195d4)

![Screenshot 2023-12-22 145800](https://github.com/PrincepaulIzuogu/The-Vaccine-Distributions-in-Europe/assets/123191250/ac354bae-053c-4f90-a896-9071ad334145)



## Key User Group
**The Director of European Centre for Disease Prevention and Control:** The Director of ECDC is responsible for leading the ECDC’s work in strengthening Europe’s defence against infectious disease.

## A Problem the The Director of ECDC Encouters
To specifically compare the distribution of covid-19 vaccinations of all the European countries between 2021-2023 in order to determine how the next distribution would be made without going through the database or raw data.

## My Solution

This app is the solution to this problem, The Director of ECDC can use this choropleth map to easily understand the distribution of vaccines across different European countries within the specified period of time, due to the data i selected for this visualization, it is easier for the Director of ECDC to identify the following: 
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

https://github.com/PrincepaulIzuogu/The-Vaccine-Distributions-in-Europe/assets/123191250/6748dafa-39a0-423a-b5a4-37172ab6343d

https://github.com/PrincepaulIzuogu/The-Vaccine-Distributions-in-Europe/assets/123191250/1939016c-32cf-4425-a06a-62e6f3957f72


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
