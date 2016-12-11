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
        Form.resize(198, 166)
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
        Form.resize(218, 359)
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
        self.checkBox1 = QtGui.QCheckBox(Form)
        self.checkBox1.setGeometry(QtCore.QRect(10, 190, 85, 18))
        self.checkBox1.setObjectName(_fromUtf8("checkBox1"))
        self.checkBox2 = QtGui.QCheckBox(Form)
        self.checkBox2.setGeometry(QtCore.QRect(10, 210, 85, 18))
        self.checkBox2.setObjectName(_fromUtf8("checkBox2"))
        self.checkBox3 = QtGui.QCheckBox(Form)
        self.checkBox3.setGeometry(QtCore.QRect(10, 230, 85, 18))
        self.checkBox3.setObjectName(_fromUtf8("checkBox3"))
        self.checkBox4 = QtGui.QCheckBox(Form)
        self.checkBox4.setGeometry(QtCore.QRect(10, 250, 85, 18))
        self.checkBox4.setObjectName(_fromUtf8("checkBox4"))
        self.checkBox5 = QtGui.QCheckBox(Form)
        self.checkBox5.setGeometry(QtCore.QRect(10, 270, 85, 18))
        self.checkBox5.setObjectName(_fromUtf8("checkBox5"))
        self.checkBox6 = QtGui.QCheckBox(Form)
        self.checkBox6.setGeometry(QtCore.QRect(10, 290, 85, 18))
        self.checkBox6.setObjectName(_fromUtf8("checkBox6"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Battery Level", None))
        self.var_label_1.setText(_translate("Form", "TextLabel", None))
        self.var_label_2.setText(_translate("Form", "TextLabel", None))
        self.checkBox1.setText(_translate("Form", "Not Set", None))
        self.checkBox2.setText(_translate("Form", "Not Set", None))
        self.checkBox3.setText(_translate("Form", "Not Set", None))
        self.checkBox4.setText(_translate("Form", "Not Set", None))
        self.checkBox5.setText(_translate("Form", "Not Set", None))
        self.checkBox6.setText(_translate("Form", "Not Set", None))

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
        Form.resize(248, 359)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
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
        self.checkBox1 = QtGui.QCheckBox(Form)
        self.checkBox1.setGeometry(QtCore.QRect(10, 190, 191, 18))
        self.checkBox1.setObjectName(_fromUtf8("checkBox1"))
        self.checkBox2 = QtGui.QCheckBox(Form)
        self.checkBox2.setGeometry(QtCore.QRect(10, 210, 191, 18))
        self.checkBox2.setObjectName(_fromUtf8("checkBox2"))
        self.checkBox3 = QtGui.QCheckBox(Form)
        self.checkBox3.setGeometry(QtCore.QRect(10, 230, 191, 18))
        self.checkBox3.setObjectName(_fromUtf8("checkBox3"))
        self.checkBox4 = QtGui.QCheckBox(Form)
        self.checkBox4.setGeometry(QtCore.QRect(10, 250, 191, 18))
        self.checkBox4.setObjectName(_fromUtf8("checkBox4"))
        self.checkBox5 = QtGui.QCheckBox(Form)
        self.checkBox5.setGeometry(QtCore.QRect(10, 270, 191, 18))
        self.checkBox5.setObjectName(_fromUtf8("checkBox5"))
        self.checkBox6 = QtGui.QCheckBox(Form)
        self.checkBox6.setGeometry(QtCore.QRect(10, 290, 191, 18))
        self.checkBox6.setObjectName(_fromUtf8("checkBox6"))
        self.shutdownButton = QtGui.QPushButton(Form)
        self.shutdownButton.setGeometry(QtCore.QRect(50, 311, 110, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.shutdownButton.setFont(font)
        self.shutdownButton.setObjectName(_fromUtf8("shutdownButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Battery Level", None))
        self.var_label_1.setText(_translate("Form", "TextLabel", None))
        self.var_label_2.setText(_translate("Form", "TextLabel", None))
        self.checkBox1.setText(_translate("Form", "Not Set", None))
        self.checkBox2.setText(_translate("Form", "Not Set", None))
        self.checkBox3.setText(_translate("Form", "Not Set", None))
        self.checkBox4.setText(_translate("Form", "Not Set", None))
        self.checkBox5.setText(_translate("Form", "Not Set", None))
        self.checkBox6.setText(_translate("Form", "Not Set", None))
        self.shutdownButton.setText(_translate("Form", "Shutdown", None))

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
        Form.resize(248, 417)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.batteryPB = QtGui.QProgressBar(Form)
        self.batteryPB.setGeometry(QtCore.QRect(10, 20, 151, 23))
        self.batteryPB.setProperty("value", 24)
        self.batteryPB.setObjectName(_fromUtf8("batteryPB"))
        self.checkBox1 = QtGui.QCheckBox(Form)
        self.checkBox1.setGeometry(QtCore.QRect(10, 119, 191, 18))
        self.checkBox1.setObjectName(_fromUtf8("checkBox1"))
        self.checkBox2 = QtGui.QCheckBox(Form)
        self.checkBox2.setGeometry(QtCore.QRect(10, 139, 191, 18))
        self.checkBox2.setObjectName(_fromUtf8("checkBox2"))
        self.checkBox3 = QtGui.QCheckBox(Form)
        self.checkBox3.setGeometry(QtCore.QRect(10, 159, 191, 18))
        self.checkBox3.setObjectName(_fromUtf8("checkBox3"))
        self.checkBox4 = QtGui.QCheckBox(Form)
        self.checkBox4.setGeometry(QtCore.QRect(10, 179, 191, 18))
        self.checkBox4.setObjectName(_fromUtf8("checkBox4"))
        self.checkBox5 = QtGui.QCheckBox(Form)
        self.checkBox5.setGeometry(QtCore.QRect(10, 199, 191, 18))
        self.checkBox5.setObjectName(_fromUtf8("checkBox5"))
        self.checkBox6 = QtGui.QCheckBox(Form)
        self.checkBox6.setGeometry(QtCore.QRect(10, 219, 191, 18))
        self.checkBox6.setObjectName(_fromUtf8("checkBox6"))
        self.shutdownButton = QtGui.QPushButton(Form)
        self.shutdownButton.setGeometry(QtCore.QRect(50, 240, 110, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.shutdownButton.setFont(font)
        self.shutdownButton.setObjectName(_fromUtf8("shutdownButton"))
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(10, 100, 121, 18))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(15, 302, 191, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Battery Level", None))
        self.checkBox1.setText(_translate("Form", "Not Set", None))
        self.checkBox2.setText(_translate("Form", "Not Set", None))
        self.checkBox3.setText(_translate("Form", "Not Set", None))
        self.checkBox4.setText(_translate("Form", "Not Set", None))
        self.checkBox5.setText(_translate("Form", "Not Set", None))
        self.checkBox6.setText(_translate("Form", "Not Set", None))
        self.shutdownButton.setText(_translate("Form", "Shutdown", None))
        self.checkBox.setText(_translate("Form", "Data Inspector", None))
        self.label_2.setText(_translate("Form", "Click to Display", None))
        self.label_3.setText(_translate("Form", "INSIGHT GUI", None))

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
        Form.resize(285, 417)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.batteryPB = QtGui.QProgressBar(Form)
        self.batteryPB.setGeometry(QtCore.QRect(10, 30, 151, 23))
        self.batteryPB.setProperty("value", 24)
        self.batteryPB.setObjectName(_fromUtf8("batteryPB"))
        self.checkBox1 = QtGui.QCheckBox(Form)
        self.checkBox1.setGeometry(QtCore.QRect(10, 119, 191, 18))
        self.checkBox1.setObjectName(_fromUtf8("checkBox1"))
        self.checkBox2 = QtGui.QCheckBox(Form)
        self.checkBox2.setGeometry(QtCore.QRect(10, 139, 191, 18))
        self.checkBox2.setObjectName(_fromUtf8("checkBox2"))
        self.checkBox3 = QtGui.QCheckBox(Form)
        self.checkBox3.setGeometry(QtCore.QRect(10, 159, 191, 18))
        self.checkBox3.setObjectName(_fromUtf8("checkBox3"))
        self.checkBox4 = QtGui.QCheckBox(Form)
        self.checkBox4.setGeometry(QtCore.QRect(10, 179, 191, 18))
        self.checkBox4.setObjectName(_fromUtf8("checkBox4"))
        self.checkBox5 = QtGui.QCheckBox(Form)
        self.checkBox5.setGeometry(QtCore.QRect(10, 199, 191, 18))
        self.checkBox5.setObjectName(_fromUtf8("checkBox5"))
        self.checkBox6 = QtGui.QCheckBox(Form)
        self.checkBox6.setGeometry(QtCore.QRect(10, 219, 191, 18))
        self.checkBox6.setObjectName(_fromUtf8("checkBox6"))
        self.shutdownButton = QtGui.QPushButton(Form)
        self.shutdownButton.setGeometry(QtCore.QRect(90, 260, 110, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.shutdownButton.setFont(font)
        self.shutdownButton.setObjectName(_fromUtf8("shutdownButton"))
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(10, 100, 121, 18))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(5, 302, 271, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Battery Level", None))
        self.checkBox1.setText(_translate("Form", "Not Set", None))
        self.checkBox2.setText(_translate("Form", "Not Set", None))
        self.checkBox3.setText(_translate("Form", "Not Set", None))
        self.checkBox4.setText(_translate("Form", "Not Set", None))
        self.checkBox5.setText(_translate("Form", "Not Set", None))
        self.checkBox6.setText(_translate("Form", "Not Set", None))
        self.shutdownButton.setText(_translate("Form", "Shutdown", None))
        self.checkBox.setText(_translate("Form", "Data Inspector", None))
        self.label_2.setText(_translate("Form", "Click to Display", None))
        self.label_3.setText(_translate("Form", "INSIGHT GUI", None))

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
        Form.resize(285, 417)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.batteryPB = QtGui.QProgressBar(Form)
        self.batteryPB.setGeometry(QtCore.QRect(10, 30, 151, 23))
        self.batteryPB.setProperty("value", 24)
        self.batteryPB.setObjectName(_fromUtf8("batteryPB"))
        self.checkBox1 = QtGui.QCheckBox(Form)
        self.checkBox1.setGeometry(QtCore.QRect(10, 119, 251, 18))
        self.checkBox1.setObjectName(_fromUtf8("checkBox1"))
        self.checkBox2 = QtGui.QCheckBox(Form)
        self.checkBox2.setGeometry(QtCore.QRect(10, 139, 261, 18))
        self.checkBox2.setObjectName(_fromUtf8("checkBox2"))
        self.checkBox3 = QtGui.QCheckBox(Form)
        self.checkBox3.setGeometry(QtCore.QRect(10, 159, 251, 18))
        self.checkBox3.setObjectName(_fromUtf8("checkBox3"))
        self.checkBox4 = QtGui.QCheckBox(Form)
        self.checkBox4.setGeometry(QtCore.QRect(10, 179, 261, 18))
        self.checkBox4.setObjectName(_fromUtf8("checkBox4"))
        self.checkBox5 = QtGui.QCheckBox(Form)
        self.checkBox5.setGeometry(QtCore.QRect(10, 199, 261, 18))
        self.checkBox5.setObjectName(_fromUtf8("checkBox5"))
        self.checkBox6 = QtGui.QCheckBox(Form)
        self.checkBox6.setGeometry(QtCore.QRect(10, 219, 261, 18))
        self.checkBox6.setObjectName(_fromUtf8("checkBox6"))
        self.shutdownButton = QtGui.QPushButton(Form)
        self.shutdownButton.setGeometry(QtCore.QRect(90, 260, 110, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.shutdownButton.setFont(font)
        self.shutdownButton.setObjectName(_fromUtf8("shutdownButton"))
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(10, 100, 221, 18))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(5, 302, 271, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Battery Level", None))
        self.checkBox1.setText(_translate("Form", "Not Set", None))
        self.checkBox2.setText(_translate("Form", "Not Set", None))
        self.checkBox3.setText(_translate("Form", "Not Set", None))
        self.checkBox4.setText(_translate("Form", "Not Set", None))
        self.checkBox5.setText(_translate("Form", "Not Set", None))
        self.checkBox6.setText(_translate("Form", "Not Set", None))
        self.shutdownButton.setText(_translate("Form", "Shutdown", None))
        self.checkBox.setText(_translate("Form", "Data Inspector", None))
        self.label_2.setText(_translate("Form", "Click to Display", None))
        self.label_3.setText(_translate("Form", "INSIGHT GUI", None))

