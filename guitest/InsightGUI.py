import numpy as np
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pyqtgraph as pg
from GLWindow import *
from threading import Thread
import socket
import InsightMsg_pb2
import struct
import DataManager
from VariableGraphWidget import *
import MainControlWidget
import DataInspector

class InsightGUI(QMainWindow):

    def __init__(self, parent=None):
        super(InsightGUI, self).__init__(parent)

        self.port = 8899
        self.recv_socket = None
        self.isRunning = None
        self.recv_thread = None

        self.data_manager = DataManager.DataManager()

        print("Starting server")
        self.start_server()

        self.graphWidgets = []
        self.graphWidgetsOn = []

        for i in range(6):
            self.graphWidgets.append(VariableGraphWidget(str(i+1)))
            self.graphWidgetsOn.append(False)

        self.world_view = GLWindow()
        self.world_view_dock_widget = QDockWidget("World View", self)
        self.world_view_dock_widget.setWidget(self.world_view)
        self.addDockWidget(Qt.DockWidgetArea(1), self.world_view_dock_widget)
        self.setWindowTitle("Insight GUI")

        self.data_inspector_widget = DataInspector.DataInspector()
        self.di_show = False

        self.maincontrol = MainControlWidget.MainControlWidget()
        self.maincontrol.show()

        QObject.connect(self.maincontrol.ui.checkBox1, SIGNAL('clicked()'), self.draw1)
        QObject.connect(self.maincontrol.ui.checkBox2, SIGNAL('clicked()'), self.draw2)
        QObject.connect(self.maincontrol.ui.checkBox3, SIGNAL('clicked()'), self.draw3)
        QObject.connect(self.maincontrol.ui.checkBox4, SIGNAL('clicked()'), self.draw4)
        QObject.connect(self.maincontrol.ui.checkBox5, SIGNAL('clicked()'), self.draw5)
        QObject.connect(self.maincontrol.ui.checkBox6, SIGNAL('clicked()'), self.draw6)
        QObject.connect(self.maincontrol.ui.checkBox, SIGNAL('clicked()'), self.showDI)
        QObject.connect(self.maincontrol.ui.shutdownButton, SIGNAL('clicked()'), self.shutdown_system)

        QObject.connect(self.world_view, SIGNAL('render'), self.render_graph)

    def shutdown_system(self):
        self.close()
        self.maincontrol.close()
        exit(1)

    def showDI(self):
        self.di_show = ~self.di_show
        if self.di_show:
            self.data_inspector_widget.show()
        else:
            self.data_inspector_widget.close()

    def updateDI(self):
        self.data_inspector_widget.ui.tableView.clearSpans()

        model = QStandardItemModel()
        model.setHorizontalHeaderItem(0, QStandardItem(QString("Variable")))
        model.setHorizontalHeaderItem(1, QStandardItem(QString("Value")))

        x, y, z = self.data_manager.getPosition()
        row = [QStandardItem("Pos X"), QStandardItem(str(x))]
        model.appendRow(row)
        row = [QStandardItem("Pos Y"), QStandardItem(str(y))]
        model.appendRow(row)
        row = [QStandardItem("Pos Z"), QStandardItem(str(z))]
        model.appendRow(row)

        roll, pitch, yaw = self.data_manager.getPose()
        row = [QStandardItem("Roll"), QStandardItem(str(roll))]
        model.appendRow(row)
        row = [QStandardItem("Pitch"), QStandardItem(str(pitch))]
        model.appendRow(row)
        row = [QStandardItem("Yaw"), QStandardItem(str(yaw))]
        model.appendRow(row)

        batteryStatus = self.data_manager.getBatteryLevel()
        row = [QStandardItem("Battery"), QStandardItem(str(batteryStatus))]
        model.appendRow(row)

        keys = self.data_manager.getVariableKeys()

        for key in keys:
            data = self.data_manager.getVariableData(key)
            row = [QStandardItem(key), QStandardItem(str(data[len(data)-1]))]
            model.appendRow(row)

        self.data_inspector_widget.ui.tableView.setModel(model)

    def draw1(self):
        self.graphWidgetsOn[0] = ~self.graphWidgetsOn[0]
        if self.graphWidgetsOn[0]:
            self.graphWidgets[0] = VariableGraphWidget("")
            self.addDockWidget(Qt.DockWidgetArea(1), self.graphWidgets[0])
        else:
            self.removeDockWidget(self.graphWidgets[0])

    def draw2(self):
        self.graphWidgetsOn[1] = ~self.graphWidgetsOn[1]
        if self.graphWidgetsOn[1]:
            self.graphWidgets[1] = VariableGraphWidget("")
            self.addDockWidget(Qt.DockWidgetArea(1), self.graphWidgets[1])
        else:
            self.removeDockWidget(self.graphWidgets[1])

    def draw3(self):
        self.graphWidgetsOn[2] = ~self.graphWidgetsOn[2]
        if self.graphWidgetsOn[2]:
            self.graphWidgets[2] = VariableGraphWidget("")
            self.addDockWidget(Qt.DockWidgetArea(1), self.graphWidgets[2])
        else:
            self.removeDockWidget(self.graphWidgets[2])

    def draw4(self):
        self.graphWidgetsOn[3] = ~self.graphWidgetsOn[3]
        if self.graphWidgetsOn[3]:
            self.graphWidgets[3] = VariableGraphWidget("")
            self.addDockWidget(Qt.DockWidgetArea(1), self.graphWidgets[3])
        else:
            self.removeDockWidget(self.graphWidgets[3])

    def draw5(self):
        self.graphWidgetsOn[4] = ~self.graphWidgetsOn[4]
        if self.graphWidgetsOn[4]:
            self.graphWidgets[4] = VariableGraphWidget("")
            self.addDockWidget(Qt.DockWidgetArea(1), self.graphWidgets[4])
        else:
            self.removeDockWidget(self.graphWidgets[4])

    def draw6(self):
        self.graphWidgetsOn[5] = ~self.graphWidgetsOn[5]
        if self.graphWidgetsOn[5]:
            self.graphWidgets[5] = VariableGraphWidget("")
            self.addDockWidget(Qt.DockWidgetArea(1), self.graphWidgets[5])
        else:
            self.removeDockWidget(self.graphWidgets[5])

    def render_graph(self):
        self.updateDI()

        keys = self.data_manager.getVariableKeys()
        if len(keys) == 0:
            return

        index = 0
        for key in keys:
            if index > 5:
                break

            if index == 0:
                self.maincontrol.ui.checkBox1.setText(QString(key + " Graph"))
            elif index == 1:
                self.maincontrol.ui.checkBox2.setText(QString(key + " Graph"))
            elif index == 2:
                self.maincontrol.ui.checkBox3.setText(QString(key + " Graph"))
            elif index == 3:
                self.maincontrol.ui.checkBox4.setText(QString(key + " Graph"))
            elif index == 4:
                self.maincontrol.ui.checkBox5.setText(QString(key + " Graph"))
            elif index == 5:
                self.maincontrol.ui.checkBox6.setText(QString(key + " Graph"))

            if self.graphWidgetsOn[index]:
                data = self.data_manager.getVariableData(key)
                self.graphWidgets[index].setWindowTitle(key)
                self.graphWidgets[index].updateData(data)
                self.graphWidgets[index].render_graph()
            index = index + 1

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Up:
            self.world_view.moveUp(1)
        elif e.key() == Qt.Key_Down:
            self.world_view.moveDown(1)
        elif e.key() == Qt.Key_W:
            self.world_view.moveForward(1)
        elif e.key() == Qt.Key_A:
            self.world_view.moveLeft(1)
        elif e.key() == Qt.Key_S:
            self.world_view.moveBack(1)
        elif e.key() == Qt.Key_D:
            self.world_view.moveRight(1)
        elif e.key() == Qt.Key_Left:
            self.world_view.rotateLeft()
        elif e.key() == Qt.Key_Right:
            self.world_view.rotateRight()
        elif e.key() == Qt.Key_R:
            self.world_view.resetRotation()
        elif e.key() == Qt.Key_Q:
            self.world_view.rotateUp()
        elif e.key() == Qt.Key_E:
            self.world_view.rotateDown()


    def start_server(self):
        try:
            self.recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print('Socket created')
        except socket.error, msg:
            print('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()

        try:
            self.recv_socket.bind(('', self.port))
        except socket.error, msg:
            print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()

        print("Client connected")

        self.isRunning = True
        self.recv_thread = Thread(target=self.run)
        self.recv_thread.daemon = True
        self.recv_thread.start()

    def process_message(self, message):
        if message.msg_type == InsightMsg_pb2.InsightMsg.BATTERY:
            self.data_manager.updateBatteryLevel(message.battery_status.battery_level)
            #self.maincontrol.updateBatterStatus(message.battery_status.battery_level)
        elif message.msg_type == InsightMsg_pb2.InsightMsg.POS:
            self.data_manager.updatePosition(message.position.pos_x, message.position.pos_y, message.position.pos_z)
            self.world_view.updatePosition(message.position.pos_x, message.position.pos_y, message.position.pos_z)
        elif message.msg_type == InsightMsg_pb2.InsightMsg.POSE:
            self.data_manager.updatePose(message.pose.roll, message.pose.pitch, message.pose.yaw)
            self.world_view.updatePose(message.pose.roll, message.pose.pitch, message.pose.yaw)
        elif message.msg_type == InsightMsg_pb2.InsightMsg.DETECTION:
            self.world_view.addDetection(message.detection)
        elif message.msg_type == InsightMsg_pb2.InsightMsg.TEXT:
            print("rcvd Text message")
        elif message.msg_type == InsightMsg_pb2.InsightMsg.VARIABLE:
            self.data_manager.updateVariable(message.var_msg)
        else:
            print("rcvd Unknown message")

    def run(self):
        while self.isRunning:
            totallen = self.recv_socket.recv(4)
            totallenRecv = struct.unpack('>I', totallen)[0]
            messagelen = totallenRecv - 4
            message = self.recv_socket.recv(messagelen)

            rcvd_message = InsightMsg_pb2.InsightMsg()
            rcvd_message.ParseFromString(message)
            self.process_message(rcvd_message)

        self.recv_socket.close()

    def shutdown(self):
        self.isRunning = False
        print("Waiting for thread to die")
        self.recv_thread.join()

        print("Exiting")


def main():
    app = QApplication(sys.argv)
    ex = InsightGUI()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()