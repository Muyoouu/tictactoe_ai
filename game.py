
class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for i in range(9)]
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')
    

    @staticmethod
    def print_board_nums():
        number_board = [[str(j) for j in range(i*3, (i+1)*3)] for i in range(3)]
        for row in number_board:
            print('|' + '|'.join(row) + '|')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # Check the current row index
        row_i = square // 3
        row = self.board[row_i*3:(row_i+1)*3]
        # Check win condition in the current row
        if all([s == letter for s in row]):
            return True
        
        # Check the current column index
        column_i = square % 3
        column = [self.board[column_i+(i*3)] for i in range(3)]
        # Check win condition in the current column
        if all([s == letter for s in column]):
            return True
        
        # Check diagonal only if current square is in [0,4,8] or [2,4,6]
        # Note that diagonal squares number is 'even' numbers only, thus check if square is even
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([s == letter for s in diagonal2]):
                return True
        
        # After passing all winning condition, return false i.e. no winner yet
        return False
    
    # Check if there is any empty square
    def empty_square(self):
        return ' ' in self.board
    
    # Count empty square
    def count_empty_square(self):
        return self.board.count(' ')
    
    # Return index/number of empty squares
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']