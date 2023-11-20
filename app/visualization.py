import plotly.express as px
import json
import pandas as pd
import plotly.graph_objects as go



# Load your Europe data
europe_df = pd.read_json('json-Europe-SelectedColumns.json', lines=True)

# Replace 'date', 'total_vaccinations', and 'location' with your actual column names
# Convert the 'date' column to datetime if it's not already
europe_df['date'] = pd.to_datetime(europe_df['date'])

# Extract year and month from the date
europe_df['year_month'] = europe_df['date'].dt.to_period('M').astype(str)  # Convert Period to string

# Group by location and year_month, aggregating total vaccinations
grouped_df = europe_df.groupby(['location', 'year_month'], as_index=False).agg({
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
fig = px.choropleth(grouped_df,
                    locations='location',
                    locationmode='country names',
                    color='total_vaccinations',
                    hover_name='location',
                    hover_data=grouped_df.columns,
                    animation_frame='year_month',
                    color_continuous_scale='Viridis',
                    title="Total Vaccinations Choropleth Across Locations in Europe",
                    width=1200,
                    height=800,
                    projection='natural earth'
                    )

# Use Europe-specific projection and set the initial center and zoom
fig.update_geos(
    projection_type="natural earth",
    center=dict(lon=10, lat=50),
    scope="europe",
)


# Show the plot
fig.show()

