from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from visualization import create_stacked_bar_chart
import os
import uvicorn

app = FastAPI()

# Get the path to the current file directory
dir_path = os.path.dirname(os.path.realpath(__file__))
data_file_path = 'data.json' 

# Endpoint to serve the stacked bar chart
@app.get("/get-stacked-bar-chart", response_class=HTMLResponse)
async def get_stacked_bar_chart():
    chart = create_stacked_bar_chart(data_file_path)  # Call the function to generate the chart
    
    # Convert the figure to HTML
    chart_html = chart.to_html(full_html=False, include_plotlyjs='cdn')
    
    # Read the content of index.html
    with open("templates/index.html", "r") as file:
        content = file.read().replace("<!-- INSERT_CHART -->", chart_html)
    
    return HTMLResponse(content=content)

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
