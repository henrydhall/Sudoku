# Sudoku
Experimenting with solving and generating Sudoku puzzles with Python.

## Setup and Running
### Windows Powershell
Virtual Environment

    python -m venv sudoku_env
    .\sudoku_env\Scripts\Activate.ps1
    pip install -r requirements.txt

Run app

    $env:FLASK_APP="sudoku.py"   
    flask run --debug

### Linux Bash
Virtual Environment

    python3 -m venv sudoku_env
    source sudoku_env/bin/activate
    pip3 install -r requirements.txt

Run app

    export FLASK_APP=sudoku
    flask run --debug

## Testing Coverage
Run the following command
    
    pytest --cov-report html --cov

## TODO
* 404 page
* Add error message for bad puzzles.
* Make form prettier.
* Add database
* Test possibility strings for web
* Restructuring