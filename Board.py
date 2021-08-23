class Board:
    BoardMatrix = [[" ", " ", " ", " "],
                   [" ", " ", " ", " "],
                   [" ", " ", " ", " "],
                   [" ", " ", " ", " "],
                   [" ", " ", " ", " "],
                   [" ", " ", " ", " "],
                   [" ", " ", " ", " "],
                   [" ", " ", " ", " "]]

    def __init__(self):
        self.board = self.BoardMatrix

    def put(self, mark, i, j):
        self.board[i][j] = mark

    def is_full(self):
        for i in range(7):
            for j in range(4):
                if self.board[i][j] == " ":
                    return False
        return True

    def reset_board(self):
        for i in range(7):
            for j in range(4):
                self.board[i][j] = " "

    def get_board(self):
        copy_board = [[" ", " ", " ", " "],
                       [" ", " ", " ", " "],
                       [" ", " ", " ", " "],
                       [" ", " ", " ", " "],
                       [" ", " ", " ", " "],
                       [" ", " ", " ", " "],
                       [" ", " ", " ", " "],
                       [" ", " ", " ", " "]]
        for i in range(8):
            for j in range(4):
                copy_board[i][j] = self.board[i][j]
        return copy_board

