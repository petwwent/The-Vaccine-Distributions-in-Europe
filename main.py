from flask import Flask, jsonify
import json
from custom_middleware import CustomMiddleware  # Import the middleware

app = Flask(__name__)

# Custom Middleware to add response headers
@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Adjust as needed for CORS policy
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Sample data serving routes
@app.route('/defaultChartData')
def default_chart_data():
    # Read data from data.json and process it
    with open('visualization_data/data.json', 'r') as json_file:
        data = json.load(json_file)

    # Process data for default chart: Sort by dates in descending order
    default_data = data['comparisonChartData']
    sorted_data = sorted(default_data, key=lambda x: x['label'], reverse=True)

    # Assign colors based on population (example colors)
    color_scale = {
        "Location A": "blue",
        "Location B": "green",
        "Location C": "red"
        # Add more colors for other locations as needed
    }

    # Assign colors to data based on population (replace 'value' with actual population key)
    for item in sorted_data:
        for key in item.keys():
            if key != 'label':
                item[key + '_color'] = color_scale[key]
    
    return jsonify(sorted_data)

if __name__ == '__main__':
    # Create an instance of the CustomMiddleware
    custom_middleware = CustomMiddleware(app)

    # Run the Flask app with the custom middleware
    from uvicorn import run
    run(app=custom_middleware, host='0.0.0.0', port=5000)
