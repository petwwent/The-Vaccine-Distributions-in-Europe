from flask import Flask, send_file

app = Flask(__name__)

# Route for serving the index.html file
@app.route('/static/')
def index():
    return send_file('index.html')

# Route for serving the data.json file
@app.route('/static/data.json')
def get_data():
    return send_file('data.json')

# Route for serving the script.js file
@app.route('/static/script.js')
def get_script():
    return send_file('script.js')

# Route for serving the styles.css file
@app.route('/static/styles.css')
def get_styles():
    return send_file('styles.css')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
