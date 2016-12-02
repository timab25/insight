# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_control.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(178, 166)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label.setObjectName("label")
        self.batteryPB = QtWidgets.QProgressBar(Form)
        self.batteryPB.setGeometry(QtCore.QRect(10, 30, 151, 23))
        self.batteryPB.setProperty("value", 24)
        self.batteryPB.setObjectName("batteryPB")
        self.var_label_1 = QtWidgets.QLabel(Form)
        self.var_label_1.setGeometry(QtCore.QRect(10, 60, 59, 15))
        self.var_label_1.setObjectName("var_label_1")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 80, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.var_label_2 = QtWidgets.QLabel(Form)
        self.var_label_2.setGeometry(QtCore.QRect(100, 60, 59, 15))
        self.var_label_2.setObjectName("var_label_2")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2.setGeometry(QtCore.QRect(100, 80, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.var_label_3 = QtWidgets.QLabel(Form)
        self.var_label_3.setGeometry(QtCore.QRect(10, 110, 59, 15))
        self.var_label_3.setObjectName("var_label_3")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_3.setGeometry(QtCore.QRect(10, 130, 64, 23))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.var_label_4 = QtWidgets.QLabel(Form)
        self.var_label_4.setGeometry(QtCore.QRect(100, 110, 59, 15))
        self.var_label_4.setObjectName("var_label_4")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_4.setGeometry(QtCore.QRect(100, 130, 64, 23))
        self.lcdNumber_4.setObjectName("lcdNumber_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Battery Level"))
        self.var_label_1.setText(_translate("Form", "TextLabel"))
        self.var_label_2.setText(_translate("Form", "TextLabel"))
        self.var_label_3.setText(_translate("Form", "TextLabel"))
        self.var_label_4.setText(_translate("Form", "TextLabel"))

