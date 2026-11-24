from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Маршруты для квартир
@app.route('/flat1')
def flat1():
    return render_template('flat1.html')

@app.route('/flat2')
def flat2():
    return render_template('flat2.html')

@app.route('/flat3')
def flat3():
    return render_template('flat3.html')

if __name__ == '__main__':
    app.run(debug=True)