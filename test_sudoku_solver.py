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

def test_str_3():
    puzzle_string = '1****************************\n*************************************************************'
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

def test_print_possibilities():
    test_puzzle_string_1 = '12*******3********45*********6************************************************************'
    test_puzzle_1 = sudoku_solver.SudokuSolver(test_puzzle_string_1)
    test_puzzle_1.print_possibilities()
    # TODO: figure out how to test the print. I say don't do it...

def test_check_valid_puzzle():
    test_puzzle_strings = [ '123456789..................1',
                            '123456789...................2',
                            '123456789....................3',
                            '123456789.....................4',
                            '123456789......................5',
                            '123456789.......................6',
                            '123456789........................7',
                            '123456789.........................8',
                            '123456789..........................9',
                            '123456789..1...............',
                            '123456789..2................',
                            '123456789.3..................',
                            '123456789....4................',
                            '123456789.....5................',
                            '123456789....6..................',
                            '123456789........7...............',
                            '123456789.......8.................',
                            '123456789......9...................',
                            '1..1',
                            '2..2',
                            '3..3',
                            '4..4',
                            '5..5',
                            '6..6',
                            '7..7',
                            '8..8',
                            '9..9',
                            ]
    errors = []
    for puzzle in test_puzzle_strings:
        try:
            new_puzzle = sudoku_solver.SudokuSolver(puzzle)
            errors.append(puzzle)
        except ValueError:
            errors.append('Error')
    for thing in errors:
        assert thing == 'Error'

def test_get_reduced_puzzle():
    test_string = '12345678.'
    test_puzzle = sudoku_solver.SudokuSolver(test_string)
    assert test_puzzle.get_reduced_puzzle() == '123456789........................................................................'

    test_string = '.2345678.9'
    test_puzzle = sudoku_solver.SudokuSolver(test_string)
    assert test_puzzle.get_reduced_puzzle() == '1234567899.......................................................................'
    #TODO: expand testing for this.

def test_check_valid_solution():
    test_string = '.234567891'
    test_puzzle = sudoku_solver.SudokuSolver(test_string)
    assert test_puzzle.check_valid_solution() is False

    test_string = '.23456789'
    test_puzzle = sudoku_solver.SudokuSolver(test_string)
    assert test_puzzle.check_valid_solution() is True

if __name__ == '__main__':
    test_SudokuSolver()
    test_str_1()
    test_str_2()
    test_str_3()
    test_build_possibilities()
    test_find_unique_possibilities()
    #test_print_possibilities()
    test_check_valid_puzzle()
    test_get_reduced_puzzle()
    #test_check_valid_solution()