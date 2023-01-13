#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, re
from math import *
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QActionGroup, QButtonGroup

sys.path.append(os.path.dirname(__file__))

from ui_window import Ui_MainWindow


RADIAN = False
# cube root function
cbrt = lambda x : x**(1.0/3)
# Adjustments for degree and radian modes
rad =       lambda x : x if RADIAN else x*pi/180
sine =      lambda x : sin(rad(x))
cosine =    lambda x : cos(rad(x))
tangent =   lambda x : tan(rad(x))
angle =     lambda x : x if RADIAN else x*180/pi
asine =     lambda x : angle(asin(x))
acosine =   lambda x : angle(acos(x))
atangent =  lambda x : angle(atan(x))

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '(', ')',
                        '+', '-', '*', '/', '√', 'sin', 'cos', 'tan', 'sin⁻¹', 'cos⁻¹',
                        'tan⁻¹', 'log', '10^', 'ln', 'e^', '∛', '^', 'π', 'e']
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.initUi()
        self.simpleMode()
        self.clear_text = False # Clears text box after equals is pressed.
        self.ans = ''

    def initUi(self):
        self.modeActionGrp = QActionGroup(self)
        self.modeActionGrp.addAction(self.actionSimple)
        self.modeActionGrp.addAction(self.actionScientific)
        self.actionSimple.triggered.connect(self.simpleMode)
        self.actionScientific.triggered.connect(self.scientificMode)
        self.angleActionGrp = QActionGroup(self)
        self.angleActionGrp.addAction(self.actionDegree)
        self.angleActionGrp.addAction(self.actionRadian)
        self.actionDegree.triggered.connect(self.degreeMode)
        self.actionRadian.triggered.connect(self.radianMode)

        self.btnGrp = QButtonGroup(self)
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
        self.deleteAction = QAction(self)
        self.deleteAction.setShortcut('Backspace')
        self.deleteAction.triggered.connect(self.lineEdit.backspace)
        self.addAction(self.deleteAction)
        self.equalsAction = QAction(self)
        self.equalsAction.setShortcuts(['Return','Enter'])
        self.equalsAction.triggered.connect(self.equalsClicked)
        self.addAction(self.equalsAction)

        self.insertAnsAction = QAction(self)
        self.insertAnsAction.setShortcut('A')
        self.insertAnsAction.triggered.connect(self.insertAns)
        self.addAction(self.insertAnsAction)

        self.quitAction = QAction(self)
        self.quitAction.setShortcut('Esc')
        self.quitAction.triggered.connect(self.close)
        self.addAction(self.quitAction)

    def onBtnClick(self, btn):
        btnId = self.btnGrp.id(btn)
        char = self.chars[abs(btnId)-2]
        self.insertText(char)

    def equalsClicked(self):
        expr = processExpression(self.lineEdit.text())
        print(expr)
        try:
            self.ans = eval(expr)
            self.lcd.display(self.ans)
            self.clear_text = True
        except:
            self.lcd.display('E')

    def insertAns(self):
        self.insertText(self.ans)

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

    def degreeMode(self):
        global RADIAN
        RADIAN = False

    def radianMode(self):
        global RADIAN
        RADIAN = True

#------------------- Process Expression -------------------------

def addMultSign(matchobj):
    ''' inserts * sign between num and bracket.
    e.g - Converts '7(' to '7*(' and 2√3 to 2*√3 '''
    expr = matchobj.group()
    return expr[0] + '*' + expr[1:]

def replaceConst(obj):
    return obj.group(1) + '*' + obj.group(3)

def toFunc(obj):
    return obj.group(1) + '(' + obj.group(9) + ')'

reg_number = re.compile('([\d]+([.][\d]+)?)|([.][\d]+)')
reg_bracket = re.compile('(\d(\(|[a-z]))|(\)\d)')
reg_constant = re.compile('((pi)|e)(\d)')
reg_func = re.compile('((log)|(ln)|(sin)|(cos)|(tan)|(sqrt)|(cbrt))(\d*\.?\d+)')


def processExpression(expr):
    items =        ['sin⁻¹', 'cos⁻¹', 'tan⁻¹', '√', '∛', 'π', '^']
    replacements = ['asin', 'acos', 'atan', 'sqrt', 'cbrt', 'pi', '**']
    for i in range(len(items)):
        expr = expr.replace(items[i], replacements[i])
    expr = reg_bracket.sub(addMultSign, expr)
    expr = reg_constant.sub(replaceConst, expr)
    expr = reg_func.sub(toFunc, expr)
    items =        ['log', 'ln', 'sin', 'cos', 'tan']
    replacements = ['log10', 'log', 'sine', 'cosine', 'tangent']
    for i in range(len(items)):
        expr = expr.replace(items[i], replacements[i])
    return expr

def wait(millisec):
    loop = QEventLoop()
    QTimer.singleShot(millisec, loop.quit)
    loop.exec_()

def main():
    app = QApplication(sys.argv)
    calc = Window()
    calc.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
