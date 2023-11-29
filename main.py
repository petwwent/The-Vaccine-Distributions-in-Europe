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
async def get_stacked_bar_chart(year: int = Query(2021), month: int = Query(1)):
    # Construct the file path or use your specific data loading process
    data_file_path = 'data.json'  # Replace with your actual file path
    create_stacked_bar_chart(data_file_path, selected_year=year, selected_month=month)
    # Return a success message or desired JSON response
    return JSONResponse(content={"message": "Stacked bar chart created for the selected year and month."})

@app.get("/search", response_class=FileResponse)
async def search():
    return FileResponse(os.path.join(dir_path, "templates/search.html"))

@app.get("/update-stacked-bar-chart")
async def update_stacked_bar_chart(year: int = Query(2021), month: int = Query(1)):
    # Construct the file path or use your specific data loading process
    data_file_path = 'updated_data.json'  # Replace with your updated data file path
    create_stacked_bar_chart(data_file_path, selected_year=year, selected_month=month)
    # Return a success message or desired JSON response
    return JSONResponse(content={"message": "Stacked bar chart updated for the selected year and month."})

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
