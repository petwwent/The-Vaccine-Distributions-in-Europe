from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from visualization import construct_choropleth  # Import the function
import os
from datetime import datetime
from typing import Optional
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
async def get_search_data(location: Optional[str] = Query(None), date: Optional[str] = Query(None)):
    if location is None or date is None:
        return {"error": "Please provide both location and date parameters."}

    try:
        date_obj = datetime.strptime(date, "%Y-%m")
        year_month = date_obj.strftime("%Y-%m")

        if os.path.exists(data_file_path):
            with open(data_file_path, "r") as file:
                data = json.load(file)
                search_result = [
                    item for item in data 
                    if item.get("location") == location and item.get("date", "").startswith(year_month)
                ]

            if not search_result:
                return {"message": f"No data found for {location} in {year_month}."}

            return search_result
        else:
            return {"error": "Data file not found."}

    except (json.JSONDecodeError, ValueError):
        return {"error": "Error decoding JSON or parsing date."}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=5000)
