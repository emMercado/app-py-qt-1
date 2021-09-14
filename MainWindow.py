# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from OtherWindow import Ui_OtherWindow
from Calculator import Ui_calculator
from Crud import Ui_crud

class Ui_window(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi (self.window)
        #window.hide()
        self.window.show()

    def openWindowCalc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_calculator()
        self.ui.setupUi (self.window)
        #window.hide()
        self.window.show()

    def openWindowCrud(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_crud()
        self.ui.setupUi (self.window)
        #window.hide()
        self.window.show()

    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(40, 30, 191, 25))
        self.btn_open.setObjectName("btn_open")
        self.btn_calc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calc.setGeometry(QtCore.QRect(40, 90, 191, 25))
        self.btn_calc.setObjectName("btn_calc")
        self.btnCrud = QtWidgets.QPushButton(self.centralwidget)
        self.btnCrud.setGeometry(QtCore.QRect(40, 150, 191, 25))
        self.btnCrud.setObjectName("btnCrud")
        window.setCentralWidget(self.centralwidget)

        self.btn_open.clicked.connect(self.openWindow)
        self.btn_calc.clicked.connect(self.openWindowCalc)
        self.btnCrud.clicked.connect(self.openWindowCrud)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Main window xd"))
        self.btn_open.setText(_translate("window", "Count Add Subtract"))
        self.btn_calc.setText(_translate("window", "Calculator"))
        self.btnCrud.setText(_translate("window", "Crud"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
