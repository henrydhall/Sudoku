import pytest
import sudoku_solver
from pathlib import Path

def test_SudokuSolver():
    puzzle_string = '******************************************************************************************'
    test_puzzle = sudoku_solver.SudokuSolver( puzzle_string )
    test_array = [' ' for i in range(0,81)]
    assert test_puzzle.puzzle_array == test_array

def test_str():
    puzzle_string = '******************************************************************************************'
    test_puzzle = sudoku_solver.SudokuSolver( puzzle_string )
    test_string = ' --- --- --- \n| '

if __name__ == '__main__':
    test_SudokuSolver()