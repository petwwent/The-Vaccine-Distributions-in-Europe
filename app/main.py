from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Get the absolute path of the 'data' directory
    data_dir = os.path.abspath('data')

    # Join the path to the JSON file
    json_file_path = os.path.join(data_dir, 'json-Europe-SelectedColumns.json')

    # Check if the file exists
    if os.path.exists(json_file_path):
        # Load the data for visualization
        with open(json_file_path) as f:
            data = json.load(f)

        return render_template('index.html', data=json.dumps(data))
    else:
        return 'File not found'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
