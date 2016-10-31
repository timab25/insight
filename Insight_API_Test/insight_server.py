from threading import Thread
import socket
import sys
import InsightMsg_pb2
import struct


class InsightServer:

    isRunning = False
    recv_thread = []

    def __init__(self, port):
        print("init")
        self.port = port

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
            print(rcvd_message.robot_name)

            if rcvd_message.msg_type == InsightMsg_pb2.InsightMsg.BATTERY:
                print("rcvd Battery message")
            elif rcvd_message.msg_type == InsightMsg_pb2.InsightMsg.POS:
                print("rcvd Position message")
            elif rcvd_message.msg_type == InsightMsg_pb2.InsightMsg.POSE:
                print("rcvd Pose message")
            elif rcvd_message.msg_type == InsightMsg_pb2.InsightMsg.DETECTION:
                print("rcvd Detection message")
            elif rcvd_message.msg_type == InsightMsg_pb2.InsightMsg.TEXT:
                print("rcvd Text message")
            elif rcvd_message.msg_type == InsightMsg_pb2.InsightMsg.VARIABLE:
                print("rcvd Variable message")
            else:
                print("rcvd Unknown message")

        self.recv_socket.close()

    def shutdown(self):
        self.isRunning = False
        print("Waiting for thread to die")
        self.recv_thread.join()
        print("Exiting")


def main():
    insight_server = InsightServer(8899)
    raw_input('Press Enter')
    insight_server.shutdown()

if __name__ == "__main__":
    main()