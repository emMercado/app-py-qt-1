#app

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("app.ui", self)
        #eventbutton
        self.add.clicked.connect(self.add_click)
        self.add.clicked.connect(self.print_click)
        self.subtract.clicked.connect(self.print_click_subtract)
        self.subtract.clicked.connect(self.down_click)

    def print_click(self):
        print("click!")
    def print_click_subtract(self):
        print("se resto!")

    def add_click(self):
        value = int(self.ticket.text())
        values = 1
        self.ticket.setText(str(values + value))
    def down_click(self):
        value = int(self.ticket.text())
        values = -1
        self.ticket.setText(str(values + value))


app = QApplication([])
win = window()
win.show()
app.exec_()