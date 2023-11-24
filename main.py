from flask import Flask, render_template
from data import construct_choropleth
import uvicorn

app = Flask(__name__)

@app.route('/')
def index():
    encoded_choropleth = construct_choropleth()
    return render_template('index.html', encoded_choropleth=encoded_choropleth)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
