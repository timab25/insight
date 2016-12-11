from PyQt4.QtGui import *
from PyQt4.QtCore import *
import data_inspector

class DataInspector(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        self.ui = data_inspector.Ui_Form()
        self.ui.setupUi(self)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderItem(0, QStandardItem(QString("Variable")))
        self.model.setHorizontalHeaderItem(1, QStandardItem(QString("Value")))

        self.ui.tableView.setModel(self.model)