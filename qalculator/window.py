# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sat Jul  1 10:25:39 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(380, 388)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lcd = QtGui.QLCDNumber(self.centralwidget)
        self.lcd.setStyleSheet(_fromUtf8("background-color: rgb(161, 236, 143);"))
        self.lcd.setFrameShape(QtGui.QFrame.Panel)
        self.lcd.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcd.setLineWidth(2)
        self.lcd.setSmallDecimalPoint(True)
        self.lcd.setNumDigits(11)
        self.lcd.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd.setObjectName(_fromUtf8("lcd"))
        self.verticalLayout.addWidget(self.lcd)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.minus = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.minus.setFont(font)
        self.minus.setAutoFillBackground(False)
        self.minus.setObjectName(_fromUtf8("minus"))
        self.gridLayout_2.addWidget(self.minus, 1, 3, 1, 1)
        self.multiply = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.multiply.setFont(font)
        self.multiply.setAutoFillBackground(False)
        self.multiply.setObjectName(_fromUtf8("multiply"))
        self.gridLayout_2.addWidget(self.multiply, 2, 3, 1, 1)
        self.b2 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setAutoFillBackground(False)
        self.b2.setObjectName(_fromUtf8("b2"))
        self.gridLayout_2.addWidget(self.b2, 3, 1, 1, 1)
        self.b1 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setAutoFillBackground(False)
        self.b1.setObjectName(_fromUtf8("b1"))
        self.gridLayout_2.addWidget(self.b1, 3, 0, 1, 1)
        self.b5 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.b5.setFont(font)
        self.b5.setAutoFillBackground(False)
        self.b5.setObjectName(_fromUtf8("b5"))
        self.gridLayout_2.addWidget(self.b5, 2, 1, 1, 1)
        self.b3 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.b3.setFont(font)
        self.b3.setAutoFillBackground(False)
        self.b3.setObjectName(_fromUtf8("b3"))
        self.gridLayout_2.addWidget(self.b3, 3, 2, 1, 1)
        self.b6 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.b6.setFont(font)
        self.b6.setAutoFillBackground(False)
        self.b6.setObjectName(_fromUtf8("b6"))
        self.gridLayout_2.addWidget(self.b6, 2, 2, 1, 1)
        self.b9 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.b9.setFont(font)
        self.b9.setAutoFillBackground(False)
        self.b9.setObjectName(_fromUtf8("b9"))
        self.gridLayout_2.addWidget(self.b9, 1, 2, 1, 1)
        self.b4 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.b4.setFont(font)
        self.b4.setAutoFillBackground(False)
        self.b4.setObjectName(_fromUtf8("b4"))
        self.gridLayout_2.addWidget(self.b4, 2, 0, 1, 1)
        self.divide = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.divide.setFont(font)
        self.divide.setAutoFillBackground(False)
        self.divide.setObjectName(_fromUtf8("divide"))
        self.gridLayout_2.addWidget(self.divide, 3, 3, 1, 1)
        self.equals = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.equals.setFont(font)
        self.equals.setObjectName(_fromUtf8("equals"))
        self.gridLayout_2.addWidget(self.equals, 4, 3, 1, 1)
        self.b8 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.b8.setFont(font)
        self.b8.setAutoFillBackground(False)
        self.b8.setObjectName(_fromUtf8("b8"))
        self.gridLayout_2.addWidget(self.b8, 1, 1, 1, 1)
        self.b7 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.b7.setFont(font)
        self.b7.setAutoFillBackground(False)
        self.b7.setObjectName(_fromUtf8("b7"))
        self.gridLayout_2.addWidget(self.b7, 1, 0, 1, 1)
        self.plus = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.plus.setFont(font)
        self.plus.setAutoFillBackground(False)
        self.plus.setObjectName(_fromUtf8("plus"))
        self.gridLayout_2.addWidget(self.plus, 0, 3, 1, 1)
        self.startbracket = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.startbracket.setFont(font)
        self.startbracket.setObjectName(_fromUtf8("startbracket"))
        self.gridLayout_2.addWidget(self.startbracket, 0, 1, 1, 1)
        self.endbracket = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.endbracket.setFont(font)
        self.endbracket.setObjectName(_fromUtf8("endbracket"))
        self.gridLayout_2.addWidget(self.endbracket, 0, 2, 1, 1)
        self.clrAll = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.clrAll.setFont(font)
        self.clrAll.setObjectName(_fromUtf8("clrAll"))
        self.gridLayout_2.addWidget(self.clrAll, 0, 0, 1, 1)
        self.clr = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.clr.setFont(font)
        self.clr.setAutoFillBackground(False)
        self.clr.setObjectName(_fromUtf8("clr"))
        self.gridLayout_2.addWidget(self.clr, 4, 0, 1, 1)
        self.b0 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.b0.setFont(font)
        self.b0.setAutoFillBackground(False)
        self.b0.setObjectName(_fromUtf8("b0"))
        self.gridLayout_2.addWidget(self.b0, 4, 1, 1, 1)
        self.point = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.point.setFont(font)
        self.point.setAutoFillBackground(False)
        self.point.setObjectName(_fromUtf8("point"))
        self.gridLayout_2.addWidget(self.point, 4, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Qalculator", None))
        self.minus.setText(_translate("MainWindow", "-", None))
        self.minus.setShortcut(_translate("MainWindow", "-", None))
        self.multiply.setText(_translate("MainWindow", "*", None))
        self.multiply.setShortcut(_translate("MainWindow", "*", None))
        self.b2.setText(_translate("MainWindow", "2", None))
        self.b2.setShortcut(_translate("MainWindow", "2", None))
        self.b1.setText(_translate("MainWindow", "1", None))
        self.b1.setShortcut(_translate("MainWindow", "1", None))
        self.b5.setText(_translate("MainWindow", "5", None))
        self.b5.setShortcut(_translate("MainWindow", "5", None))
        self.b3.setText(_translate("MainWindow", "3", None))
        self.b3.setShortcut(_translate("MainWindow", "3", None))
        self.b6.setText(_translate("MainWindow", "6", None))
        self.b6.setShortcut(_translate("MainWindow", "6", None))
        self.b9.setText(_translate("MainWindow", "9", None))
        self.b9.setShortcut(_translate("MainWindow", "9", None))
        self.b4.setText(_translate("MainWindow", "4", None))
        self.b4.setShortcut(_translate("MainWindow", "4", None))
        self.divide.setText(_translate("MainWindow", "/", None))
        self.divide.setShortcut(_translate("MainWindow", "/", None))
        self.equals.setText(_translate("MainWindow", "=", None))
        self.equals.setShortcut(_translate("MainWindow", "=", None))
        self.b8.setText(_translate("MainWindow", "8", None))
        self.b8.setShortcut(_translate("MainWindow", "8", None))
        self.b7.setText(_translate("MainWindow", "7", None))
        self.b7.setShortcut(_translate("MainWindow", "7", None))
        self.plus.setText(_translate("MainWindow", "+", None))
        self.plus.setShortcut(_translate("MainWindow", "+", None))
        self.startbracket.setText(_translate("MainWindow", "(", None))
        self.startbracket.setShortcut(_translate("MainWindow", "(", None))
        self.endbracket.setText(_translate("MainWindow", ")", None))
        self.endbracket.setShortcut(_translate("MainWindow", ")", None))
        self.clrAll.setText(_translate("MainWindow", "AC", None))
        self.clrAll.setShortcut(_translate("MainWindow", "Shift+Backspace", None))
        self.clr.setText(_translate("MainWindow", "Clr", None))
        self.clr.setShortcut(_translate("MainWindow", "Backspace", None))
        self.b0.setText(_translate("MainWindow", "0", None))
        self.b0.setShortcut(_translate("MainWindow", "0", None))
        self.point.setText(_translate("MainWindow", ".", None))
        self.point.setShortcut(_translate("MainWindow", ".", None))

