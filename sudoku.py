from flask import Flask, render_template

from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess huh'

bootstrap = Bootstrap(app)

class SudokuForm(FlaskForm):
    sudoku_puzzle = TextAreaField("SudokuPuzzle",validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    name = None
    numbers = [i for i in range(0,81)]
    numbers[1] = ''
    return render_template('index.html', numbers = numbers)

@app.route('/solve_helper',methods = ['GET','POST'])
def solve_helper():
    form = SudokuForm()
    if form.validate_on_submit():
        print(form.sudoku_puzzle.data)
        return render_template('index.html', numbers = form.sudoku_puzzle.data )
    name = None
    numbers = [i for i in range(0,81)]
    return render_template('solve_input.html', numbers = numbers, form = form)