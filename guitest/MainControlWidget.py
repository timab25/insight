from PyQt4.QtGui import *
from PyQt4.QtCore import *
import main_control

class MainControlWidget(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        self.ui = main_control.Ui_Form()
        self.ui.setupUi(self)

        self.ui.batteryPB.setValue(0)

    def updateBatterStatus(self, level):
        self.ui.batteryPB.setValue(level)

