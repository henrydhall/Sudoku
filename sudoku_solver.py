"""
This module has some classes and functionality for solving sudokus.

sudoku_solver.SudokuSolver
    This class is the simplest object to help solve sudoku puzzles.

sudoku_solver.BacktrackSolver
    This class uses backtracking to eliminate possibilities and solve sudoku puzzles.
"""

import string
import copy

BLANK_PUZZLE = ['\n\n\n' for i in range(0,81)]

class SudokuSolver:
    """
    SudokuSolver object.

    Provides solving, reading, and basic notes for solving a sudoku puzzle.

    Basic Usage::
    >>> import sudoku_solver
    >>> p = sudoku_solver.SudokuSolver('123...456...')
    >>> p.get_reduced_puzzle()
    '123...456........................................................................'
    """

    def __init__(self, **kwargs):
        """
        Creates SudokuSolver class.

        param **kwargs: 
            puzzle_string: puzzle encoding for new puzzle (optional).

        returns SudokuSolver object.
        """
        if 'puzzle_string' in kwargs: 
            puzzle_string = kwargs['puzzle_string']
            puzzle_array = []
            processor = 0
            while processor < len(puzzle_string) and len(puzzle_array) < 81:
                if puzzle_string[processor].isnumeric():
                    puzzle_array.append(puzzle_string[processor])
                elif puzzle_string[processor] == '\n' or puzzle_string[processor] == '\r':
                    # This was tricky. HTML form newlines aren't \n, they are \r
                    pass
                else:
                    puzzle_array.append(' ')
                processor = processor + 1
            while len(puzzle_array) < 81:
                puzzle_array.append(' ')
            self.puzzle_array = puzzle_array
            self.puzzle_string = puzzle_string
            self.check_valid_puzzle()
            self.build_possibilities()
        else:
            pass
        # if self.check_valid_solution() is False:
        #    pass #TODO: come up with error handling...see if we can make this not so slow

    def copy_solver(self) -> 'SudokuSolver':
        """
        Creates a copy of a SudokuSolver object by copying all of its attributes.

        Returns: SudokuSolver object.
        """
        copy_solver = SudokuSolver()
        copy_solver.puzzle_string = copy.deepcopy( self.puzzle_string )
        copy_solver.puzzle_array  = copy.deepcopy( self.puzzle_array )
        copy_solver.possibilities = copy.deepcopy( self.get_possibilities() )
        return copy_solver

    def check_valid_puzzle(self) -> None:
        """
        Checks that the puzzle created is valid. Raises ValueError if invalid.
        """
        for i in range(0, 9):
            if not self.check_valid_box(i):
                raise ValueError("Invalid puzzle. Bad box.")
            if not self.check_valid_row(i):
                raise ValueError("Invalid puzzle. Bad row.")
            if not self.check_valid_column(i):
                raise ValueError("Invalid puzzle. Bad column.")

    def check_valid_solution(self) -> bool:
        """
        Checks that a solution generated by the class is valid.

        Returns: bool. True if the solution is valid. False if invalid.
        """
        try:
            # Uses the reduced puzzle to create a new puzzle. Returns false if an error is raised.
            temp_puzzle = SudokuSolver( puzzle_string = self.get_reduced_puzzle())
            return True
        except:
            return False

    def check_valid_box(self, box_number) -> bool:
        """
        Check that a box of cells is valid under sudoku rules.

        param box_number: int. The number of the box to be checked.

        Returns: bool. True if valid. False in invalid.
        """
        # Get the index of the first cell.
        box_start = self.get_box_start_index(box_number)
        # Create an empty list. We'll insert each cell's contents.
        box = []
        box.append(self.puzzle_array[box_start])
        box.append(self.puzzle_array[box_start + 1])
        box.append(self.puzzle_array[box_start + 2])
        box.append(self.puzzle_array[box_start + 9])
        box.append(self.puzzle_array[box_start + 10])
        box.append(self.puzzle_array[box_start + 11])
        box.append(self.puzzle_array[box_start + 18])
        box.append(self.puzzle_array[box_start + 19])
        box.append(self.puzzle_array[box_start + 20])

        # Check to see if any numbers are duplicated. If it is, return False.
        for i in range(1, 10):
            if box.count(str(i)) > 1:
                return False

        return True

    def check_valid_row(self, row_number) -> bool:
        """
        Check to see if a row is valid under sudoku rules.

        param row_number: number of row to check.

        Returns: bool. True if valid, False if invalid.
        """
        # Get a list with all the numbers in the row.
        row = self.puzzle_array[row_number * 9 : row_number * 9 + 9 :]
        # If a number is duplicated return false.
        for i in range(1, 10):
            if row.count(str(i)) > 1:
                return False
        return True

    def check_valid_column(self, column_number) -> bool:
        """
        Check if a column in the puzzle is valid.

        param column_number: int. Number of column to check.

        Returns: bool. True if valid. False if invalid.
        """
        # Make a list containing the selected column.
        column = self.puzzle_array[column_number::9]
        # If a number is duplicated return false.
        for i in range(1, 10):
            if column.count(str(i)) > 1:
                return False
        return True

    def get_cell_column_number(self, cell_number):
        """
        Returns a cell's column number calculated from the cell number.

        Returns: int. Column number of the cell.
        """
        return cell_number % 9

    def get_cell_row_number(self, cell_number) -> int:
        """
        Returns the row number of a cell calculated from its cell number.

        Returns: int. A row number 0-8.
        """
        return cell_number // 9

    def get_cell_box_number(self, cell_number):
        raise NotImplementedError('TODO: get_cell_box_number')

    def __str__(self) -> str:
        """
        Gets a printable version of the puzzle.

        Returns: str. printable string in puzzle format.
        """
        sudoku_string = ' --- --- ---\n'

        for i in range(len(self.puzzle_array)):
            if i % 27 == 0 and i != 0:
                sudoku_string = sudoku_string + '|\n --- --- ---\n'
            elif i % 9 == 0 and i != 0:
                sudoku_string = sudoku_string + '|\n'
            if i % 3 == 0:
                sudoku_string = sudoku_string + '|'

            sudoku_string = sudoku_string + self.puzzle_array[i]

        sudoku_string = sudoku_string + '|\n --- --- ---'

        return sudoku_string

    def print_possibilities(self) -> None:
        """
        Prints solved cells and nothing else.

        TODO: figure out what to do with this function.
        """
        for i in range(81):
            if i % 9 == 0 and i != 0:
                print()
            if len(self.possibilities[i]) == 1:
                print(self.possibilities[i][0], end='')
            else:
                print(' ', end='')
        print()

    def build_possibilities(self) -> None:
        """
        Builds the possible solutions for all of the cells. If a cell is solved it continues running
        until no more are solved during an iteration.

        Uses row, column, and box elimination, and can identify unique solutions for a number in a 
        box.

        Saves the possibilities as a class attribute.
        """
        self.possibilities = [[str(i) for i in range(1, 10)] for i in range(0, 81)]
        for i in range(0, 81):
            if self.puzzle_array[i] != ' ':
                self.possibilities[i] = [self.puzzle_array[i]]

        old_possibilities = self.number_of_possibilites()
        new_possibilities = 0
        while old_possibilities > new_possibilities:
            old_possibilities = self.number_of_possibilites()

            for i in range(0, 9):
                self.reduce_row(i)

            for i in range(0, 9):
                self.reduce_column(i)

            for i in range(0, 9):
                self.reduce_box(i)

            for i in range(0, 9):
                self.find_unique_possibilities_by_box(i)

            new_possibilities = self.number_of_possibilites()

    def reduce_row(self, row_number) -> None:
        """
        Reduces possibilities in a row.

        param row_number: the number of the row to reduce.
        """
        i = row_number * 9

        numbers_to_eliminate = []

        while i < (row_number * 9) + 9:
            if len(self.possibilities[i]) == 1:
                numbers_to_eliminate.append(self.possibilities[i][0])
            i = i + 1

        for number in numbers_to_eliminate:
            i = row_number * 9
            while i < (row_number * 9) + 9:
                if len(self.possibilities[i]) != 1 and number in self.possibilities[i]:
                    self.possibilities[i].pop(self.possibilities[i].index(number))
                i = i + 1

    def reduce_column(self, column_number) -> None:
        """
        Reduces possibilities in a column.

        param: column_number. Number of the column to reduce 0-8.
        """
        i = column_number

        numbers_to_eliminate = []

        while i < 81:
            if len(self.possibilities[i]) == 1:
                numbers_to_eliminate.append(self.possibilities[i][0])
            i = i + 9

        for number in numbers_to_eliminate:
            i = column_number
            while i < 81:
                if len(self.possibilities[i]) != 1 and number in self.possibilities[i]:
                    self.possibilities[i].pop(self.possibilities[i].index(number))
                i = i + 9

    def get_box_start_index(self, box_number) -> int:
        """
        Get the index of the first cell in a box based on box number.

        param box_number: the number of box to the index for.

        Returns: int. The index of the upper left cell in the box.
        """
        if box_number == 0:
            return 0
        elif box_number == 1:
            return 3
        elif box_number == 2:
            return 6
        elif box_number == 3:
            return 27
        elif box_number == 4:
            return 30
        elif box_number == 5:
            return 33
        elif box_number == 6:
            return 54
        elif box_number == 7:
            return 57
        elif box_number == 8:
            return 60

    def reduce_box(self, box_number) -> None:
        """
        Reduces the possibilities in a box based on given or solved cells in the box.

        param int box_number: the box number to be reduced.

        Returns: None.
        """
        i = self.get_box_start_index(box_number)
        numbers_to_eliminate = []

        for j in range(0, 3):
            if len(self.possibilities[i]) == 1:
                numbers_to_eliminate.append(self.possibilities[i][0])
            i = i + 1
            if len(self.possibilities[i]) == 1:
                numbers_to_eliminate.append(self.possibilities[i][0])
            i = i + 1
            if len(self.possibilities[i]) == 1:
                numbers_to_eliminate.append(self.possibilities[i][0])
            i = i + 7

        for number in numbers_to_eliminate:
            i = self.get_box_start_index(box_number)
            for j in range(0, 3):
                if len(self.possibilities[i]) != 1 and number in self.possibilities[i]:
                    self.possibilities[i].pop(self.possibilities[i].index(number))
                i = i + 1
                if len(self.possibilities[i]) != 1 and number in self.possibilities[i]:
                    self.possibilities[i].pop(self.possibilities[i].index(number))
                i = i + 1
                if len(self.possibilities[i]) != 1 and number in self.possibilities[i]:
                    self.possibilities[i].pop(self.possibilities[i].index(number))
                i = i + 7

    def find_unique_possibilities_by_box(self, box_number) -> None:
        """
        Looks in a box and finds a number that has only one place that it can be, and solves that cell.

        Params: int box_number. The number of the box to look in.

        Returns: None
        TODO: test more, this one is scary.
        """
        box_start = self.get_box_start_index(box_number)
        all_possibilities = []
        numbers_to_reduce = []
        not_to_eliminate = []
        i = box_start

        for j in range(0, 3):
            if len(self.possibilities[i]) > 1:
                all_possibilities = all_possibilities + self.possibilities[i]
            else:
                not_to_eliminate.append(self.possibilities[i][0])
            i = i + 1

            if len(self.possibilities[i]) > 1:
                all_possibilities = all_possibilities + self.possibilities[i]
            else:
                not_to_eliminate.append(self.possibilities[i][0])
            i = i + 1

            if len(self.possibilities[i]) > 1:
                all_possibilities = all_possibilities + self.possibilities[i]
            else:
                not_to_eliminate.append(self.possibilities[i][0])
            i = i + 7

        for j in range(0, 10):
            if all_possibilities.count(str(j)) == 1 and str(j) not in not_to_eliminate:
                numbers_to_reduce.append(str(j))

        for number in numbers_to_reduce:
            i = box_start
            for j in range(0, 3):
                if len(self.possibilities[i]) > 1 and (number in self.possibilities[i]):
                    self.possibilities[i] = [number]
                i = i + 1
                if len(self.possibilities[i]) > 1 and (number in self.possibilities[i]):
                    self.possibilities[i] = [number]
                i = i + 1
                if len(self.possibilities[i]) > 1 and (number in self.possibilities[i]):
                    self.possibilities[i] = [number]
                i = i + 7

    def number_of_possibilites(self) -> int:
        """
        Count the number of possibilities remaining in the puzzle.

        Returns: int.
        """
        possibilities = 0

        for i in range(0, 81):
            possibilities = possibilities + len(self.possibilities[i])
        return possibilities

    def get_possibilities(self) -> list:
        """
        Get the remaining possibilities in a puzzle.

        Returns: list (of lists). 
        """
        return self.possibilities

    def get_reduced_puzzle(self) -> string:  # TODO: expand testing for this
        """
        Get the string encoding of the puzzle, with any solved cells, as a string.

        Returns: string.
        """
        reduced_puzzle = ''
        for possibility in self.possibilities:
            if len(possibility) == 1:
                reduced_puzzle = reduced_puzzle + possibility[0]
            else:
                reduced_puzzle = reduced_puzzle + '.'
        return reduced_puzzle
    
    def get_possibilities_for_web(self) -> list:
        """
        Get the string encodings of the reduced puzzle. Returns a list of strings.
        For cells that have multiple possibilities still, it will format them so that
        the preformatting checker will leave them alone and they'll be readable.

        Returns: list (of strings).
        """
        def build_hints_string(remaining_hints) -> str:
            hint_string = ''
            index = 1
            for letter in remaining_hints:
                while int(letter) != index:
                    hint_string = hint_string + ' '
                    if index % 3 == 0:
                        hint_string = hint_string + '\n'
                    index += 1
                hint_string = hint_string + letter
                if index % 3 ==0:
                    hint_string = hint_string + '\n'
                index = index+1
                
            return hint_string
        
        formatted_list = []

        for cell in self.possibilities:
            if len(cell) == 1:
                formatted_list.append(cell)
            else:
                formatted_list.append( build_hints_string(cell) )

        return formatted_list
    
