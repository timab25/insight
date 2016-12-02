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

        bar = self.menuBar()
        self.variables_menu = bar.addMenu("Variables")

        self.dockWidget = VariableGraphWidget("Test")
        self.addDockWidget(Qt.DockWidgetArea(1), self.dockWidget)

        self.world_view = GLWindow()
        self.world_view_dock_widget = QDockWidget("World View", self)
        self.world_view_dock_widget.setWidget(self.world_view)
        self.addDockWidget(Qt.DockWidgetArea(1), self.world_view_dock_widget)
        self.setWindowTitle("Insight GUI")

        self.maincontrol = MainControlWidget.MainControlWidget()
        self.maincontrol.show()

        QObject.connect(self.world_view, SIGNAL('render'), self.render_graph)

    def render_graph(self):
        self.dockWidget.render_graph()

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
            self.maincontrol.updateVar1("robot x", message.position.pos_x)
            self.maincontrol.updateVar2("robot z", message.position.pos_z)
        elif message.msg_type == InsightMsg_pb2.InsightMsg.POSE:
            self.data_manager.updatePose(message.pose.roll, message.pose.pitch, message.pose.yaw)
            self.world_view.updatePose(message.pose.roll, message.pose.pitch, message.pose.yaw)
        elif message.msg_type == InsightMsg_pb2.InsightMsg.DETECTION:
            self.world_view.addDetection(message.detection)
        elif message.msg_type == InsightMsg_pb2.InsightMsg.TEXT:
            print("rcvd Text message")
        elif message.msg_type == InsightMsg_pb2.InsightMsg.VARIABLE:
            self.data_manager.updateVariable(message.var_msg)
            self.dockWidget.updateData(self.data_manager.getVariableData('test_var'))
            keys = self.data_manager.getNewKeys()
            for k in keys:
                self.variables_menu.addAction(k)
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