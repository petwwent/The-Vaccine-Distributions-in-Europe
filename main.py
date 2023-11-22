from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from plotly.offline import plot

# Import the function to generate the choropleth map
from data.py import construct_choropleth

app = FastAPI()

# Endpoint to get the base64-encoded choropleth map
@app.get("/get_choropleth", response_class=HTMLResponse)
async def get_choropleth():
    # Generate the choropleth map
    encoded_choropleth = construct_choropleth()

    # Display the base64-encoded choropleth map in HTML using Plotly's offline plot
    plot_div = plot({'data': []}, output_type='div', include_plotlyjs=False)
    html_content = f"<img src='data:image/png;base64,{encoded_choropleth}'/> {plot_div}"

    return HTMLResponse(content=html_content)
