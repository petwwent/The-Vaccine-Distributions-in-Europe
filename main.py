from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def default_chart():
    # Logic to render default chart data
    return render_template('index.html')

@app.route('/comparison')
def comparison_chart():
    # Logic to handle comparison based on selected locations
    return render_template('comparison.html')

if __name__ == '__main__':
    app.run(debug=True)
