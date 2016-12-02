# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_control.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(178, 166)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.batteryPB = QtGui.QProgressBar(Form)
        self.batteryPB.setGeometry(QtCore.QRect(10, 30, 151, 23))
        self.batteryPB.setProperty("value", 24)
        self.batteryPB.setObjectName(_fromUtf8("batteryPB"))
        self.var_label_1 = QtGui.QLabel(Form)
        self.var_label_1.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.var_label_1.setObjectName(_fromUtf8("var_label_1"))
        self.var_label_2 = QtGui.QLabel(Form)
        self.var_label_2.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.var_label_2.setObjectName(_fromUtf8("var_label_2"))
        self.text_1 = QtGui.QLabel(Form)
        self.text_1.setGeometry(QtCore.QRect(10, 80, 151, 17))
        self.text_1.setText(_fromUtf8(""))
        self.text_1.setObjectName(_fromUtf8("text_1"))
        self.text_2 = QtGui.QLabel(Form)
        self.text_2.setGeometry(QtCore.QRect(10, 130, 151, 17))
        self.text_2.setText(_fromUtf8(""))
        self.text_2.setObjectName(_fromUtf8("text_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Battery Level", None))
        self.var_label_1.setText(_translate("Form", "TextLabel", None))
        self.var_label_2.setText(_translate("Form", "TextLabel", None))

