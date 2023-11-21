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
    # Call the function to generate the choropleth figure
    fig = construct_choropleth()

    # Convert the figure to JSON
    graphJSON = fig.to_json()

    return render_template('index.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
