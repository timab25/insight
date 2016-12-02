import RobotPos_pb2
import RobotBatteryStatus_pb2
import RobotDetection_pb2
import RobotPose_pb2
import TextMessage_pb2
import Variable_pb2
import InsightMsg_pb2
import socket
import sys
import struct
import time
import math

class InsightClient:

    def __init__(self, ip, port):
        """
        initialize InsightClient

        initialize the InsightClient and connection to the server

        Args:
            ip: ip address of InsightServer
            port: port of InsightServer

        Returns:
            no return value
        """
        print("init")
        try:
            self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.ip = ip
            self.port = port
            self.sender_socket.connect((ip, port))
        except socket.error:
            print('Failed to create socket')
            sys.exit()

    def sendPos(self, x, y, z):
        """
        send robot position to Insight GUI

        This method is used to send the 3D position of the robot to the Insight GUI.  Units are based of what the GUI is setup for

        Args:
            x: x position of robot
            y: y position of robot
            z: z position of robot

        Returns:
            no return value
        """
        print("Sending pos(x,y): " + str(x) + " " + str(y))
        pos_to_send = RobotPos_pb2.RobotPos()
        pos_to_send.pos_x = x
        pos_to_send.pos_y = y
        pos_to_send.pos_z = z

        insight_msg_to_send = InsightMsg_pb2.InsightMsg()
        insight_msg_to_send.robot_name = "Test"
        insight_msg_to_send.msg_type = InsightMsg_pb2.InsightMsg.POS
        insight_msg_to_send.position.CopyFrom(pos_to_send)

        s = insight_msg_to_send.SerializeToString()

        totallen = 4 + len(s)
        print("Sending: " + str(totallen))
        pack1 = struct.pack('>I', totallen)  # the first part of the message is length
        print(insight_msg_to_send)

        self.sender_socket.sendall(pack1)
        self.sender_socket.sendall(s)


    def sendBatteryStatus(self, level):
        """
        send battery level of robot to Insight GUI

        This method is used to send the battery/fuel level of the robot to the Insight GUI

        Args:
            level: battery level

        Return:
            no return value
        """
        print("Sending battery status: " + str(level))
        battery_status = RobotBatteryStatus_pb2.RobotBatteryStatus()
        battery_status.battery_level = level

        insight_msg_to_send = InsightMsg_pb2.InsightMsg()
        insight_msg_to_send.robot_name = "Test"
        insight_msg_to_send.msg_type = InsightMsg_pb2.InsightMsg.BATTERY
        insight_msg_to_send.battery_status.CopyFrom(battery_status)

        s = insight_msg_to_send.SerializeToString()

        totallen = 4 + len(s)
        print("Sending: " + str(totallen))
        pack1 = struct.pack('>I', totallen)  # the first part of the message is length
        print(insight_msg_to_send)

        self.sender_socket.sendall(pack1)
        self.sender_socket.sendall(s)

    def sendDetection(self, bearing, distance, robot_x, robot_y, r=255, g=255, b=255):
        """
        send sensor detection

        This method is used to send a sensor detection from the robot to the Insight GUI

        Args:
            bearing: relative bearing to detection
            distance: distance to detection
            robot_x: x position of robot
            robot_y: y position of robot
            r: red color value
            g: green color value
            b: blue color value

        Return:
            no return value
        """
        print("Sending detection: Bearing = " + str(bearing) + "  Distance = " + str(distance))
        detection = RobotDetection_pb2.RobotDetection()
        detection.bearing = bearing
        detection.range = distance
        detection.red = r
        detection.green = g
        detection.blue = b
        detection.robot_x = robot_x
        detection.robot_y = robot_y

        insight_msg_to_send = InsightMsg_pb2.InsightMsg()
        insight_msg_to_send.robot_name = "Test"
        insight_msg_to_send.msg_type = InsightMsg_pb2.InsightMsg.DETECTION
        insight_msg_to_send.detection.CopyFrom(detection)

        s = insight_msg_to_send.SerializeToString()

        totallen = 4 + len(s)
        print("Sending: " + str(totallen))
        pack1 = struct.pack('>I', totallen)  # the first part of the message is length
        print(insight_msg_to_send)

        self.sender_socket.sendall(pack1)
        self.sender_socket.sendall(s)

    def sendPose(self, roll, pitch, yaw):
        """
        send pose of the robot

        This method is used to send the pose of the robot to the Insight GUI

        Args:
            roll: roll of the robot
            pitch: pitch of the robot
            yaw: yaw of the robot

        Return:
            no return value
        """
        print("Sending pose: roll=" + str(roll) + "  pitch=" + str(pitch) + "  yaw=" + str(yaw))
        pose_report = RobotPose_pb2.RobotPose()
        pose_report.roll = roll
        pose_report.pitch = pitch
        pose_report.yaw = yaw

        insight_msg_to_send = InsightMsg_pb2.InsightMsg()
        insight_msg_to_send.robot_name = "Test"
        insight_msg_to_send.msg_type = InsightMsg_pb2.InsightMsg.POSE
        insight_msg_to_send.pose.CopyFrom(pose_report)

        s = insight_msg_to_send.SerializeToString()

        totallen = 4 + len(s)
        print("Sending: " + str(totallen))
        pack1 = struct.pack('>I', totallen)  # the first part of the message is length
        print(insight_msg_to_send)

        self.sender_socket.sendall(pack1)
        self.sender_socket.sendall(s)

    def sendTextMessage(self, sender, severity, message, file_name="", line_number=0):
        """
        send text message from the robot

        This method is used to send a text message from the robot to the Insight GUI

        Args:
            sender: name of the sending module
            severity: DEBUG, INFO, ERROR, WARNING
            message: message body
            file_name: filename the message is being sent from
            line_number: line number the message is being sent from

        Return:
            no return value
        """
        print("Sending text message: " + sender + ":" + severity + ":" + message)
        print(file_name + ":" + str(line_number))

        message_to_send = TextMessage_pb2.TextMessage()
        message_to_send.sending_module = sender
        message_to_send.severity_level = severity
        message_to_send.message = message
        message_to_send.file_name = file_name
        message_to_send.line_number = line_number

        insight_msg_to_send = InsightMsg_pb2.InsightMsg()
        insight_msg_to_send.robot_name = "Test"
        insight_msg_to_send.msg_type = InsightMsg_pb2.InsightMsg.TEXT
        insight_msg_to_send.txt_msg.CopyFrom(message_to_send)

        s = insight_msg_to_send.SerializeToString()

        totallen = 4 + len(s)
        print("Sending: " + str(totallen))
        pack1 = struct.pack('>I', totallen)  # the first part of the message is length
        print(insight_msg_to_send)

        self.sender_socket.sendall(pack1)
        self.sender_socket.sendall(s)

    def sendVariableDouble(self, class_name, name, value):
        """
        send a double variable

        This method is used to send a double variable from the robot to the Insight GUI

        Args:
            class_name: name of class containing the variable
            name: name of the variable
            value: value of the variable

        Return:
            no return value
        """
        print("Sending double variable: " + class_name + ":" + name + ":" + str(value))
        variable_to_send = Variable_pb2.Variable()
        variable_to_send.class_name = class_name
        variable_to_send.variable_type = Variable_pb2.Variable.DOUBLE
        variable_to_send.variable_name = name
        variable_to_send.double_value = value

        insight_msg_to_send = InsightMsg_pb2.InsightMsg()
        insight_msg_to_send.robot_name = "Test"
        insight_msg_to_send.msg_type = InsightMsg_pb2.InsightMsg.VARIABLE
        insight_msg_to_send.var_msg.CopyFrom(variable_to_send)

        s = insight_msg_to_send.SerializeToString()

        totallen = 4 + len(s)
        print("Sending: " + str(totallen))
        pack1 = struct.pack('>I', totallen)  # the first part of the message is length
        print(insight_msg_to_send)

        self.sender_socket.sendall(pack1)
        self.sender_socket.sendall(s)

    def sendVariableFloat(self, class_name, name, value):
        """
        send a float variable

        This method is used to send a float variable from the robot to the Insight GUI

        Args:
            class_name: name of class containing the variable
            name: name of the variable
            value: value of the variable

        Return:
            no return value
        """
        print("Sending float variable: " + class_name + ":" + name + ":" + str(value))
        variable_to_send = Variable_pb2.Variable()
        variable_to_send.class_name = class_name
        variable_to_send.variable_type = Variable_pb2.Variable.FLOAT
        variable_to_send.variable_name = name
        variable_to_send.float_value = value

        insight_msg_to_send = InsightMsg_pb2.InsightMsg()
        insight_msg_to_send.robot_name = "Test"
        insight_msg_to_send.msg_type = InsightMsg_pb2.InsightMsg.VARIABLE
        insight_msg_to_send.var_msg.CopyFrom(variable_to_send)

        s = insight_msg_to_send.SerializeToString()

        totallen = 4 + len(s)
        print("Sending: " + str(totallen))
        pack1 = struct.pack('>I', totallen)  # the first part of the message is length
        print(insight_msg_to_send)

        self.sender_socket.sendall(pack1)
        self.sender_socket.sendall(s)

    def sendVariableInt32(self, class_name, name, value):
        """
        send a int32 variable

        This method is used to send a int32 variable from the robot to the Insight GUI

        Args:
            class_name: name of class containing the variable
            name: name of the variable
            value: value of the variable

        Return:
            no return value
        """
        print("Sending int32 variable: " + class_name + ":" + name + ":" + str(value))
        variable_to_send = Variable_pb2.Variable()
        variable_to_send.class_name = class_name
        variable_to_send.variable_name = name
        variable_to_send.variable_type = Variable_pb2.Variable.INT32
        variable_to_send.int32_value = value

        insight_msg_to_send = InsightMsg_pb2.InsightMsg()
        insight_msg_to_send.robot_name = "Test"
        insight_msg_to_send.msg_type = InsightMsg_pb2.InsightMsg.VARIABLE
        insight_msg_to_send.var_msg.CopyFrom(variable_to_send)

        s = insight_msg_to_send.SerializeToString()

        totallen = 4 + len(s)
        print("Sending: " + str(totallen))
        pack1 = struct.pack('>I', totallen)  # the first part of the message is length
        print(insight_msg_to_send)

        self.sender_socket.sendall(pack1)
        self.sender_socket.sendall(s)

    def sendVariableInt64(self, class_name, name, value):
        """
        send a int64 variable

        This method is used to send a int64 variable from the robot to the Insight GUI

        Args:
            class_name: name of class containing the variable
            name: name of the variable
            value: value of the variable

        Return:
            no return value
        """
        print("Sending double variable: " + class_name + ":" + name + ":" + str(value))
        variable_to_send = Variable_pb2.Variable()
        variable_to_send.class_name = class_name
        variable_to_send.variable_name = name
        variable_to_send.variable_type = Variable_pb2.Variable.INT64
        variable_to_send.int64_value = value

        insight_msg_to_send = InsightMsg_pb2.InsightMsg()
        insight_msg_to_send.robot_name = "Test"
        insight_msg_to_send.msg_type = InsightMsg_pb2.InsightMsg.VARIABLE
        insight_msg_to_send.var_msg.CopyFrom(variable_to_send)

        s = insight_msg_to_send.SerializeToString()

        totallen = 4 + len(s)
        print("Sending: " + str(totallen))
        pack1 = struct.pack('>I', totallen)  # the first part of the message is length
        print(insight_msg_to_send)

        self.sender_socket.sendall(pack1)
        self.sender_socket.sendall(s)

    def sendVariableString(self, class_name, name, value):
        """
        send a string variable

        This method is used to send a string variable from the robot to the Insight GUI

        Args:
            class_name: name of class containing the variable
            name: name of the variable
            value: value of the variable

        Return:
            no return value
        """
        print("Sending double variable: " + class_name + ":" + name + ":" + value)
        variable_to_send = Variable_pb2.Variable()
        variable_to_send.class_name = class_name
        variable_to_send.variable_name = name
        variable_to_send.variable_type = Variable_pb2.Variable.STRING
        variable_to_send.string_value = value

        insight_msg_to_send = InsightMsg_pb2.InsightMsg()
        insight_msg_to_send.robot_name = "Test"
        insight_msg_to_send.msg_type = InsightMsg_pb2.InsightMsg.VARIABLE
        insight_msg_to_send.var_msg.CopyFrom(variable_to_send)

        s = insight_msg_to_send.SerializeToString()

        totallen = 4 + len(s)
        print("Sending: " + str(totallen))
        pack1 = struct.pack('>I', totallen)  # the first part of the message is length
        print(insight_msg_to_send)

        self.sender_socket.sendall(pack1)
        self.sender_socket.sendall(s)

    def close_connection(self):
        """
        close the socket connection

        This method is used to shutdown the socket connection

        Return:
            no return value
        """
        self.sender_socket.close()


