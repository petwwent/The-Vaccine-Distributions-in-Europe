from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, FileResponse
from visualization import create_stacked_bar_chart  # Import the function
import os
import uvicorn

app = FastAPI()

# Get the path to the current file directory
dir_path = os.path.dirname(os.path.realpath(__file__))

@app.get("/", response_class=FileResponse)
async def index():
    return FileResponse(os.path.join(dir_path, "templates/index.html"))

@app.get("/get-stacked-bar-chart")
async def get_stacked_bar_chart(year: int = Query(None), month: int = Query(None)):
    # Construct the file path or use your specific data loading process
    data_file_path = 'data.json'  # Replace with your actual file path
    
    chart_data = create_stacked_bar_chart(data_file_path, selected_year=year, selected_month=month)
    
    # Convert Plotly figure to HTML content
    chart_html = chart_data.to_html(full_html=False, include_plotlyjs='cdn')
    
    # Save HTML content to a file
    html_file_path = 'chart.html'
    with open(html_file_path, 'w') as file:
        file.write(chart_html)
    
    # Return the file as a FileResponse
    return FileResponse(path=html_file_path, media_type='text/html', filename='stacked_bar_chart.html')

@app.get("/aboutus", response_class=FileResponse)
async def aboutus():
    return FileResponse(os.path.join(dir_path, "templates/aboutus.html"))

@app.get("/aboutapp", response_class=FileResponse)
async def aboutapp():
    return FileResponse(os.path.join(dir_path, "templates/aboutapp.html"))

@app.get("/static/{file_path:path}")
async def serve_static(file_path: str):
    static_file_path = os.path.join(dir_path, "static", file_path)
    if os.path.exists(static_file_path):
        return FileResponse(static_file_path)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
