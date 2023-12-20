from flask import Flask, send_file

app = Flask(__name__)

# Route for serving the index.html file
@app.route('/')
def index():
    return send_file('index.html')

# Route for serving the data.json file
@app.route('/data.json')
def get_data():
    return send_file('data.json')

# Route for serving the script.js file
@app.route('/script.js')
def get_script():
    return send_file('script.js')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