def main():
    insight_client = InsightClient('127.0.0.1', 8899)

    raw_input('Press Enter to send next\n')

    time.sleep(3)
    #insight_client.sendBatteryStatus(100)
    insight_client.sendPos(0, 0, 0)
    time.sleep(1)
    insight_client.sendPos(0, 0, 1)
    time.sleep(1)
    insight_client.sendPos(0, 0, 2)
    time.sleep(1)
    insight_client.sendPos(0, 0, 3)
    time.sleep(1)
    insight_client.sendPos(0, 0, 4)
    time.sleep(1)

    insight_client.sendDetection(5, 5, 0, 0, 1, 1, 1)
    insight_client.sendDetection(10, 5, 0, 0, 1, 1, 1)
    insight_client.sendDetection(15, 5, 0, 0, 1, 1, 1)
    insight_client.sendDetection(20, 5, 0, 0, 1, 1, 1)
    insight_client.sendDetection(25, 5, 0, 0, 1, 1, 1)
    insight_client.sendDetection(30, 5, 0, 0, 1, 1, 1)

    for x in range(0, 360, 10):
        insight_client.sendVariableFloat("test_class", "test_var", math.sin(math.radians(x)))
        time.sleep(1)
        insight_client.sendPos((x/100.0)*-1, 0, 4+(x/100.0))
        time.sleep(1)

    # insight_client.sendBatteryStatus(95)
    # raw_input('Press Enter to send next\n')
    #
    # insight_client.sendDetection(150, 65, 0, 125, 230)
    # raw_input('Press Enter to send next\n')
    #
    # insight_client.sendPose(45, 25, 270)
    # raw_input('Press Enter to send next\n')
    #
    # insight_client.sendTextMessage("test_prog", "DEBUG", "this is a test", "test.cpp", 60)
    # raw_input('Press Enter to send next\n')
    #
    # insight_client.sendVariableDouble("test_class", "double_var", 12.34)
    # raw_input('Press Enter to send next\n')
    #
    # insight_client.sendVariableFloat("test_class", "float_var", 54.56)
    # raw_input('Press Enter to send next\n')
    #
    # insight_client.sendVariableInt32("test_class", "int32_var", 123456)
    # raw_input('Press Enter to send next\n')
    #
    # insight_client.sendVariableInt64("test_class", "int64_var", 987654321)
    # raw_input('Press Enter to send next\n')
    #
    # insight_client.sendVariableString("test_class", "string_var", "test_string")
    # raw_input('Press Enter to send next\n')


if __name__ == "__main__":
    main()