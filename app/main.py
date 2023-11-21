from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Load the data for visualization
    with open('data/json-Europe-SelectedColumns.json') as f:
        data = json.load(f)

    return render_template('index.html', data=json.dumps(data))

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Specify the port to run the application
