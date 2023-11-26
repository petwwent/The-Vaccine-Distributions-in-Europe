from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from visualization import construct_choropleth  # Import the function
import os
import json
import uvicorn

app = FastAPI()

# Get the path to the current file directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# Define the path to your data file
data_file_path = os.path.join(dir_path, "data.json")

@app.get("/", response_class=FileResponse)
async def index():
    return FileResponse(os.path.join(dir_path, "templates/index.html"))

@app.get("/get-choropleth-data")
async def get_choropleth_data():
    choropleth_data = construct_choropleth()
    return choropleth_data

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

@app.get("/get-search-data")
async def get_search_data(location: str = Query(None), date: str = Query(None)):
    if location is None or date is None:
        return {"error": "Please provide both location and date parameters."}

    # Read data from data.json based on provided location and date
    try:
        with open(data_file_path, "r") as file:
            data = file.read()
            data_json = json.loads(data)
            search_result = [item for item in data_json if item["location"] == location and item["date"] == date]

        if not search_result:
            return {"message": "No data found for the provided location and date."}

        return search_result

    except FileNotFoundError:
        return {"error": "Data file not found."}
    except json.JSONDecodeError:
        return {"error": "Error decoding JSON."}

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=5000)
