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
    assert str(test_puzzle) == test_string

def test_str_2():
    puzzle_string = '1*****************************************************************************************'
    test_puzzle = sudoku_solver.SudokuSolver( puzzle_string )
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
    assert str(test_puzzle) == test_string

#TODO: mess around with formats, newlines, etc.

def test_build_possibilities():
    test_puzzle_string = '12345678***********************************************************************9*'
    test_puzzle = sudoku_solver.SudokuSolver(test_puzzle_string)
    assert test_puzzle.possibilities[8] == ['9']
    assert test_puzzle.possibilities[9] == ['4','5','6','7','8','9']
    assert test_puzzle.possibilities[17] == ['1','2','3','4','5','6']
    #TODO: test building possibilities
    #might want to break things down some more...
    #then test building numbers to be eliminated, etc.

def test_find_unique_possibilities():
    test_puzzle_string_1 = '12*******3********45*********6************************************************************'
    test_puzzle_1 = sudoku_solver.SudokuSolver(test_puzzle_string_1)
    assert test_puzzle_1.possibilities[10] == ['6']
    test_puzzle_string_2 = '*12*********6*************6******************************************************'
    test_puzzle_2 = sudoku_solver.SudokuSolver(test_puzzle_string_2)
    assert test_puzzle_2.possibilities[0] == ['6']
    test_puzzle_string_3 = '12**********6*************6******************************************************'
    test_puzzle_3 = sudoku_solver.SudokuSolver(test_puzzle_string_3)
    assert test_puzzle_3.possibilities[2] == ['6']

if __name__ == '__main__':
    test_SudokuSolver()
    test_str_1()
    test_str_2()
    test_build_possibilities()
    test_find_unique_possibilities()