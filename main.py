from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, HTMLResponse
from visualization import create_stacked_bar_chart  # Import the function from visualization.py
import os
import uvicorn

app = FastAPI()
data_file_path = 'data.json'
dir_path = os.path.dirname(os.path.realpath(__file__))

def get_index_with_chart(chart_html: str) -> str:
    # Read the content of index.html
    with open(os.path.join(dir_path, "templates/index.html"), "r") as file:
        html_content = file.read()

    # Inject the chart HTML into the index.html content
    html_content_with_chart = html_content.replace("{{ chart_here }}", chart_html)
    return html_content_with_chart

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    chart = create_stacked_bar_chart(data_file_path)
    chart_html = chart.to_html(full_html=False, include_plotlyjs='cdn')

    return HTMLResponse(content=get_index_with_chart(chart_html), status_code=200)

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

