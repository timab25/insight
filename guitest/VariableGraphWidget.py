from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pyqtgraph as pg
import numpy as np

class VariableGraphWidget(QDockWidget):

    def __init__(self, title="", parent=None):
        QDockWidget.__init__(self, parent)
        self.setMinimumSize(200, 200)
        self.setWindowTitle(title)
        pg.setConfigOptions(antialias=True)
        self.win = pg.PlotWidget()  # Automatically generates grids with multiple items
        self.win.getPlotItem().enableAutoScale()
        #x = np.random.normal(size=1000)
        #y = np.random.normal(size=1000)
        #self.win.plot(x, y)
        self.setWidget(self.win)
        self.graph_data = {}

    def clearData(self):
        self.graph_data = {}

    def updateData(self, new_data):
        self.graph_data = new_data

    def render_graph(self):
        self.win.plot(self.graph_data)



