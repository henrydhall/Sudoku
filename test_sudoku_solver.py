import pytest
import sudoku_solver
from pathlib import Path

def test_SudokuSolver():
    puzzle_string = '******************************************************************************************'
    test_puzzle = sudoku_solver.SudokuSolver( puzzle_string )
    test_array = [' ' for i in range(0,81)]
    assert test_puzzle.puzzle_array == test_array

def test_str_1():
    puzzle_string = '******************************************************************************************'
    test_puzzle = sudoku_solver.SudokuSolver( puzzle_string )
    #print(test_puzzle)
    test_string = \
f''' --- --- ---
|   |   |   |
|   |   |   |
|   |   |   |
 --- --- ---
|   |   |   |
|   |   |   |
|   |   |   |
 --- --- ---
|   |   |   |
|   |   |   |
|   |   |   |
 --- --- ---'''
    print(test_string)
    assert str(test_puzzle) == test_string

def test_str_2():
    puzzle_string = '1*****************************************************************************************'
    test_puzzle = sudoku_solver.SudokuSolver( puzzle_string )
    #print(test_puzzle)
    test_string = \
f''' --- --- ---
|1  |   |   |
|   |   |   |
|   |   |   |
 --- --- ---
|   |   |   |
|   |   |   |
|   |   |   |
 --- --- ---
|   |   |   |
|   |   |   |
|   |   |   |
 --- --- ---'''
    print(test_string)
    assert str(test_puzzle) == test_string

#TODO: mess around with formats, newlines, etc.

if __name__ == '__main__':
    test_SudokuSolver()
    test_str_1()
    test_str_2()