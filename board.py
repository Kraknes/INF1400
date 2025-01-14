from sudoku_reader import Sudoku_reader
#test

class Board:
    # It is your task to subclass this in order to make it more fit
    # to be a sudoku board

    def __init__(self, nums):
        # Nums parameter is a 2D list, like what the sudoku_reader returns
        self.n_rows = len(nums[0]) # = 9   
        self.n_cols = len(nums) # = 9
        self.nums = nums
        
    def _set_up_nums(self):
        liste = []                                  # Set up the squares on the board (ints into Square objects)
        for i in range(self.n_cols):
            for j in range (self.n_rows):           # Lager squares her med nummer fra en sudoku. Skal lage 81 classe squares
                s = Square(self) 
                s.number = self.nums[i][j]
                s.mapped_check()                    # En checker slik at man ikke kan endre dette tallet noensinne
                liste.append(s)                     # Lager en liste over alle squares som returneres til Sudoku class
        return liste                        

    def _set_up_elems(self):
        # You should set up links between your squares and elements
        # (rows, columns, boxes)
        for i in range(len(self.square_lists)):     # Går gjennom alle squares i square_list og referer til kolonne, rad og box.
            s = self.square_lists[i] 
            s.column = self.column_list[i%9]
            s.row = self.row_list[int(i/9)]
            s.box = self.box_list[int((i%9)/3)+(int((i/9)/3)*3)]
            s.column.squaresinElement.append(s)
            s.row.squaresinElement.append(s)
            s.box.squaresinElement.append(s)
            
        for j in range(9):                           # Går gjennom squares og lager liste over ulovlige tall i elementene:
            self.row_list[j].illegal_numbers()
            self.column_list[j].illegal_numbers()
            self.box_list[j].illegal_numbers()

    def solve(self):
        # Your solving algorithm goes here!
        for square in self.square_lists:
            if square.mapped == True:
                print("\n Square is mapped, next square")
            else:
                for square in self.square_lists:
                    square.checking_legal_nr()
                    
    # Makes it possible to print a board in a sensible format
    def __str__(self):
        r = "Board with " + str(self.n_rows) + " rows and " + str(self.n_cols) + " columns:\n"
        r += "[["
        for num in self.nums:
            for elem in num:
                r += elem.__str__() + ", "
            r = r[:-2] + "]" + "\n ["
        r = r[:-3] + "]"
        return r

class Sudokuboard(Board):
    def __init__(self, nums):
        super().__init__(nums)                                                                     # Arver init av Board klassen
        self.used_squares, self.row_list, self.column_list, self.box_list = [], [], [], []         # Lager tomme element lister
        self.square_lists = super()._set_up_nums()                                                 # Lager squares av sudoku brettet
        for i in range(9):                                                                         # Lager rad, kolonne og box elementer
            self.row_list.append(element(i))
            self.column_list.append(element(i))
            self.box_list.append(element(i))
        super()._set_up_elems()                                             # Setter opp respektive elementer til hver square
        super().solve()
        
class Square:
    def __init__(self, sudoku):
        self.number = None
        self.mapped = False
        self.row = None
        self.column = None
        self.box = None
        self.legal_numbers = [1,2,3,4,5,6,7,8,9]
        self.used_nums = []
        self.sudoku = sudoku
        self.iterator = 0

    def mapped_check(self):
        if self.number != 0:
            self.mapped = True
         
    def checking_legal_nr(self):
        if self.mapped == True:
            pass
        else:
            self.legal_numbers = [item for item in self.legal_numbers if item not in self.row.illegal_list]     # Fjerner alle ulovlige tall i lovlige tall listen til square
            self.legal_numbers = [item for item in self.legal_numbers if item not in self.column.illegal_list]
            self.legal_numbers = [item for item in self.legal_numbers if item not in self.box.illegal_list]
            if len(self.legal_numbers) == 0:
                self.backtrack()
            else:
                self.insert_number()

    def insert_number(self):
        self.number = self.legal_numbers[self.iterator]
        self.used_nums.append(self.number)
        self.sudoku.used_squares.append(self)
        self.add_illegal_nr()
        print("\n", self.number)
    
    def add_illegal_nr(self):
        self.row.illegal_list.append(self.number)
        self.column.illegal_list.append(self.number)
        self.box.illegal_list.append(self.number)
        
    def backtrack(self):
        for s in self.sudoku.used_squares:
            if len(s.legal_numbers) == 0:
                pass
            else:
                s.row.illegal_list.remove(s.legal_numbers[s.iterator])
                s.column.illegal_list.remove(s.legal_numbers[s.iterator])
                s.box.illegal_list.remove(s.legal_numbers[s.iterator])
                s.used_nums = []
                # s.legal_numbers = [1,2,3,4,5,6,7,8,9]
        square = self.sudoku.used_squares[(len(self.sudoku.used_squares)-1)]
        square.iterator_reset()
        self.sudoku.used_squares = []
        self.sudoku.solve()              # Kaller sudoku klassen for å kjøre algoritmen på nytt
        
        # Mye tull her, må gjennom på nytt
        
    def iterator_reset(self):            # Iterator som går gjennom alle tall i legal_numbers hvis det blir backtracking
        if self.iterator >= (len(self.legal_numbers))-1:
            s = self.sudoku.used_squares[(len(self.sudoku.used_squares)-2)]  # Hvis en square har brukt alle sine muligheter så endrer iteratoren på den som kom før
            s.iterator += 1
            s.iterator_reset()
            self.iterator = 0
        else:
            self.iterator += 1
        
        
class element:
    def __init__(self, element_name):
        self.element_name = element_name
        self.squaresinElement = []
        self.illegal_list = []   

        
    ## Lager element, enten rad, kolonne eller box av en liste på 9 class square. lager en egen liste for "illegal numbers" som ikke kan endres. Har "navn" på hva hvilke elemeent det er. 
    def illegal_numbers(self):
        for square in self.squaresinElement:
            if square.number != 0:
                self.illegal_list.append(square.number)
            
if __name__ == "__main__":
    # Test code...
    reader = Sudoku_reader("sudoku_10.csv") 
    board = Sudokuboard(reader.next_board())
    
    print(board)