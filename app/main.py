from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Load the data for visualization
    data = pd.read_json('data/json-Europe-SelectedColumns.json', lines=True)

    # Convert DataFrame to JSON string
    json_data = data.to_json(orient='records')

    return render_template('index.html', data=json_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
