from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, HTMLResponse
from visualization import create_stacked_bar_chart  # Import the function from visualization.py
import os
import uvicorn

app = FastAPI()

# Get the path to the current file directory
dir_path = os.path.dirname(os.path.realpath(__file__))
data_file_path = 'data.json' 

@app.get("/", response_class=HTMLResponse)
async def index():
    chart = create_stacked_bar_chart(data_file_path)  # Call the function to generate the chart
    
    # Convert the figure to HTML and return it as the response
    chart_html = chart.to_html(full_html=False, include_plotlyjs='cdn')
    return HTMLResponse(content=chart_html)


@app.get("/aboutus", response_class=FileResponse)
async def aboutus():
    return FileResponse(os.path.join(dir_path, "templates/aboutus.html"))

@app.get("/aboutapp", response_class=FileResponse)
async def aboutapp():
    return FileResponse(os.path.join(dir_path, "templates/aboutapp.html"))

@app.get("/static/{file_path:path}", response_class=FileResponse)
async def serve_static(file_path: str):
    static_file_path = os.path.join(dir_path, "static", file_path)
    if os.path.exists(static_file_path):
        return FileResponse(static_file_path)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
