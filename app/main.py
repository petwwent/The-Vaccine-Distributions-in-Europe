from flask import Flask, render_template
import pandas as pd
import json
import os

app = Flask(__name__)

# Get the absolute path to the templates directory
template_dir = os.path.abspath('templates')

# Set the template folder for Flask explicitly
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    # Load the data for visualization
    with open('data/converted_data.json') as f:
        data = json.load(f)

    return render_template('index.html', data=json.dumps(data))

if __name__ == '__main__':
    app.run(debug=True, port=5000)

        
