from flask import Flask, Response
from plotly.offline import plot

# Import the function to generate the choropleth map from data.py
from data import construct_choropleth

app = Flask(__name__)

# Endpoint to get the base64-encoded choropleth map
@app.route("/get_choropleth")
def get_choropleth():
    # Generate the choropleth map
    encoded_choropleth = construct_choropleth()

    # Display the base64-encoded choropleth map in HTML using Plotly's offline plot
    plot_div = plot({'data': []}, output_type='div', include_plotlyjs=False)
    html_content = f"<img src='data:image/png;base64,{encoded_choropleth}'/> {plot_div}"

    return Response(html_content, mimetype='text/html')
