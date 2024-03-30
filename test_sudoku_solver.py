import pytest
import sudoku_solver
from pathlib import Path


def test_SudokuSolver_1():
    puzzle_string = '******************************************************************************************'
    test_puzzle = sudoku_solver.SudokuSolver( puzzle_string = puzzle_string)
    test_array = [' ' for i in range(0, 81)]
    assert test_puzzle.puzzle_array == test_array

def test_SudokuSolver_2():
    puzzle_string = f'''123456789\n\r
*********'''
    test_puzzle = sudoku_solver.SudokuSolver( puzzle_string = puzzle_string)
    test_array = [' ' for i in range(0,81)]
    test_array[0] = '1'
    test_array[1] = '2'
    test_array[2] = '3'
    test_array[3] = '4'
    test_array[4] = '5'
    test_array[5] = '6'
    test_array[6] = '7'
    test_array[7] = '8'
    test_array[8] = '9'
    assert test_puzzle.puzzle_array == test_array

def test_str_1():
    puzzle_string = '******************************************************************************************'
    test_puzzle = sudoku_solver.SudokuSolver( puzzle_string = puzzle_string)
    test_string = f''' --- --- ---
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
    test_puzzle = sudoku_solver.SudokuSolver( puzzle_string = puzzle_string)
    test_string = f''' --- --- ---
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
    test_puzzle = sudoku_solver.SudokuSolver(puzzle_string = puzzle_string)
    test_string = f''' --- --- ---
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


# TODO: mess around with formats, newlines, etc.


def test_build_possibilities():
    test_puzzle_string = '12345678***********************************************************************9*'
    test_puzzle = sudoku_solver.SudokuSolver(puzzle_string = test_puzzle_string)
    assert test_puzzle.possibilities[8] == ['9']
    assert test_puzzle.possibilities[9] == ['4', '5', '6', '7', '8', '9']
    assert test_puzzle.possibilities[17] == ['1', '2', '3', '4', '5', '6']
    # TODO: test building possibilities
    # might want to break things down some more...
    # then test building numbers to be eliminated, etc.


def test_find_unique_possibilities():
    test_puzzle_string_1 = '12*******3********45*********6************************************************************'
    test_puzzle_1 = sudoku_solver.SudokuSolver(puzzle_string = test_puzzle_string_1)
    assert test_puzzle_1.possibilities[10] == ['6']
    test_puzzle_string_2 = '*12*********6*************6******************************************************'
    test_puzzle_2 = sudoku_solver.SudokuSolver(puzzle_string = test_puzzle_string_2)
    assert test_puzzle_2.possibilities[0] == ['6']
    test_puzzle_string_3 = '12**********6*************6******************************************************'
    test_puzzle_3 = sudoku_solver.SudokuSolver(puzzle_string = test_puzzle_string_3)
    assert test_puzzle_3.possibilities[2] == ['6']


def test_print_possibilities():
    test_puzzle_string_1 = '12*******3********45*********6************************************************************'
    test_puzzle_1 = sudoku_solver.SudokuSolver(puzzle_string = test_puzzle_string_1)
    test_puzzle_1.print_possibilities()
    # TODO: figure out how to test the print. I say don't do it...


def test_check_valid_puzzle():
    test_puzzle_strings = [
        '123456789..................1',
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
            new_puzzle = sudoku_solver.SudokuSolver(puzzle_string = puzzle)
            errors.append(puzzle)
        except ValueError:
            errors.append('Error')
    for thing in errors:
        assert thing == 'Error'


def test_get_reduced_puzzle():
    test_string = '12345678.'
    test_puzzle = sudoku_solver.SudokuSolver(puzzle_string = test_string)
    assert (
        test_puzzle.get_reduced_puzzle()
        == '123456789........................................................................'
    )

    test_string = '.2345678.9'
    test_puzzle = sudoku_solver.SudokuSolver(puzzle_string = test_string)
    assert (
        test_puzzle.get_reduced_puzzle()
        == '1234567899.......................................................................'
    )
    # TODO: expand testing for this.


def test_check_valid_solution():
    test_string = '.234567891'
    test_puzzle = sudoku_solver.SudokuSolver(puzzle_string = test_string)
    assert test_puzzle.check_valid_solution() is False

    test_string = '.23456789'
    test_puzzle = sudoku_solver.SudokuSolver(puzzle_string = test_string)
    assert test_puzzle.check_valid_solution() is True

def test_get_cell_column_number():
    test_puzzle = sudoku_solver.SudokuSolver(puzzle = '123')
    assert test_puzzle.get_cell_column_number(0)  == 0
    assert test_puzzle.get_cell_column_number(14) == 5
    assert test_puzzle.get_cell_column_number(27) == 0
    assert test_puzzle.get_cell_column_number(28) == 1
    assert test_puzzle.get_cell_column_number(31) == 4
    assert test_puzzle.get_cell_column_number(40) == 4
    assert test_puzzle.get_cell_column_number(50) == 5
    assert test_puzzle.get_cell_column_number(60) == 6
    assert test_puzzle.get_cell_column_number(70) == 7
    assert test_puzzle.get_cell_column_number(80) == 8
    assert test_puzzle.get_cell_column_number(62) == 8

def test_get_cell_row_number():
    test_puzzle = sudoku_solver.SudokuSolver(puzzle = '123')
    assert test_puzzle.get_cell_row_number(0)  == 0
    assert test_puzzle.get_cell_row_number(11)  == 1
    assert test_puzzle.get_cell_row_number(12)  == 1
    assert test_puzzle.get_cell_row_number(23)  == 2
    assert test_puzzle.get_cell_row_number(33)  == 3
    assert test_puzzle.get_cell_row_number(44)  == 4
    assert test_puzzle.get_cell_row_number(54)  == 6
    assert test_puzzle.get_cell_row_number(65)  == 7
    assert test_puzzle.get_cell_row_number(75)  == 8
    assert test_puzzle.get_cell_row_number(80)  == 8
    assert test_puzzle.get_cell_row_number(66)  == 7

def test_copy_solver():
    test_puzzle = sudoku_solver.SudokuSolver( puzzle_string =  '12345')
    copy_puzzle = test_puzzle.copy_solver()
    assert test_puzzle.puzzle_string == copy_puzzle.puzzle_string
    assert test_puzzle.puzzle_array == copy_puzzle.puzzle_array
    assert test_puzzle.possibilities == copy_puzzle.possibilities
    assert test_puzzle.get_reduced_puzzle() == copy_puzzle.get_reduced_puzzle()

def test_BacktrackSolver():
    # Test from solver
    my_solver = sudoku_solver.SudokuSolver(puzzle_string = '123')
    test_solver = sudoku_solver.BacktrackSolver(solver = my_solver)
    assert test_solver.puzzle == my_solver.puzzle_string
    assert test_solver.possibilities == my_solver.possibilities

    # Test from puzzle string
    test_solver = sudoku_solver.BacktrackSolver(puzzle = '124')
    assert test_solver.puzzle_string == '124'
    my_solver = sudoku_solver.SudokuSolver(puzzle_string='124')
    assert test_solver.possibilities == my_solver.possibilities

    # Test type error
    with pytest.raises(TypeError):
        test_solver = sudoku_solver.BacktrackSolver( solver = '123456' )

    # Test KeyError
    with pytest.raises(KeyError):
        test_solver = sudoku_solver.BacktrackSolver(this_is_wrong = 'hi')

def test_solve_by_backtrack():
    test_solver = sudoku_solver.BacktrackSolver(puzzle = '123')
    test_solver.solve_by_backtrack()
    assert test_solver.solver.get_reduced_puzzle() == '123456789456789123789123456214365897365897214897214365531642978642978531978531642'

    test_solver = sudoku_solver.BacktrackSolver(puzzle = '.8.5.1...2.....83........4.8...9..57..5........6..32.........28..91.57.....96....')
    test_solver.solve_by_backtrack()
    assert test_solver.solver.get_reduced_puzzle() == '984531672257649831613827549832496157745218396196753284561374928429185763378962415'

if __name__ == '__main__':
    test_SudokuSolver_1()
    test_SudokuSolver_2()
    test_str_1()
    test_str_2()
    test_str_3()
    test_build_possibilities()
    test_find_unique_possibilities()
    # test_print_possibilities()
    test_check_valid_puzzle()
    test_get_reduced_puzzle()
    test_check_valid_solution()
    test_get_cell_column_number()
    test_copy_solver()
    test_BacktrackSolver()