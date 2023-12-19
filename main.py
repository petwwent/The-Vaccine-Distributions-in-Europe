from flask import Flask, jsonify
import json

app = Flask(__name__)

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

# Your other routes and logic go here...

if __name__ == '__main__':
    app.run()