class BacktrackSolver:
    """
    BacktrackSolver object

    Uses modified backtracking algorithm to find solutions to sudoku puzzles.
    """
    def __init__(self, **kwargs) -> None:
        """
        Creates Backtrack solver object.

        Parameters
            **kwargs
                Accepts 'puzzle = <puzzle string>' or 'solver = <SudokuSolver>'
        """
        if 'puzzle' in kwargs:
            self.puzzle_string = kwargs['puzzle']
            self.solver = SudokuSolver( puzzle_string = self.puzzle_string)
            self.possibilities = self.solver.possibilities
        elif 'solver' in kwargs:
            if type( kwargs['solver'] ) is not SudokuSolver:
                raise TypeError('kwargs[\'solver\'] is not SudokuSolver')
            self.solver = kwargs['solver']
            self.puzzle = self.solver.puzzle_string
            self.possibilities = self.solver.possibilities
        else:
            raise KeyError('Use \'puzzle = <puzzle>\' or \'solver = <solver>\'')

    def solve_by_backtrack(self) -> list:
        """
        Solves a sudoku puzzle using a brute force back tracking method.

        Returns: list. A solved sudoku puzzle.
        TODO: optimize this
        """
        root_solver = self.solver.copy_solver()
        step_solver = self.solver.copy_solver()

        i = 0
        guesses = []
       
        while i < 81: 
            if (step_solver.possibilities[i]  == root_solver.possibilities[i]
                and len(step_solver.possibilities[i]) == 1 ):
                i += 1 
            elif (i,step_solver.possibilities[i][0]) in guesses:
                i += 1
            else:
                guesses.append( (i,step_solver.possibilities[i][0]) )
                step_solver.possibilities[i] = [step_solver.possibilities[i][0]]

                valid_guess = step_solver.check_valid_solution() # TODO: optimize right here. this is not efficient 

                if not valid_guess:
                    bad_guess = guesses.pop()

                    step_solver.possibilities[i] = copy.copy(root_solver.possibilities[i])

                    to_remove = []
                    for possibility in step_solver.possibilities[i]:
                        if int(possibility) <= int(bad_guess[1]):
                            to_remove.append(possibility)

                    for item in to_remove:
                        step_solver.possibilities[i].remove(item)
                    
                    while len( step_solver.possibilities[i] ) == 0:

                        step_solver.possibilities[i] = copy.copy(root_solver.possibilities[i])

                        i = guesses[-1][0]

                        bad_guess = guesses.pop()

                        step_solver.possibilities[i] = copy.copy(root_solver.possibilities[i])

                        to_remove = []
                        for possibility in step_solver.possibilities[i]:
                            if int(possibility) <= int(bad_guess[1]):
                                to_remove.append(possibility)

                        for item in to_remove:
                            step_solver.possibilities[i].remove(item)
                    if guesses:
                        i = guesses[-1][0]
                    else:
                        i = 0
                else:
                    i += 1
        self.solver.possibilities = step_solver.get_possibilities()
        return step_solver.get_possibilities()
    
    """
    Backtracking algorithm

    Make two copies of the solver
    i = 0, guesses = empty stack

    while i < 81
        if cell i is solved or a guess has been made for it
            skip it: i+=1
        else
            add (i, guess) to guesses
            set the cell to match that guess
            see if it's a valid guess

            if not valid:
                pop the bad guess from guesses
                reset the cell without the invalid guesses

                while cell i is empty (due to removing bad guesses)
                    continue popping and resetting
                
                if the stack is empty
                    just set i=0
            else
                i+=1
    """