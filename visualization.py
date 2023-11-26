import pandas as pd
import plotly.express as px
import json

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, FileResponse
from typing import Optional
from visualization import construct_choropleth  # Import the function
import os
import uvicorn

def construct_choropleth(location=None, year_month=None, output_file=None):
    # Load your JSON data into a DataFrame, replace 'your_json_file.json' with the correct file path
    df = pd.read_json('data.json')

    # Convert the 'date' column to datetime if it's not already
    df['date'] = pd.to_datetime(df['date'])

    # Extract year and month from the date
    df['year_month'] = df['date'].dt.to_period('M').astype(str)

    # Filter data based on the provided location or year_month
    if location and year_month:
        # Return data for the specified location on the specified date
        df = df[(df['location'] == location) & (df['year_month'] == year_month)]
    elif location:
        # Return all data for the specified location across different dates
        df = df[df['location'] == location]
    elif year_month:
        # Return data only for the specified date, irrespective of the location
        df = df[df['year_month'] == year_month]

    # Group by location and year_month, aggregating total vaccinations
    grouped_df = df.groupby(['location', 'year_month'], as_index=False).agg({
        'iso_code': 'first',
        'continent': 'first',
        'date': 'first',
        'total_cases': 'sum',
        'population': 'first',
        'total_vaccinations': 'sum',
        'people_vaccinated': 'sum',
        'people_fully_vaccinated': 'sum',
        'total_vaccinations_per_hundred': 'sum',
        'people_vaccinated_per_hundred': 'sum',
        'people_fully_vaccinated_per_hundred': 'sum'
    })

    # Create a choropleth using Plotly Express based on total vaccinations
    fig = px.choropleth(
        grouped_df,
        locations='location',
        locationmode='country names',
        color='total_vaccinations',
        hover_name='location',
        hover_data=grouped_df.columns,
        animation_frame='year_month',
        color_continuous_scale='Viridis',
        title="Total Vaccinations Choropleth Across Locations",
        width=1200,
        height=800,
        projection='natural earth'
    )

    # Use Europe-specific projection and set the initial center and zoom
    fig.update_geos(
        projection_type="natural earth",
        center=dict(lon=10, lat=50),
        scope="europe"
    )

    # Convert the filtered data to JSON
    choropleth_json = fig.to_json()

    # If an output file path is provided, write the filtered data to a JSON file
    if output_file:
        with open(output_file, 'w') as file:
            file.write(choropleth_json)

    return choropleth_json
