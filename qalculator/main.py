#!/usr/bin/env python
import sys
from PyQt4 import QtCore, QtGui
from window import Ui_MainWindow

class Calc(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.b0.clicked.connect(self.b0Clicked)
        self.b1.clicked.connect(self.b1Clicked)
        self.b2.clicked.connect(self.b2Clicked)
        self.b3.clicked.connect(self.b3Clicked)
        self.b4.clicked.connect(self.b4Clicked)
        self.b5.clicked.connect(self.b5Clicked)
        self.b6.clicked.connect(self.b6Clicked)
        self.b7.clicked.connect(self.b7Clicked)
        self.b8.clicked.connect(self.b8Clicked)
        self.b9.clicked.connect(self.b9Clicked)
        self.point.clicked.connect(self.pointClicked)
        self.plus.clicked.connect(self.plusClicked)
        self.minus.clicked.connect(self.minusClicked)
        self.multiply.clicked.connect(self.multiplyClicked)
        self.divide.clicked.connect(self.divideClicked)
        self.startbracket.clicked.connect(self.brac1Clicked)
        self.endbracket.clicked.connect(self.brac2Clicked)
        self.equals.clicked.connect(self.equalsClicked)
        self.clr.clicked.connect(self.lineEdit.backspace)
        self.clrAll.clicked.connect(self.clearAll)
        self.quitAction = QtGui.QAction(self)
        self.quitAction.setShortcut('Esc')
        self.quitAction.triggered.connect(self.close)
        self.addAction(self.quitAction)

    def equalsClicked(self):
        self.lcd.display(eval(str(self.lineEdit.text())))

    def clearAll(self):
        self.lcd.display(0)
        self.lineEdit.clear()

    def b0Clicked(self):
        text = self.lineEdit.text() + '0'
        self.lineEdit.setText(text)

    def b1Clicked(self):
        text = self.lineEdit.text() + '1'
        self.lineEdit.setText(text)

    def b2Clicked(self):
        text = self.lineEdit.text() + '2'
        self.lineEdit.setText(text)

    def b3Clicked(self):
        text = self.lineEdit.text() + '3'
        self.lineEdit.setText(text)

    def b4Clicked(self):
        text = self.lineEdit.text() + '4'
        self.lineEdit.setText(text)

    def b5Clicked(self):
        text = self.lineEdit.text() + '5'
        self.lineEdit.setText(text)

    def b6Clicked(self):
        text = self.lineEdit.text() + '6'
        self.lineEdit.setText(text)

    def b7Clicked(self):
        text = self.lineEdit.text() + '7'
        self.lineEdit.setText(text)

    def b8Clicked(self):
        text = self.lineEdit.text() + '8'
        self.lineEdit.setText(text)

    def b9Clicked(self):
        text = self.lineEdit.text() + '9'
        self.lineEdit.setText(text)

    def pointClicked(self):
        text = self.lineEdit.text() + '.'
        self.lineEdit.setText(text)

    def plusClicked(self):
        text = self.lineEdit.text() + '+'
        self.lineEdit.setText(text)

    def minusClicked(self):
        text = self.lineEdit.text() + '-'
        self.lineEdit.setText(text)

    def multiplyClicked(self):
        text = self.lineEdit.text() + '*'
        self.lineEdit.setText(text)

    def divideClicked(self):
        text = self.lineEdit.text() + '/'
        self.lineEdit.setText(text)

    def brac1Clicked(self):
        text = self.lineEdit.text() + '('
        self.lineEdit.setText(text)

    def brac2Clicked(self):
        text = self.lineEdit.text() + ')'
        self.lineEdit.setText(text)

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calc()
    calc.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
