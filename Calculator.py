# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calculator(object):
    def setupUi(self, calculator):
        calculator.setObjectName("calculator")
        calculator.resize(667, 428)
        self.centralwidget = QtWidgets.QWidget(calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setGeometry(QtCore.QRect(160, 270, 89, 25))
        self.btnOk.setObjectName("btnOk")
        self.radioBtnMult = QtWidgets.QRadioButton(self.centralwidget)
        self.radioBtnMult.setGeometry(QtCore.QRect(460, 60, 111, 23))
        self.radioBtnMult.setObjectName("radioBtnMult")
        self.radioBtnDiv = QtWidgets.QRadioButton(self.centralwidget)
        self.radioBtnDiv.setGeometry(QtCore.QRect(460, 90, 111, 23))
        self.radioBtnDiv.setObjectName("radioBtnDiv")
        self.radioBtnSumar = QtWidgets.QRadioButton(self.centralwidget)
        self.radioBtnSumar.setGeometry(QtCore.QRect(460, 120, 112, 23))
        self.radioBtnSumar.setObjectName("radioBtnSumar")
        self.radioBtnRestar = QtWidgets.QRadioButton(self.centralwidget)
        self.radioBtnRestar.setGeometry(QtCore.QRect(460, 150, 112, 23))
        self.radioBtnRestar.setObjectName("radioBtnRestar")
        self.inputNum_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNum_1.setGeometry(QtCore.QRect(150, 90, 221, 25))
        self.inputNum_1.setObjectName("inputNum_1")
        self.inputNum_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNum_2.setGeometry(QtCore.QRect(150, 160, 221, 25))
        self.inputNum_2.setObjectName("inputNum_2")
        self.lblResult = QtWidgets.QLabel(self.centralwidget)
        self.lblResult.setGeometry(QtCore.QRect(220, 220, 67, 17))
        self.lblResult.setObjectName("lblResult")
        self.num_2 = QtWidgets.QLabel(self.centralwidget)
        self.num_2.setGeometry(QtCore.QRect(210, 130, 67, 17))
        self.num_2.setObjectName("num_2")
        self.num_1 = QtWidgets.QLabel(self.centralwidget)
        self.num_1.setGeometry(QtCore.QRect(210, 60, 67, 17))
        self.num_1.setObjectName("num_1")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(280, 270, 89, 25))
        self.btnCancel.setObjectName("btnCancel")
        self.lbl_igual = QtWidgets.QLabel(self.centralwidget)
        self.lbl_igual.setGeometry(QtCore.QRect(236, 190, 51, 20))
        self.lbl_igual.setObjectName("lbl_igual")
        calculator.setCentralWidget(self.centralwidget)

        self.btnOk.clicked.connect(self.btnOk_click)
        self.btnCancel.clicked.connect(self.btnCancel_click)

        self.retranslateUi(calculator)
        QtCore.QMetaObject.connectSlotsByName(calculator)

    def btnOk_click(self):

        valueNum_1 = int(self.inputNum_1.text())
        valueNum_2 = int(self.inputNum_2.text())

        if self.radioBtnSumar.isChecked():
            self.lblResult.setText(str(valueNum_1 + valueNum_2))
        elif self.radioBtnRestar.isChecked():
            self.lblResult.setText(str(valueNum_1 - valueNum_2))
        elif self.radioBtnMult.isChecked():
            self.lblResult.setText(str(valueNum_1 * valueNum_2))
        elif self.radioBtnDiv.isChecked():
            self.lblResult.setText(str(valueNum_1 / valueNum_2))

    def btnCancel_click(self):
        self.lblResult.setText(str("Result"))
        self.inputNum_1.setText(str(""))
        self.inputNum_2.setText(str(""))

    def retranslateUi(self, calculator):
        _translate = QtCore.QCoreApplication.translate
        calculator.setWindowTitle(_translate("calculator", "Calculator"))
        self.btnOk.setText(_translate("calculator", "Calcular"))
        self.radioBtnMult.setText(_translate("calculator", "Multiplicar"))
        self.radioBtnDiv.setText(_translate("calculator", "Dividir"))
        self.radioBtnSumar.setText(_translate("calculator", "Sumar"))
        self.radioBtnRestar.setText(_translate("calculator", "Restar"))
        self.lblResult.setText(_translate("calculator", "Resultado"))
        self.num_2.setText(_translate("calculator", "Number 2"))
        self.num_1.setText(_translate("calculator", "Number 1"))
        self.btnCancel.setText(_translate("calculator", "Clean"))
        self.lbl_igual.setText(_translate("calculator", "="))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calculator = QtWidgets.QMainWindow()
    ui = Ui_calculator()
    ui.setupUi(calculator)
    calculator.show()
    sys.exit(app.exec_())
