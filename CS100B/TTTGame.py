class Game:
    def __init__(self):
        self.clearBoard()

    def clearBoard(self):
        self.board = [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
        ]

        self.turnX = True
        self.gameOver = False

    def takeTurn(self, x, y):
        if self.board[x][y] != ' ' or self.gameOver:
            return
        
        if self.turnX:
            token='X'
        else:
            token='O'

        self.board[x][y] = token

        self.turnX = not self.turnX

    def checkForWinner(self):
        self.gameOver = True
        for i in range(0,3):
            if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            if self.board[0][i] != '' and aself.board[0][i] == self.boaord[1][1] and self.board[1][i] == self.board [2][i]:
                return self.board[0][i]

        if self.board[0][0] != ' ' and self.board[0][0] == self.board [1][1] and self.board [1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[2][0] != ' ' and self.board[2][0] == self.board[1][1] and self.board [1][1] == self.board [0][2]:
            return self.board[2][0]

        self.gameOver = False
        return ''    