import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


def convert_csv_to_json(csv_Africa_covid_data, csv_Europe_covid_data, json_Africa_output, json_Europe_output):
    # Read CSV files into pandas DataFrames
    df_Europe = pd.read_csv(csv_Europe_covid_data)

    # Convert DataFrames to JSON and save to new files
    df_Europe.to_json(json_Europe_output, orient='records', lines=True)

# Replace  'csv-Europe-covid-data.csv' to 'json-Europe-output.json' with your actual filenames
convert_csv_to_json('csv-Europe-covid-data.csv','json-Europe-output.json')



# this is a world data, filter out Europe

# Load the Europe JSON data
with open('json-Europe-output.json') as f:
    data_europe = pd.read_json(f, lines=True)

# Filter the data for Europe
europe_data_filtered = data_europe[data_europe['continent'] == 'Europe']

# Save the filtered data to a new JSON file
europe_data_filtered.to_json('json-Europe-Filtered.json', orient='records', lines=True)




# Select specific columns for Europe
europe_selected_columns = europe_filtered_data[['iso_code', 'continent', 'location', 'date', 'total_cases', 'population']]

# Save the DataFrame to a new JSON file
europe_selected_columns.to_json('json-Europe-SelectedColumns.json', orient='records', lines=True)


# Load your Europe data
europe_df = pd.read_json('json-Europe-SelectedColumns.json', lines=True)

# Replace 'date', 'total_cases', and 'location' with your actual column names
# Convert the 'date' column to datetime if it's not already
europe_df['date'] = pd.to_datetime(europe_df['date'])

# Extract year and month from the date
europe_df['year_month'] = europe_df['date'].dt.to_period('M')

# Group by location and year_month, aggregating total cases
grouped_df = europe_df.groupby(['location', 'year_month'], as_index=False)['total_cases'].sum()

# Create a choropleth using Plotly Express
fig = px.choropleth(grouped_df,
                    locations='location',
                    locationmode='country names',
                    color='total_cases',
                    animation_frame='year_month',
                    color_continuous_scale='Viridis',  # You can choose any colorscale
                    title="Total Cases Choropleth Across Locations in Europe",
                    width=1200,   # Adjust the width as needed
                    height=800,   # Adjust the height as needed
                    projection='natural earth',  # You can choose a different map projection
                    )

# Use Europe-specific projection and set the initial center and zoom
fig.update_geos(
    projection_type="natural earth",
    center=dict(lon=10, lat=50),  # Adjust longitude and latitude to center the map on Europe
    scope="europe",  # Set the scope to Europe
)

# Add country names
fig.add_trace(
    go.Scattergeo(
        locationmode='country names',
        lon=grouped_df['location'],
        lat=[0] * len(grouped_df),  # Use 0 as latitude to position the text at the bottom of the map
        mode='text',
        text=grouped_df['location'],
        textposition='bottom center',
        showlegend=False,
        textfont=dict(size=10, color='black'),  # Adjust font size and color
    )
)

# Show the plot
fig.show()





















