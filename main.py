from fastapi import FastAPI, File, Query
from fastapi.responses import HTMLResponse, FileResponse
from visualization import create_stacked_bar_chart
import os
import uvicorn

app = FastAPI()

# Get the path to the current file directory
dir_path = os.path.dirname(os.path.realpath(__file__))
data_file_path = 'data.json' 

# Function to generate the stacked bar chart HTML
def generate_chart_html(location1: str, location2: str, date: str):
    chart = create_stacked_bar_chart(data_file_path, location1, location2, date)
    chart_html = chart.to_html(full_html=False, include_plotlyjs='cdn')
    return chart_html

# Endpoint to serve the stacked bar chart with location and date query parameters
@app.get("/get-stacked-bar-chart", response_class=HTMLResponse)
async def get_stacked_bar_chart(location1: str = Query(...), location2: str = Query(...), date: str = Query(...)):
    chart_html = generate_chart_html(location1, location2, date)
    return HTMLResponse(content=chart_html)

# Endpoint for the main index page
@app.get("/", response_class=HTMLResponse)
async def index():
    with open("templates/index.html", "r") as file:
        content = file.read()
    return HTMLResponse(content=content)
# Endpoint for the aboutus page
@app.get("/aboutus", response_class=HTMLResponse)
async def aboutus():
    with open("templates/aboutus.html", "r") as file:
        content = file.read()
    return HTMLResponse(content=content)

# Endpoint for the aboutapp page
@app.get("/aboutapp", response_class=HTMLResponse)
async def aboutapp():
    with open("templates/aboutapp.html", "r") as file:
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
