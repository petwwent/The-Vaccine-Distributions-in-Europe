from fastapi import FastAPI
from fastapi.responses import FileResponse
from visualization import construct_choropleth  # Import the function
import os

app = FastAPI()

# Get the path to the current file directory
dir_path = os.path.dirname(os.path.realpath(__file__))

@app.get("/", response_class=FileResponse)
async def index():
    return FileResponse(os.path.join(dir_path, "templates/index.html"))

@app.get("/get-choropleth-data")
async def get_choropleth_data():
    choropleth_data = construct_choropleth()
    return choropleth_data

@app.get("/about-us", response_class=FileResponse)
async def about_us():
    return FileResponse(os.path.join(dir_path, "templates/about us.html"))

@app.get("/about-app", response_class=FileResponse)
async def about_app():
    return FileResponse(os.path.join(dir_path, "templates/about App.html"))

@app.get("/static/{file_path:path}")
async def serve_static(file_path: str):
    static_file_path = os.path.join(dir_path, "static", file_path)
    if os.path.exists(static_file_path):
        return FileResponse(static_file_path)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
