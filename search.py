import pandas as pd
import plotly.express as px

def compare_stacked_bar_chart(data_path, selected_location1=None, selected_location2=None, date=None):
    # Load your JSON data into a DataFrame
    df = pd.read_json(data_path)

    # Your logic for processing data and creating the stacked bar chart for comparison...
    # Here's an example implementation (customize as needed):

    # Filtering data based on selected locations and date
    filtered_data = df[(df['location'] == selected_location1) | (df['location'] == selected_location2)]
    if date:
        filtered_data = filtered_data[df['date'] == date]

    # Group by location and date, calculating the sum of selected columns
    grouped_data = filtered_data.groupby(['location', 'date']).agg({
        'total_vaccinations': 'sum',
        'population': 'first',
        'total_cases': 'first',
        'people_vaccinated': 'first',
        'people_fully_vaccinated': 'first',
        'total_vaccinations_per_hundred': 'first',
        'people_vaccinated_per_hundred': 'first',
        'people_fully_vaccinated_per_hundred': 'first'
        # Add more columns as needed
    }).reset_index()

    # Create a stacked bar chart for comparing total vaccinations by location and date
    fig = px.bar(
        grouped_data,
        x='date',
        y='total_vaccinations',
        color='location',
        labels={'date': 'Date', 'total_vaccinations': 'Total Vaccinations'},
        title=f'Total Vaccinations Comparison between {selected_location1} and {selected_location2}',
        barmode='group',
        height=600,
        width=1000
    )

    return fig
