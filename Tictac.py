from board import Board
from sudoku_reader import Sudoku_reader

class TicTacBoard(Board):
    def __init__(self, nums):
        super().__init__(nums)
        self.nums = nums
        self.square_list, self.vertical_list, self.horisontal_list = [], [], []
        
        self.solved = 0
        
    def _set_up_nums(self):
        for i in range(9):
            for j in range(9):
                s = Square()
                self.vertical_list[j].append(s)
                self.horisontal_list[i].append(s)
                self.square_list.append(s)
                
    def _set_up_elems(self):
        for _ in range(9):
            element = []
            self.vertical_list.append(element)
            self.horisontal_list.append(element)

        
    def play(self):
        self._set_up_elems()
        self._set_up_nums()
        while self.solved == 0:
            row = input("Player 1: Enter your row: ")
            col = input("Player 1: Enter your column: ")
            print(type(row))
            print(type(int(row)))
            row = int(row)
            col = int(col)
            self.nums[row][col] = 1
            row = input("Player 2: Enter your row: ")
            col = input("Player 2: Enter your column: ")
            self.nums[int(row)][int(col)] = 2
            print(self)
            
            
    
    def __str__(self):
        return super().__str__()
        
    def check_winner(self):
        pass
        
class Square:
    def __init__(self):
        self.spot = 0
    
if __name__ == "__main__":
    # Test code...
    reader = Sudoku_reader("sudoku_10.csv") 
    board = TicTacBoard(reader.next_board())
    board.play()
    
    print(board)
        
        

    
    