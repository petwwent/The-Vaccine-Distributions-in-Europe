import dash
from dash import html, dcc
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the search page
app.layout = html.Div([
    html.H1("Search Dashboard"),
    
    # Input fields for year and month
    dcc.Input(id='year-input', type='number', placeholder='Enter Year'),
    dcc.Input(id='month-input', type='text', placeholder='Enter Month'),

    # Link to the visualization (index.html)
    html.A('Go to Visualization', href='/visualization')
])

# Callback to store input values in the URL
@app.callback(
    Output('url', 'pathname'),
    [Input('year-input', 'value'),
     Input('month-input', 'value')]
)
def update_url(year, month):
    if year and month:
        return f'/visualization?year={year}&month={month}'
    else:
        return '/'

if __name__ == '__main__':
    app.run_server(debug=True)
