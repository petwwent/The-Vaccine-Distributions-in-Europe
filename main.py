from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/script.js')
def script():
    return send_file('script.js')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
