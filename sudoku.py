from flask import Flask, render_template

from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    name = None
    numbers = [i for i in range(0,81)]
    numbers[1] = ''
    return render_template('index.html', numbers = numbers)

@app.route('/solve_helper')
def solve_helper():
    name = None
    numbers = [i for i in range(0,81)]
    return render_template('solve_input.html', numbers = numbers)