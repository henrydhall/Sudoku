# Sudoku
Experimenting with solving and generating Sudoku puzzles with Python.

## Setup and Running
I know this will work with Python>=3.8.10. For now I recommend using the latest version.
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

## Apendix
### Pip Error
While testing my startup instructions I encountered the following error when using pip to install any module:

WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ProtocolError('Connection aborted.', FileNotFoundError(2, 'No such file or directory'))': /simple/numpy/  
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ProtocolError('Connection aborted.', FileNotFoundError(2, 'No such file or directory'))': /simple/numpy/  
WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ProtocolError('Connection aborted.', FileNotFoundError(2, 'No such file or directory'))': /simple/numpy/  
WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ProtocolError('Connection aborted.', FileNotFoundError(2, 'No such file or directory'))': /simple/numpy/  
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ProtocolError('Connection aborted.', FileNotFoundError(2, 'No such file or directory'))': /simple/numpy/  
ERROR: Could not find a version that satisfies the requirement numpy (from versions: none)  
ERROR: No matching   distribution found for numpy

Which was very frustrating. There don't seem to be many people who run into this issue, and most of them seem to be solved by adjusting proxy server settings. Mine was an especially stupid reason though. Using 

    pip install numpy --verbose --debug

and with a lot of help from an old Discord help chat by Zaddish and Mark (link below) I found an error where it was searching for a log file that didn't exist: SSLKEYLOGFILE. That was my problem. I had set up my environmental variable to point to a file I had created to work with analyzing TLS packets, and had set that variable up to let me decrypt streams. Once I deleted that environmentmental variable I was fine.

https://discord.com/channels/267624335836053506/1051017993963966534