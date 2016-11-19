from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pyqtgraph as pg
import numpy as np

class VariableSelectPanel(QDockWidget):

    def __init__(self, title="", parent=None):
        QDockWidget.__init__(self, parent)
        self.setMinimumSize(200, 200)
        self.setWindowTitle(title)
        self.check_boxes = dict()

    def addCheckBox(self, name):
        print('yo')

