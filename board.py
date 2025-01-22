from sudoku_reader import Sudoku_reader
import time
#Test test ugheb


class Board:
    """
    Main class inheritence for Sudoboard.
    Contains three functions: setting up numbers to squares, squares to elements, and solving sudoku.
    """
    
    def __init__(self, nums):
        
        """
        Initiating the given board to self. Saving the number of rows and columns.
        """

        self.n_rows = len(nums[0])
        self.n_cols = len(nums)
        self.nums = nums
        
    def _set_up_nums(self):
        pass

    def _set_up_elems(self):
       pass
            
    def solve(self):
        pass

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
    
    """ 
    Initiate the class Sudokuboard by inhereting from Board class. 
    Crates list of all squares (81 squares total)
    Creates empty lists of used squares, and all of elements in a board (9 of each)
    Inherits the solve() function from the Board class in __init__()

    Args:
        Board (nums): Takes in the nums[][] of a sudoku problem board
    """
    
    def __init__(self, nums):
        super().__init__(nums)
        self.solved = 0
        self.used_squares, self.row_list, self.column_list, self.box_list = [], [], [], []
        self.square_lists = self._set_up_nums()
        self._set_up_elems()
        while self.solved == 0:
            self.Solve()

    def _set_up_nums(self):    
        """
        Setting up the number to squares, and putting squares back into the sudoko board.
        """
        liste = []
        for i in range(self.n_cols):
            for j in range(self.n_rows):
                s = Square(self)
                s.number = self.nums[i][j]
                self.nums[i][j] = s
                liste.append(s)
        return liste

    def _set_up_elems(self):
        """
        Setting up 9x elements of row, column and box. 
        Using the lists of all squares, and appends them to its respective row, column and box elements
        """

        for _ in range(9):
            self.row_list.append(Element()) 
            self.column_list.append(Element())
            self.box_list.append(Element())

        for i, s in enumerate(self.square_lists):
            s.column = self.column_list[i%9]
            s.row = self.row_list[int(i/9)]
            s.box = self.box_list[int((i%9)/3)+(int((i/9)/3)*3)]
            s.column.squares_in_element.append(s)
            s.row.squares_in_element.append(s)
            s.box.squares_in_element.append(s)
                   
        for j in range(9):
            self.row_list[j].illegal_numbers()
            self.column_list[j].illegal_numbers()
            self.box_list[j].illegal_numbers()
            
    def Solve(self):
        """
        Solving algorithm. 
        Iterating through all squares and check if each square can put a legal number on the board.
        If a square has no legal values, solved is set to False and solve() is started again. 
        """
        self.solved = True
        for square in self.square_lists:
            if square.number != 0:
                continue
            else:
                square.checking_legal_nr()
                if square.number == 0:
                    self.solved = False
                    break
                else:
                    continue
        
class Square:
    
    """
    Square class:
    Variables: its number, elements for row column and box, list of forbidden numbers, 
    link to sudoku class, and iterator
    """
    
    def __init__(self, sudoku):
        self.number = 0
        self.row = None
        self.column = None
        self.box = None
        self.legal_numbers = [1,2,3,4,5,6,7,8,9]
        self.sudoku = sudoku
        self.iterator = 0
        
    def checking_legal_nr(self):
        
        """
        Updates its legal_number list by removing all numbers that are present in its element illegal_lists.
        Square picks a number from the legal_number list to the board by its self.iterator. 
        If no legal numbers are available, backtrack() is initiated. 
        """
        
        self.legal_numbers = [item for item in self.legal_numbers if item not in self.row.illegal_list]     # Fjerner alle ulovlige tall i lovlige tall listen til square
        self.legal_numbers = [item for item in self.legal_numbers if item not in self.column.illegal_list]
        self.legal_numbers = [item for item in self.legal_numbers if item not in self.box.illegal_list]
        if len(self.legal_numbers) == 0:
            self.backtrack()
        else:
            self.insert_number()
            
    def insert_number(self):
        
        """
        Inserts number from its legal_number list.
        Self.iterator dictates which number from the list is used.
        Appends to the used_square list of the sudoku class.
        Add its number to the illegal list of its elements. 
        """
        
        self.number = self.legal_numbers[self.iterator]
        self.sudoku.used_squares.append(self)
        self.add_illegal_nr()
        
    def add_illegal_nr(self):
        
        """
        After square insert legal number, the element list of illegal numbers are updated
        """
        
        self.row.illegal_list.append(self.number)
        self.column.illegal_list.append(self.number)
        self.box.illegal_list.append(self.number)
        
    def backtrack(self):
        
        """
        Backtracking mechanism, when a square has no legal numbers it goes to this function.
        Goes through all previous used squares and resets itself and elements, but not its iterator. 
        The square with no legal numbers will initiate iterator_reset function and resets legal_number list.
        Resets used_square list for new solve() from the start
        """
        
        self.sudoku.used_squares.append(self)
        for s in reversed(self.sudoku.used_squares):
            if len(s.legal_numbers) == 0:
                s.iterator_reset()
                s.legal_numbers = [1,2,3,4,5,6,7,8,9]
            else:
                s.row.illegal_list.remove(s.number)
                s.column.illegal_list.remove(s.number)
                s.box.illegal_list.remove(s.number)
                s.number = 0
                s.legal_numbers = [1,2,3,4,5,6,7,8,9]
        self.sudoku.used_squares = []
        
    def iterator_reset(self):
        
        """
        Backbone of backtrack(). It resets iterator if its out of bounds from legal_number list. 
        Finds itself in the used_square list, and changes the iterator of the previous square. 
        iterator_reset starts again for previous square to check if its iterator is out of bounds. 
        """
        
        if self.iterator == (len(self.legal_numbers)):
            self.iterator = 0
            self_nr_in_list = self.sudoku.used_squares.index(self)
            prev_square = self.sudoku.used_squares[self_nr_in_list-1]
            prev_square.iterator += 1
            prev_square.iterator_reset()
            
    def __str__(self):
        return str(self.number)
    
class Element:
    
    """
    Element creater. Creates empty list for the squares it contains and the forbidden numbers the squares can't use.
    """
    
    def __init__(self):
        self.squares_in_element = []
        self.illegal_list = []
        
    def illegal_numbers(self):
        
        """
        Adds all the numbers from its squares in its illegal number list.
        This list will be used by other squares to know what numbers are forbidden to use. 
        """
        
        for square in self.squares_in_element:
            if square.number != 0:
                self.illegal_list.append(square.number)
                
if __name__ == "__main__":
    start = time.time()
    SUDOKU_PROBLEMS = "sudoku_1M.csv"
    reader = Sudoku_reader(SUDOKU_PROBLEMS)
    N = 1000
    print("\nStart of solving", N ,"sudoku problems:\n")
    for _ in range(N):
        board = Sudokuboard(reader.next_board())
        print(board)
    end = time.time()
    length = end - start
    print("\nThis algorithm used", length, "seconds solving", N, "sudoku problems!\n")
