from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from visualization import create_stacked_bar_chart
import os
import uvicorn

app = FastAPI()

# Get the path to the current file directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# Function to generate the stacked bar chart HTML
def generate_chart_html():
    # Replace this function with your actual logic to generate the chart HTML
    data_file_path = 'data.json'
    chart = create_stacked_bar_chart(data_file_path)
    chart_html = chart.to_html(full_html=False, include_plotlyjs='cdn')
    return chart_html

# Endpoint to serve the stacked bar chart
@app.get("/get-stacked-bar-chart", response_class=HTMLResponse)
async def get_stacked_bar_chart():
    chart_html = generate_chart_html()
    return HTMLResponse(content=chart_html)

# Endpoint for the main index page
@app.get("/", response_class=HTMLResponse)
async def index():
    chart = create_stacked_bar_chart(data_file_path)  # Call the function to generate the chart
    
    # Convert the figure to HTML and return it as the response
    chart_html = chart.to_html(full_html=False, include_plotlyjs='cdn')
    return HTMLResponse(content=chart_html)

# Endpoint for aboutus
@app.get("/aboutus", response_class=HTMLResponse)
async def read_aboutus():
    with open(os.path.join(dir_path, "templates/aboutus.html"), "r") as file:
        content = file.read()
    return HTMLResponse(content=content)

# Endpoint for aboutapp
@app.get("/aboutapp", response_class=HTMLResponse)
async def read_aboutapp():
    with open(os.path.join(dir_path, "templates/aboutapp.html"), "r") as file:
        content = file.read()
    return HTMLResponse(content=content)

# Endpoint to serve static files like CSS
@app.get("/static/{file_path:path}")
async def serve_static(file_path: str):
    static_file_path = os.path.join(dir_path, "static", file_path)
    if os.path.exists(static_file_path):
        return FileResponse(static_file_path)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
