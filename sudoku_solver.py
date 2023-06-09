import string

class SudokuSolver:
    def __init__(self, sudoku_string_):
        puzzle_array = []
        processor = 0
        while processor < len(sudoku_string_):
            if sudoku_string_[processor].isnumeric():
                puzzle_array.append(sudoku_string_[processor])
            else: #TODO: account for new lines when inputting puzzle
                puzzle_array.append(' ')
            processor = processor + 1
        self.puzzle_array = puzzle_array
        self.puzzle_string = sudoku_string_
        #print(len(self.puzzle_array))
        #print( self.puzzle_array )
    
    def __str__(self) -> str:
        sudoku_string = ' --- --- ---\n'
        
        for i in range( len(self.puzzle_array) ):
            if i % 9 == 0 and i != 0:
                sudoku_string = sudoku_string + '|\n --- --- ---\n'
            if i % 3 == 0:
                sudoku_string = sudoku_string + '|'
            
            sudoku_string = sudoku_string + self.puzzle_array[i]

        sudoku_string = sudoku_string + '|\n --- --- ---'

        return sudoku_string


if __name__ == '__main__':
    puzzle = '**14728**\
**41*57**\
5*******3\
71*5***82\
4*******9\
32***9*74\
1*******7\
**38*79**\
**72614**'
    #print(puzzle)
    my_puz = SudokuSolver(puzzle)
    print( my_puz )
