#!/usr/bin/env python
import sys, re
from PyQt4 import QtCore, QtGui
from window import Ui_MainWindow

reg_number = re.compile('[\d]*([.][\d]*)?')

def toFloat(matchobj):
    num = matchobj.group()
    if '.' not in num: num = num+'.0'
    return num

class Calc(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '(', ')', '+', '-', '*', '/']
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.btnGrp = QtGui.QButtonGroup(self)
        btns = [self.b0, self.b1, self.b2, self.b3, self.b4, self. b5, self.b6, self.b7, self.b8,
                self.b9, self.point, self.startbracket, self.endbracket, self.plus, self.minus, self.multiply, self.divide]
        for btn in btns:
            self.btnGrp.addButton(btn)
        self.btnGrp.buttonClicked.connect(self.onBtnClick)
        self.equals.clicked.connect(self.equalsClicked)
        self.clrAll.clicked.connect(self.clearAll)
        self.deleteAction = QtGui.QAction(self)
        self.deleteAction.setShortcut('Backspace')
        self.deleteAction.triggered.connect(self.lineEdit.backspace)
        self.addAction(self.deleteAction)
        self.quitAction = QtGui.QAction(self)
        self.quitAction.setShortcut('Esc')
        self.quitAction.triggered.connect(self.close)
        self.addAction(self.quitAction)

    def onBtnClick(self, btn):
        btnId = self.btnGrp.id(btn)
        char = self.chars[abs(btnId)-2]
        text = self.lineEdit.text() + char
        self.lineEdit.setText(text)

    def equalsClicked(self):
        expr = reg_number.sub(toFloat, str(self.lineEdit.text()))
        self.lcd.display(eval(expr))

    def clearAll(self):
        self.lcd.display(0)
        self.lineEdit.clear()


def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calc()
    calc.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
