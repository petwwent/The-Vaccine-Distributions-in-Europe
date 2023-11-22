import pandas as pd
import plotly.express as px

def construct_choropleth():
    # Load your JSON data into a DataFrame, replace 'your_json_file.json' with the correct file path
    df = pd.read_json('json-Europe-SelectedColumns.json', lines=True)

    # Convert the 'date' column to datetime if it's not already
    df['date'] = pd.to_datetime(df['date'])

    # Extract year and month from the date
    df['year_month'] = df['date'].dt.to_period('M').astype(str)

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

    return fig  # Return the figure object
