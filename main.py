from fastapi import FastAPI, File
from fastapi.responses import HTMLResponse, FileResponse
from visualization import create_stacked_bar_chart  # Import the function from visualization.py

app = FastAPI()

# Function to generate the stacked bar chart HTML
def generate_chart_html():
    # Replace 'data_file_path' with the actual path to your data file
    data_file_path = 'data.json'
    chart = create_stacked_bar_chart(data_file_path)
    chart_html = chart.to_html(full_html=False, include_plotlyjs='cdn')
    return chart_html

# Endpoint to serve index.html with the embedded visualization
@app.get("/index", response_class=HTMLResponse)
async def index():
    chart_html = generate_chart_html()
    # Read the content of index.html and embed the chart HTML into it
    with open("templates/index.html", "r") as file:
        content = file.read().replace("<!-- INSERT_CHART -->", chart_html)
    return HTMLResponse(content=content)

# Endpoint for /aboutus to serve aboutus.html
@app.get("/aboutus", response_class=HTMLResponse)
async def aboutus():
    with open("templates/aboutus.html", "r") as file:
        content = file.read()
    return HTMLResponse(content=content)

# Endpoint for /aboutapp to serve aboutapp.html
@app.get("/aboutapp", response_class=HTMLResponse)
async def aboutapp():
    with open("templates/aboutapp.html", "r") as file:
        content = file.read()
    return HTMLResponse(content=content)

# Endpoint to serve static files like CSS
@app.get("/static/{file_path:path}")
async def serve_static(file_path: str):
    return FileResponse(f"static/{file_path}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
