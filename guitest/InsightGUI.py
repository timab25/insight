import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pyqtgraph as pg
import numpy as np
from GLWindow import *
from threading import Thread
import socket
import sys
import InsightMsg_pb2
import struct
import DataManager

class InsightGUI(QMainWindow):

    def __init__(self, parent=None):
        super(InsightGUI, self).__init__(parent)

        self.port = 8899
        self.recv_socket = None
        self.isRunning = None
        self.recv_thread = None

        self.data_manager = DataManager()

        print("Starting server")
        self.start_server()

        bar = self.menuBar()
        file = bar.addMenu("File")

        pg.setConfigOptions(antialias=True)

        # win = pg.PlotWidget()  # Automatically generates grids with multiple items
        # x = np.random.normal(size=1000)
        # y = np.random.normal(size=1000)
        # win.plot(x,y)
        # dockWidget = QDockWidget("Test Graph", self)
        # dockWidget.setWidget(win)
        # self.addDockWidget(Qt.DockWidgetArea(1), dockWidget)

        self.world_view = GLWindow()
        self.world_view_dock_widget = QDockWidget("World View", self)
        self.world_view_dock_widget.setWidget(self.world_view)
        self.addDockWidget(Qt.DockWidgetArea(1), self.world_view_dock_widget)

        self.setWindowTitle("Insight GUI")

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
        print("Processing message")
        if message.msg_type == InsightMsg_pb2.InsightMsg.BATTERY:
            print("rcvd Battery message")
            self.data_manager.updateBatteryLevel(message.battery_status.battery_leve)
        elif message.msg_type == InsightMsg_pb2.InsightMsg.POS:
            print("rcvd Position message")
        elif message.msg_type == InsightMsg_pb2.InsightMsg.POSE:
            print("rcvd Pose message")
        elif message.msg_type == InsightMsg_pb2.InsightMsg.DETECTION:
            print("rcvd Detection message")
        elif message.msg_type == InsightMsg_pb2.InsightMsg.TEXT:
            print("rcvd Text message")
        elif message.msg_type == InsightMsg_pb2.InsightMsg.VARIABLE:
            print("rcvd Variable message")
        else:
            print("rcvd Unknown message")

    def run(self):
        while self.isRunning:
            print("recv message")

            totallen = self.recv_socket.recv(4)
            totallenRecv = struct.unpack('>I', totallen)[0]
            print("got size " + str(totallenRecv))
            messagelen = totallenRecv - 4
            message = self.recv_socket.recv(messagelen)

            print("rcvd a message")

            rcvd_message = InsightMsg_pb2.InsightMsg()
            rcvd_message.ParseFromString(message)
            print(rcvd_message)
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