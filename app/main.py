from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load data from data.json
with open('../data/json-Europe-SelectedColumns.json', 'r') as file:
    data = json.load(file)

# Define API endpoints
@app.route('/api/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

