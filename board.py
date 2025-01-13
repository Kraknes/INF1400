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
        # self.sudoku må super() hentes til subclass sudoku

    

    def _set_up_nums(self):
        liste = []
        # Set up the squares on the board (ints into Square objects)
        for i in range(self.n_cols):
            for j in range (self.n_rows):
                s = Square() 
                s.number = self.nums[i][j]
                s.mapped_check()
                liste.append(s)

        return liste
        
        # Lager squares her med nummer fra en sudoku. Skal lage 81 classe squares
        # Hvordan hente man nummeran? 

    def _set_up_elems(self):
        # You should set up links between your squares and elements
        # (rows, columns, boxes)

        # Går gjennom alle squares i square_list og referer til kolonne, rad og box.
        for i in range(len(self.square_lists)):
            s = self.square_lists[i] 
            s.column = self.column_list[i%9]
            s.row = self.row_list[int(i/9)]
            s.box = self.box_list[int((i%9)/3)+(int((i/9)/3)*3)]
            s.column.squaresinElement.append(s)
            s.row.squaresinElement.append(s)
            s.box.squaresinElement.append(s)

        # Går gjennom squares og lager liste over ulovlige tall i elementene:
        for j in range(9):
            self.row_list[j].illegal_numbers()
            self.column_list[j].illegal_numbers()
            self.box_list[j].illegal_numbers()





         

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
    def __init__(self, nums):
        super().__init__(nums)
        # Lager tomme element lister
        self.row_list, self.column_list, self.box_list = [], [], []
        # henter in sudoku brettet
        
        # Lager 
        self.square_lists = super()._set_up_nums()
        for i in range(9):
            self.row_list.append(element(i))
            self.column_list.append(element(i))
            self.box_list.append(element(i))
        super()._set_up_elems()


                         
    # Henter inn solve funksjon fra board. I teorien skal board classe funke til alle brettspill, så den må være generell
        pass

class Square:
    def __init__(self):
        self.number = None
        self.mapped = False
        self.row = None
        self.column = None
        self.box = None

    def mapped_check(self):
        if self.number != 0:
            self.mapped = True
         

    def legal_numbers(self, element):
        for value in element:
            if self.mapped == True:
                break
            if value in self.legal_numbers:
                self.legal_numbers.remove(value)

            
    def insert_number(self,value):
        self.number = value
            

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