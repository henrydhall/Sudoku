from flask import Flask, render_template

from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello there!!</h1>'

@app.route('/sudoku')
def sudoku():
    name = None
    return render_template('index.html')