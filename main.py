import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from data import construct_choropleth

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Use the processed data returned by construct_choropleth() from data.py
    processed_data = construct_choropleth()
    return templates.TemplateResponse('index.html', {'request': request, 'data': processed_data})

    
    return data
