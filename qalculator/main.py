#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re
from math import *
from PyQt4 import QtCore, QtGui
from ui_window import Ui_MainWindow

utf8 = lambda x : unicode(QtCore.QString.fromUtf8(x))


class Window(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '(', ')',
                        '+', '-', '*', '/', '√', 'sin', 'cos', 'tan', 'sin⁻¹', 'cos⁻¹',
                        'tan⁻¹', 'log', '10^', 'ln', 'e^', '∛', '^', 'π', 'e']
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.initUi()
        self.simpleMode()
        self.clear_text = False # Clears text box after equals is pressed.
        self.ans = ''

    def initUi(self):
        self.actionSimple.triggered.connect(self.simpleMode)
        self.actionScientific.triggered.connect(self.scientificMode)
        self.btnGrp = QtGui.QButtonGroup(self)
        btns = [self.b0, self.b1, self.b2, self.b3, self.b4, self. b5, self.b6, self.b7,
                self.b8, self.b9, self.point, self.startbracket, self.endbracket, self.plus,
                self.minus, self.multiply, self.divide, self.root, self.sin, self.cos,
                self.tan, self.asin, self.acos, self.atan, self.log, self.antilog, self.ln,
                self.antiln, self.cuberoot, self.power, self.pi, self.e]
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
        expr = processExpression(unicode(self.lineEdit.text()))
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

    def simpleMode(self):
        self.scientificWidget.hide()
        wait(30)
        self.resize(330, 390)

    def scientificMode(self):
        self.scientificWidget.show()

#------------------- Process Expression -------------------------
# cube root function
cbrt = lambda x : x**(1.0/3)

def addMultSign(matchobj):
    ''' inserts * sign between num and bracket.
    e.g - Converts '7(' to '7*(' and 2√3 to 2*√3 '''
    expr = matchobj.group()
    return expr[0] + '*' + expr[1:]

def replaceConst(obj):
    return obj.group(1) + '*' + obj.group(3)

def toFloat(matchobj):
    ''' Converts all integers to float in re match object '''
    num = matchobj.group()
    if '.' not in num: num = num+'.0'
    elif num.startswith('.'):
        num = '0'+num
    return num

def toFunc(obj):
    return obj.group(1) + '(' + obj.group(9) + ')'

reg_number = re.compile('([\d]+([.][\d]+)?)|([.][\d]+)')
reg_bracket = re.compile('(\d(\(|[a-z]))|(\)\d)')
reg_constant = re.compile('((pi)|e)(\d)')
reg_func = re.compile('((log)|(ln)|(sin)|(cos)|(tan)|(sqrt)|(cbrt))(\d+\.\d+)')

def processExpression(expr):
    # Convert integers to float before evaluation to improve accuracy
    expr = reg_number.sub(toFloat, expr)
    items =        ['sin⁻¹', 'cos⁻¹', 'tan⁻¹', '√', '∛', 'π', '^']
    replacements = ['asin', 'acos', 'atan', 'sqrt', 'cbrt', 'pi', '**']
    for i in range(len(items)):
        expr = expr.replace(utf8(items[i]), replacements[i])
    expr = reg_bracket.sub(addMultSign, expr)
    expr = reg_constant.sub(replaceConst, expr)
    expr = reg_func.sub(toFunc, expr)
    expr = expr.replace('log', 'log10')
    expr = expr.replace('ln', 'log')
    return expr

def wait(millisec):
    loop = QtCore.QEventLoop()
    QtCore.QTimer.singleShot(millisec, loop.quit)
    loop.exec_()

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Window()
    calc.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
