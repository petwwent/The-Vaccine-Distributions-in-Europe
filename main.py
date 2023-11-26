from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, FileResponse
from typing import Optional
import pandas as pd
import plotly.express as px
import os
import uvicorn

app = FastAPI()

# Get the path to the current file directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# Sample JSON data (Replace this with your actual JSON data or data retrieval logic)
# Sample data for demonstration purposes only
data = {
    "location": ["Germany", "France", "Italy"],
    "date": ["2022-04-01", "2022-04-01", "2022-04-01"],
    "total_cases": [1000, 1500, 800],
    "population": [83000000, 67000000, 60360000],
    "total_vaccinations": [20000000, 18000000, 15000000],
    "people_vaccinated": [12000000, 10000000, 8000000],
    "people_fully_vaccinated": [8000000, 8000000, 7000000],
    "total_vaccinations_per_hundred": [24.1, 26.9, 24.9],
    "people_vaccinated_per_hundred": [14.5, 14.9, 13.3],
    "people_fully_vaccinated_per_hundred": [9.6, 11.9, 11.6]
}

df = pd.DataFrame(data)

def construct_choropleth(location=None, year_month=None, output_file=None):
    # Convert the 'date' column to datetime if it's not already
    df['date'] = pd.to_datetime(df['date'])

    # Extract year and month from the date
    df['year_month'] = df['date'].dt.to_period('M').astype(str)

    # Filter data based on the provided location or year_month
    if location and year_month:
        # Return data for the specified location on the specified date
        filtered_data = df[(df['location'] == location) & (df['year_month'] == year_month)]
    else:
        # Return empty DataFrame if no filter is applied
        filtered_data = pd.DataFrame()

    return {
        "mapData": get_choropleth_data(),
        "filteredData": filtered_data.to_dict(orient='records')
    }

def get_choropleth_data():
    # Group by location and year_month, aggregating total vaccinations
    grouped_df = df.groupby(['location', 'year_month'], as_index=False).agg({
        'location': 'first',
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

    # Convert the choropleth data to JSON
    choropleth_json = fig.to_json()

    return choropleth_json

@app.get("/", response_class=FileResponse)
async def index():
    return FileResponse(os.path.join(dir_path, "templates/index.html"))

@app.get("/get-choropleth-data")
async def get_choropleth_data(location: Optional[str] = Query(None), year_month: Optional[str] = Query(None)):
    choropleth_data = construct_choropleth(location=location, year_month=year_month)
    return JSONResponse(content=choropleth_data)

@app.get("/aboutus", response_class=FileResponse)
async def aboutus():
    return FileResponse(os.path.join(dir_path, "templates/aboutus.html"))

@app.get("/aboutapp", response_class=FileResponse)
async def aboutapp():
    return FileResponse(os.path.join(dir_path, "templates/aboutapp.html"))

@app.get("/static/{file_path:path}")
async def serve_static(file_path: str):
    static_file_path = os.path.join(dir_path, "static", file_path)
    if os.path.exists(static_file_path):
        return FileResponse(static_file_path)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
