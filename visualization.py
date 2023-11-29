import pandas as pd
import plotly.express as px

def create_stacked_bar_chart(data_path, selected_year=None, selected_month=None):
    # Load your JSON data into a DataFrame
    df = pd.read_json(data_path)

    # Convert the 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Group by location and date, calculating the sum of total vaccinations and other aggregated columns
    grouped_data = df.groupby(['location', 'date'], as_index=False).agg({
        'total_vaccinations': 'sum',
        'population': 'first',
        'total_cases': 'first',
        'people_vaccinated': 'first',
        'people_fully_vaccinated': 'first',
        'total_vaccinations_per_hundred': 'first',
        'people_vaccinated_per_hundred': 'first',
        'people_fully_vaccinated_per_hundred': 'first',
        # Add more columns as needed
    })

    # Create a stacked bar chart for total vaccinations by location with animation_frame
    fig = px.bar(
        grouped_data,
        x='total_vaccinations',
        y='location',
        orientation='h',
        color='population',  # Color based on population
        labels={'total_vaccinations': 'Total Vaccinations', 'location': 'Location'},
        title='Total Vaccinations by Location',
        width=1000,
        height=800,
        text='total_vaccinations',  # Display total vaccinations at the tip of bars
        hover_data=['population', 'total_cases', 'people_vaccinated', 'people_fully_vaccinated',
                    'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred',
                    'people_fully_vaccinated_per_hundred'],
        animation_frame='date',  # Use date as animation frame
        range_x=[0, grouped_data['total_vaccinations'].max()]  # Set x-axis range
    )

    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')  # Adjust text display

    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        xaxis_title='Total Vaccinations',
        yaxis_title='Location',
        updatemenus=[dict(type='buttons',
                          buttons=[dict(label='Play', method='animate', args=[None, {'frame': {'duration': 200}}]),
                                   dict(label='Pause', method='animate', args=[[None], {'frame': {'duration': 0}, 'mode': 'immediate'}])])],
        sliders=[dict(currentvalue={'prefix': 'Date: '}, steps=[])]  # Empty steps for slider initialization
    )

    frames = [dict(data=[dict(type='bar',
                               x=df[df['date'] == date]['total_vaccinations'],
                               y=df[df['date'] == date]['location'],
                               orientation='h',
                               text=df[df['date'] == date]['total_vaccinations'],
                               hoverinfo='text',
                               marker={'color': df[df['date'] == date]['population']})],
                   name=str(date)) for date in df['date'].sort_values().unique()]

    fig.frames = frames  # Assign frames for animation

    return fig
data_file_path = 'data.json'


