import sys 
import random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from TTTGame import *

class MainWindow(QWidget):
    def __init__(self, parent = None ):
        super(MainWindow, self ).__init__(parent)
        self.resize(500,500)
        self.setWindowTitle("T-T-T")

        self.game = Game()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(Qt.black)
        size = event.rect().size()

        colsize = size.width() // 5
        rowsize = size.height() // 5

        qp.drawLine(colsize*2, rowsize, colsize*2, rowsize*4)

        qp.drawLine(colsize *3, rowsize, colsize*3, rowsize*4)

        qp.drawLine(colsize, rowsize*2, colsize*4, rowsize*2)
        
        qp.drawLine(colsize, rowsize*3, colsize*4, rowsize*3)

        for r in range(0,3):
            for c in range(0,3):
                if self.game.board[c][r] == 'X':
                    self.drawX(qp, c, r, colsize, rowsize)
                elif self.game.board[c][r] == 'O':
                    self.drawO(qp, c, r, colsize, rowsize)

    def drawX(self, qp, c, r, colsize, rowsize):
        x = colsize + c*colsize
        y = rowsize + r*rowsize
        qp.drawLine(x, y, x+colsize, y+rowsize)
        qp.drawLine(x+colsize, y, x, y+rowsize)


    def mousePressEvent(self, event):
        size = self.size()

        colsize = size.width() // 5
        rowsize = size.height() // 5

        col = (event.x() // colsize) - 1
        row = (event.y() // rowsize) - 1
        if col >= 0 and col < 3 and row >= 0 and row < 3:
            self.game.takeTurn(col, row)

            self.repaint



def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
