from flask import Flask, send_from_directory, jsonify, request
import json

app = Flask(__name__)

# Route to serve index.html
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Route to serve comparison.html
@app.route('/comparison')
def comparison():
    return send_from_directory('static', 'comparison.html')

# Route to serve static files like CSS and JavaScript
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# Route to serve COVID-19 data from data.json
@app.route('/covidData')
def covid_data():
    # Read data from data.json
    with open('static/data.json', 'r') as json_file:
        data = json.load(json_file)

    return jsonify(data)

# Route to handle comparison based on locations and date
@app.route('/compareData', methods=['POST'])
def compare_data():
    data = request.json  # Received JSON data from JavaScript

    # Process data for comparison based on selected locations and date (data contains selected locations and date)
    selected_locations = data.get('locations', [])
    selected_date = data.get('date')

    # Read data from data.json
    with open('static/data.json', 'r') as json_file:
        all_data = json.load(json_file)

    # Filter data based on selected locations and date
    compared_data = [entry for entry in all_data if entry['location'] in selected_locations and entry['date'] == selected_date]

    return jsonify(compared_data)

# Your other routes and logic...

if __name__ == '__main__':
    app.run()
