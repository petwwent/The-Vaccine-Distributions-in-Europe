from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from visualization import create_stacked_bar_chart
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
data_file_path = 'data.json'
dir_path = os.path.dirname(os.path.realpath(__file__))

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    chart = create_stacked_bar_chart(data_file_path)
    chart_html = chart.to_html(full_html=False, include_plotlyjs='cdn')
    return templates.TemplateResponse("index.html", {"request": request, "chart_html": chart_html})

@app.get("/aboutus", response_class=HTMLResponse)
async def aboutus(request: Request):
    return templates.TemplateResponse("aboutus.html", {"request": request})

@app.get("/aboutapp", response_class=HTMLResponse)
async def aboutapp(request: Request):
    return templates.TemplateResponse("aboutapp.html", {"request": request})

@app.get("/static/{file_path:path}", response_class=FileResponse)
async def serve_static(file_path: str):
    static_file_path = os.path.join(dir_path, "static", file_path)
    if os.path.exists(static_file_path):
        return FileResponse(static_file_path)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
