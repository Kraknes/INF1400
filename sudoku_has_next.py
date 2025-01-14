class Sudoku_reader:

    def __init__(self, filename):
        self.file = open(filename, "r")
        self.current_line = 0
        
    def has_next_board(self):
        try:
            pass
        except:
            return("None")
