import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


"""
def window():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setGeometry(0,0,1920,1280)
    w.setWindowTitle("PyQt5")

    b = QLabel(w)
    b.setText("Hello World!")
    b.move(200,500)

    w.showMaximized()
    sys.exit(app.exec_())

    

if __name__ == '__main__':
    window()
"""

class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.resize(200,50)
        self.setWindowTitle("Battle Suggestion")

        self.label = QLabel(self)
        self.label.setText("How to faint that pokemon!")
        self.label.move(800,50)

        font = QFont()
        font.setFamily('Windlass')
        font.setPointSize(16)
        self.label.setFont(font)

        self.btn = QPushButton(self)
        self.btn.move(650,600)
        self.btn.setText("Sumbit")


        self.label2 = QLabel(self)
        self.label2.setText("Please Enter your Pokemons name")
        self.label2.move(150,450)
        self.label2 = QLineEdit(self)
        self.label2.move(200,500)

        self.enemylabel = QLabel(self)
        self.enemylabel.setText("Please enter your enemy pokemon")
        self.enemylabel.move(600,450)
        self.enemyinput= QLineEdit(self)
        self.enemyinput.move(650,500)

        self.btn.clicked.connect(self.getinfo)

        label = QLabel(self)
        pixmap = QPixmap('R.jfif')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())

    def getinfo(self):
        UPoke = self.label2.text()
        EPoke =  self.enemyinput.text()
        print(UPoke + "   ___VS___   " + EPoke)


def main():
    app = QApplication(sys.argv)
    w = mainwindow()
    w.show()
    sys.exit(app.exec_())

if __name__== '__main__':
    main()