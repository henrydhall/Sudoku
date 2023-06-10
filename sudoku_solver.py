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

    def print_possibilities(self) -> None:
        for i in range(81):
            if i % 9 == 0:
                print()
            if len( self.possibilities[i] ) == 1:
                print( self.possibilities[i][0], end='' )

    def build_possibilities(self) -> None:
        self.possibilities = [ [ str(i) for i in range(1,10) ] for i in range(0,81) ]
        for i in range(0,81):
            if self.puzzle_array[i] != ' ':
                self.possibilities[i] = [ self.puzzle_array[i] ]

        old_possibilities = self.number_of_possibilites()
        new_possibilities = 0
        while old_possibilities > new_possibilities:

            old_possibilities = self.number_of_possibilites()

            for i in range(0,9):
                self.reduce_row(i)

            for i in range(0,9):
                self.reduce_column(i)

            for i in range(0,9):
                self.reduce_group(i)

            new_possibilities = self.number_of_possibilites()
    

    def reduce_row( self, row_number ) -> None:
        i = row_number * 9

        numbers_to_eliminate = []

        while i < (row_number*9) + 9:
            if len( self.possibilities[i] ) == 1:
                numbers_to_eliminate.append( self.possibilities[i][0] )
            i = i+1

        for number in numbers_to_eliminate:
            i = row_number*9
            while i < (row_number*9) + 9:
                if len( self.possibilities[i] ) != 1 and number in self.possibilities[i]:
                    self.possibilities[i].pop( self.possibilities[i].index( number ) )
                i = i+1

    def reduce_column(self, column_number):

        i = column_number

        numbers_to_eliminate = []
        
        while i < 81:
            if len(self.possibilities[i]) == 1:
                numbers_to_eliminate.append( self.possibilities[i][0] )
            i = i+9

        for number in numbers_to_eliminate:
            i = column_number
            while i < 81:
                if len( self.possibilities[i] ) != 1 and number in self.possibilities[i]:
                    self.possibilities[i].pop( self.possibilities[i].index( number ) )
                i = i+9

    def get_group_start_index(self, group_number) -> int:
        if group_number == 0:
            return 0
        elif group_number == 1:
            return 3
        elif group_number == 2:
            return 6
        elif group_number == 3:
            return 27
        elif group_number == 4:
            return 30
        elif group_number == 5:
            return 33
        elif group_number == 6:
            return 54
        elif group_number == 7:
            return 57
        elif group_number == 8:
            return 60

    def reduce_group(self, group_number) -> None:
        
        i = self.get_group_start_index(group_number)
        numbers_to_eliminate = []

        for j in range(0,3):
            if len( self.possibilities[i] ) == 1:
                numbers_to_eliminate.append( self.possibilities[i][0] )
            i = i+1
            if len( self.possibilities[i] ) == 1:
                numbers_to_eliminate.append( self.possibilities[i][0] )
            i = i+1
            if len( self.possibilities[i] ) == 1:
                numbers_to_eliminate.append( self.possibilities[i][0] )
            i = i+7

        for number in numbers_to_eliminate:
            i = self.get_group_start_index(group_number)
            for j in range(0,3):
                if len( self.possibilities[i] ) != 1 and number in self.possibilities[i]:
                    self.possibilities[i].pop( self.possibilities[i].index( number ) )
                i = i+1
                if len( self.possibilities[i] ) != 1 and number in self.possibilities[i]:
                    self.possibilities[i].pop( self.possibilities[i].index( number ) )
                i = i+1
                if len( self.possibilities[i] ) != 1 and number in self.possibilities[i]:
                    self.possibilities[i].pop( self.possibilities[i].index( number ) )
                i = i+7

    def find_unique_possibilities_by_group(self, group_number) -> None:
        pass

    def number_of_possibilites(self) -> int:
        possibilities = 0

        for i in range(0,81):
            possibilities = possibilities + len( self.possibilities[i] )
        return possibilities
    
    def get_possibilities(self) -> string:
        possibilities = ''
        for possibility in self.possibilities:
            if len( possibility ) == 1:
                possibilities = possibilities + possibility[0]
            else:
                possibility = possibility + ' '
        return possibilities

if __name__ == '__main__':
    puzzle = \
'**14*28**\
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
    #print( my_puz )
    my_puz.build_possibilities()