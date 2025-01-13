from sudoku_reader import Sudoku_reader

class Board:
    # It is your task to subclass this in order to make it more fit
    # to be a sudoku board

    def __init__(self, nums):
        # Nums parameter is a 2D list, like what the sudoku_reader returns
        self.n_rows = len(nums[0]) # = 9   
        self.n_cols = len(nums) # = 9
        self.nums = nums
        # self.sudoku må super() hentes til subclass sudoku

    

    def _set_up_nums(self):
        liste = []
        # Set up the squares on the board (ints into Square objects)
        for i in range(self.n_cols):
            for j in range (self.n_rows):
                s = Square() 
                s.number = self.nums[i][j]
                liste.append(s)

        return liste
        
        # Lager squares her med nummer fra en sudoku. Skal lage 81 classe squares
        # Hvordan hente man nummeran? 

    def _set_up_elems(self):
        # You should set up links between your squares and elements
        # (rows, columns, boxes)
        # Henter squares fra _set_up_nums og legger dem til i riktig element. 
        
        pass    

    def solve(self):
        # Your solving algorithm goes here!
        pass

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
    def __init__(self, square_lists):
        super().__init__(self)
        self.square_lists = super(board)._set_up_nums()
                         
    # Henter inn solve funksjon fra board. I teorien skal board classe funke til alle brettspill, så den må være generell
        pass

class Square:
    def __init__(self):
        self.number = None
        self.mapped = False
        self.row = None
        self.column = None
        self.box = None
         

    def legal_numbers(self, element):
        for value in element:
            if self.mapped == True:
                break
            if value in self.legal_numbers:
                self.legal_numbers.remove(value)

            
    def insert_number(self,value):
        self.number = value
            

class element:
    def __init__(self, square_list, element_name):
        self.squares = square_list
        self.illegal_number = []
        self.legal_numbers = [1,2,3,4,5,6,7,8,9]   
        self.element_name = element_name
        self.making_element()
        
    ## Lager element, enten rad, kolonne eller box av en liste på 9 class square. lager en egen liste for "illegal numbers" som ikke kan endres. Har "navn" på hva hvilke elemeent det er. 
    def making_element(self, element_name):
        for square in self.squares:
            if square.number is None:
                square.number = 0
            if square.number != 0:
                self.illegal_number.append(square.number)
            
        
        
    
    

        

if __name__ == "__main__":
    # Test code...
    reader = Sudoku_reader("sudoku_10.csv")
    # kanskje endre denne til sudokuo istedenfor board? 
    board = Board(reader.next_board())
    liste = board._set_up_nums()
    
    # print(board)