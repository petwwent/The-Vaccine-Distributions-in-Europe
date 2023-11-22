from flask import Flask, render_template
import os
from visualization import construct_choropleth  # Import the function

app = Flask(__name__)

# Get the absolute path to the templates directory
template_dir = os.path.abspath('templates')

# Set the template folder for Flask explicitly
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-choropleth-data')
def get_choropleth_data():
    choropleth_data = construct_choropleth()
    return jsonify(choropleth_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
