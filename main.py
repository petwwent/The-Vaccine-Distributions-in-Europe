from flask import Flask, send_file

app = Flask(__name__)

# Route for serving index.html
@app.route('/')
def index():
    return send_file('static/index.html')

# Route for serving script.js
@app.route('/script.js')
def get_script():
    return send_file('static/script.js')

# Route for serving styles.css
@app.route('/styles.css')
def get_styles():
    return send_file('static/styles.css')

# Route for serving data.json
@app.route('/data.json')
def get_data():
    return send_file('static/data.json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
