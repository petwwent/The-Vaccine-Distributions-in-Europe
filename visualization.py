import pandas as pd
import json
import plotly.express as px

def create_stacked_bar_chart(data_path):
    # Load your JSON data into a DataFrame
    df = pd.read_json(data_path)

    # Convert the 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Extract year from the date
    df['year'] = df['date'].dt.year

    # Filter data for the years 2021 to 2023 (inclusive)
    filtered_data = df[df['year'].between(2021, 2023)]

    # Group by location for the specified year range, calculating the sum of total vaccinations and using population for colors
    grouped_data = filtered_data.groupby(['location'], as_index=False).agg({
        'total_vaccinations': 'sum',
        'population': 'first',
        'total_cases': 'first',
        'people_vaccinated': 'first',
        'people_fully_vaccinated': 'first',
        'total_vaccinations_per_hundred': 'first',
        'people_vaccinated_per_hundred': 'first',
        'people_fully_vaccinated_per_hundred': 'first'
        # Add more columns as needed
    })

    # Sort the data by total vaccinations in ascending order
    grouped_data = grouped_data.sort_values('total_vaccinations', ascending=True)

    # Create a stacked bar chart for total vaccinations from 2021 to 2023
    fig_all_years = px.bar(
        grouped_data,
        x='total_vaccinations',
        y='location',
        orientation='h',
        color='population',  # Color based on population
        labels={'total_vaccinations': 'Total Vaccinations', 'location': 'Location'},
        title='Total Vaccinations from 2021 to 2023 (Ascending Order)',
        width=1000,
        height=800,
        text='total_vaccinations',  # Display total vaccinations at the tip of bars
        hover_data=['population', 'total_cases', 'people_vaccinated', 'people_fully_vaccinated',
                    'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred',
                    'people_fully_vaccinated_per_hundred']
        # Add more columns as needed
    )

    fig_all_years.update_traces(texttemplate='%{text:.2s}', textposition='outside')  # Adjust text display

    fig_all_years.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        xaxis_title='Total Vaccinations',
        yaxis_title='Location'
    )

    # Convert the Plotly figure to JSON and return it
    chart_data = fig_all_years.to_json()
    return chart_data

# Example: Call the function with the data file path
data_file_path = 'data.json'  # Replace with your actual file path
create_stacked_bar_chart(data_file_path)
