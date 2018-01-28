#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re
from math import sqrt
from PyQt4 import QtCore, QtGui
from window import Ui_MainWindow
utf8 = QtCore.QString.fromUtf8

reg_sqrt = re.compile('sqrt([\d]+([.][\d]+)?)')

def subSqrt(matchobj):
    expr = matchobj.group(1)
    return 'sqrt(' + expr + ')'

reg_bracket = re.compile('(\d([(]|(sqrt)))|([)]\d)')

def addMultSign(matchobj):
    ''' inserts * sign between num and bracket. e.g - Converts '7(' to '7*(' and 2√3 to 2*√3'''
    expr = matchobj.group()
    return expr[0] + '*' + expr[1:]

reg_number = re.compile('([\d]+([.][\d]+)?)|([.][\d]+)')

def toFloat(matchobj):
    ''' Converts all integers to float in re match object '''
    num = matchobj.group()
    if '.' not in num: num = num+'.0'
    elif num.startswith('.'):
        num = '0'+num
    return num

class Calc(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '(', ')', '+', '-', '*', '/', '√']
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.initUi()
        self.clear_text = False # Clears text box after equals is pressed.
        self.ans = ''

    def initUi(self):
        self.btnGrp = QtGui.QButtonGroup(self)
        btns = [self.b0, self.b1, self.b2, self.b3, self.b4, self. b5, self.b6, self.b7, self.b8,
                self.b9, self.point, self.startbracket, self.endbracket, self.plus, self.minus, self.multiply, self.divide, self.root]
        for btn in btns:
            self.btnGrp.addButton(btn)
        self.btnGrp.buttonClicked.connect(self.onBtnClick)
        self.equals.clicked.connect(self.equalsClicked)
        self.clrAll.clicked.connect(self.clearAll)
        self.deleteAction = QtGui.QAction(self)
        self.deleteAction.setShortcut('Backspace')
        self.deleteAction.triggered.connect(self.lineEdit.backspace)
        self.addAction(self.deleteAction)
        self.equalsAction = QtGui.QAction(self)
        self.equalsAction.setShortcuts(['Return','Enter'])
        self.equalsAction.triggered.connect(self.equalsClicked)
        self.addAction(self.equalsAction)

        self.insertAnsAction = QtGui.QAction(self)
        self.insertAnsAction.setShortcut('A')
        self.insertAnsAction.triggered.connect(self.insertAns)
        self.addAction(self.insertAnsAction)

        self.quitAction = QtGui.QAction(self)
        self.quitAction.setShortcut('Esc')
        self.quitAction.triggered.connect(self.close)
        self.addAction(self.quitAction)

    def onBtnClick(self, btn):
        btnId = self.btnGrp.id(btn)
        char = utf8( self.chars[abs(btnId)-2] )
        self.insertText(char)

    def equalsClicked(self):
        expr = unicode(self.lineEdit.text()).replace(unicode(utf8('√')), 'sqrt')
        # Convert integers to float before evaluation to improve accuracy
        expr = reg_number.sub(toFloat, expr)
        expr = reg_sqrt.sub(subSqrt, expr)
        expr = reg_bracket.sub(addMultSign, expr)
        print expr
        try:
            self.ans = eval(expr)
            self.lcd.display(self.ans)
            self.clear_text = True
        except:
            self.lcd.display('E')

    def insertAns(self):
        self.insertText(str(self.ans))

    def insertText(self, text):
        if self.clear_text :
            try:
                int(text)
                self.lineEdit.clear()
            except:
                pass
            self.clear_text = False
        
        self.lineEdit.insert(text)


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
