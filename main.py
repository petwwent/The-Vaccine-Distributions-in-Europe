from fastapi import FastAPI, FileResponse
from visualization import construct_choropleth  # Import the function
import os

app = FastAPI()

# Get the path to the current file directory
dir_path = os.path.dirname(os.path.realpath(__file__))

@app.get("/", response_class=FileResponse)
async def index():
    # Assuming you have an index.html file in the 'templates' directory
    return FileResponse(os.path.join(dir_path, "templates/index.html"))

@app.get("/get-choropleth-data")
async def get_choropleth_data():
    choropleth_data = construct_choropleth()
    return choropleth_data

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
