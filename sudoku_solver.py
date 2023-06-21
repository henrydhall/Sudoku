import string

class SudokuSolver:
    def __init__(self, sudoku_string_):
        puzzle_array = []
        processor = 0
        while processor < len(sudoku_string_) and len(puzzle_array) < 81:
            if sudoku_string_[processor].isnumeric():
                puzzle_array.append(sudoku_string_[processor])
            else: #TODO: account for new lines when inputting puzzle
                puzzle_array.append(' ')
            processor = processor + 1
        self.puzzle_array = puzzle_array
        self.puzzle_string = sudoku_string_
        self.build_possibilities()
        #TODO: check that a puzzle is valid
    
    def __str__(self) -> str:
        sudoku_string = ' --- --- ---\n'
        
        for i in range( len(self.puzzle_array) ):
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
        for i in range(81):
            if i % 9 == 0 and i != 0:
                print()
            if len( self.possibilities[i] ) == 1:
                print( self.possibilities[i][0], end='' )
            else:
                print(' ',end='')
        print()

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
                self.reduce_box(i)

            for i in range(0,9):
                self.find_unique_possibilities_by_box(i)

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

    def get_box_start_index(self, box_number) -> int:
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
        
        i = self.get_box_start_index(box_number)
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
            i = self.get_box_start_index(box_number)
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

    def find_unique_possibilities_by_box(self, box_number) -> None:

        #TODO: test this more, this one of all of them is the scariest so far
        box_start = self.get_box_start_index(box_number)
        all_possibilities = []
        numbers_to_reduce = []
        not_to_eliminate = []
        i = box_start

        for j in range(0,3):
            if len( self.possibilities[i] ) > 1:
                all_possibilities = all_possibilities + self.possibilities[i]
            else:
                not_to_eliminate.append( self.possibilities[i][0] )
            i = i+1

            if len( self.possibilities[i] ) > 1:
                all_possibilities = all_possibilities + self.possibilities[i]
            else:
                not_to_eliminate.append( self.possibilities[i][0] )
            i = i+1

            if len( self.possibilities[i] ) > 1:
                all_possibilities = all_possibilities + self.possibilities[i]
            else:
                not_to_eliminate.append( self.possibilities[i][0] )
            i = i+7

        for j in range(0,9):
            if all_possibilities.count(str(j)) == 1 and str(j) not in not_to_eliminate:
                numbers_to_reduce.append(str(j))

        for number in numbers_to_reduce:
            i = box_start
            for j in range(0,3):
                if len( self.possibilities[i] ) > 1 and (number in self.possibilities[i]):
                    self.possibilities[i] = [number]
                i = i+1
                if len( self.possibilities[i] ) > 1 and (number in self.possibilities[i]):
                    self.possibilities[i] = [number]
                i = i+1
                if len( self.possibilities[i] ) > 1 and (number in self.possibilities[i]):
                    self.possibilities[i] = [number]
                i = i+7

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
                possibilities = possibilities + ' '
        return possibilities

if __name__ == '__main__':
    puzzle_1 = \
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
    my_puz = SudokuSolver(puzzle_1)
    #print( my_puz )
    my_puz.build_possibilities()
    my_puz.print_possibilities()
    print( my_puz )

    puzzle_2 = \
'*******12\
*******_3\
*******45\
******6**\
*********\
*********\
*********\
*********\
*********'
    #puz_2 = SudokuSolver(puzzle_2)
    #puz_2.build_possibilities()
    #puz_2.print_possibilities()
    #print( puz_2.get_possibilities() )
    