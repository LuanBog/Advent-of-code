# Board layout:
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]

class Board:
    def __init__(self, board_numbers):
        self.board = []
        self.moves = 0
        self.score = 0
        self.previous_number_plotted = 0

        # Creates the board
        new_row = []
        for index, number in enumerate(board_numbers):
            new_row.append(str(number))

            # Appends the new row to the board
            if (index + 1) % 5 == 0:
                self.board.append(new_row.copy())
                new_row.clear()
            
    def plot_number(self, number):
        for y_index, y in enumerate(self.board):
            for x_index, x in enumerate(y):
                if x == str(number):
                    self.board[y_index][x_index] = 'X'
                    break

        self.moves += 1
        self.previous_number_plotted = number

    def has_won(self):
        return (self.board[0][0] == 'X' and self.board[0][1] == 'X' and self.board[0][2] == 'X' and self.board[0][3] == 'X' and self.board[0][4] == 'X') or  (self.board[1][0] == 'X' and self.board[1][1] == 'X' and self.board[1][2] == 'X' and self.board[1][3] == 'X' and self.board[1][4] == 'X') or  (self.board[2][0] == 'X' and self.board[2][1] == 'X' and self.board[2][2] == 'X' and self.board[2][3] == 'X' and self.board[2][4] == 'X') or  (self.board[3][0] == 'X' and self.board[3][1] == 'X' and self.board[3][2] == 'X' and self.board[3][3] == 'X' and self.board[3][4] == 'X') or  (self.board[4][0] == 'X' and self.board[4][1] == 'X' and self.board[4][2] == 'X' and self.board[4][3] == 'X' and self.board[4][4] == 'X') or  (self.board[4][0] == 'X' and self.board[4][1] == 'X' and self.board[4][2] == 'X' and self.board[4][3] == 'X' and self.board[4][4] == 'X') or  (self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X' and self.board[3][0] == 'X' and self.board[4][0] == 'X') or  (self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X' and self.board[3][1] == 'X' and self.board[4][1] == 'X') or  (self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2] == 'X' and self.board[3][2] == 'X' and self.board[4][2] == 'X') or  (self.board[0][3] == 'X' and self.board[1][3] == 'X' and self.board[2][3] == 'X' and self.board[3][3] == 'X' and self.board[4][3] == 'X') or  (self.board[0][4] == 'X' and self.board[1][4] == 'X' and self.board[2][4] == 'X' and self.board[3][4] == 'X' and self.board[4][4] == 'X') or  (self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X' and self.board[3][3] == 'X' and self.board[4][4] == 'X') or  (self.board[0][4] == 'X' and self.board[1][3] == 'X' and self.board[2][2] == 'X' and self.board[3][1] == 'X' and self.board[4][0] == 'X')

    def calculate_score(self):
        unplotted_sum = 0

        for y in self.board:
            for x in y:
                if x != 'X':
                    unplotted_sum += int(x)

        self.score = unplotted_sum * self.previous_number_plotted

    # Not necessary but why not
    def display(self):
        for y in self.board:
            print(y)

