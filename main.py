from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from visualization import create_stacked_bar_chart  # Import the function from visualization.py
import os
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")
data_file_path = 'data.json'
dir_path = os.path.dirname(os.path.realpath(__file__))

@app.get("/", response_class=HTMLResponse)
async def index():
    chart = create_stacked_bar_chart(data_file_path)
    chart_html = chart.to_html(full_html=False, include_plotlyjs='cdn')

    # Read the content of index.html
    with open(os.path.join(dir_path, "templates/index.html"), "r") as file:
        html_content = file.read()

    # Inject the chart HTML into the index.html content
    html_content_with_chart = html_content.replace("{{ chart_here }}", chart_html)
    return HTMLResponse(content=html_content_with_chart)

@app.get("/aboutus", response_class=HTMLResponse)
async def aboutus():
    return templates.TemplateResponse("aboutus.html")

@app.get("/aboutapp", response_class=HTMLResponse)
async def aboutapp():
    return templates.TemplateResponse("aboutapp.html")


@app.get("/static/{file_path:path}", response_class=FileResponse)
async def serve_static(file_path: str):
    static_file_path = os.path.join(dir_path, "static", file_path)
    if os.path.exists(static_file_path):
        return FileResponse(static_file_path)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

