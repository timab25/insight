import RobotPos_pb2
import RobotBatteryStatus_pb2
import RobotDetection_pb2
import RobotPose_pb2
import TextMessage_pb2
import Variable_pb2
import socket
import sys


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
        self.sender_socket.sendto(pos_to_send.SerializeToString(), (self.ip, self.port))


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

    def sendDetection(self, bearing, distance, r=255, g=255, b=255):
        """
        send sensor detection

        This method is used to send a sensor detection from the robot to the Insight GUI

        Args:
            bearing: relative bearing to detection
            distance: distance to detection
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

    def sendTextMessage(self, sender, severity, message, file_name="", line_number=0):
        print("Sending text message: " + sender + ":" + severity + ":" + message)
        print(file_name + ":" + line_number)

        message_to_send = TextMessage_pb2.TextMessage()
        message_to_send.sending_module = sender
        message_to_send.severity_level = severity
        message_to_send.message = message
        message_to_send.file_name = file_name
        message_to_send.line_number = line_number

    def sendVariableDouble(self, class_name, name, value):
        print("Sending double variable: " + class_name + ":" + name + ":" + str(value))
        variable_to_send = Variable_pb2.Variable()
        variable_to_send.class_name = class_name
        variable_to_send.name = name
        variable_to_send.variable_name = Variable_pb2.Variable.DOUBLE
        variable_to_send.double_value = value

    def sendVariableFloat(self, class_name, name, value):
        print("Sending double variable: " + class_name + ":" + name + ":" + str(value))
        variable_to_send = Variable_pb2.Variable()
        variable_to_send.class_name = class_name
        variable_to_send.name = name
        variable_to_send.variable_name = Variable_pb2.Variable.FLOAT
        variable_to_send.float_value = value

    def sendVariableIntSmall(self, class_name, name, value):
        print("Sending double variable: " + class_name + ":" + name + ":" + str(value))
        variable_to_send = Variable_pb2.Variable()
        variable_to_send.class_name = class_name
        variable_to_send.name = name
        variable_to_send.variable_name = Variable_pb2.Variable.INT32
        variable_to_send.int32_value = value

    def sendVariableIntBig(self, class_name, name, value):
        print("Sending double variable: " + class_name + ":" + name + ":" + str(value))
        variable_to_send = Variable_pb2.Variable()
        variable_to_send.class_name = class_name
        variable_to_send.name = name
        variable_to_send.variable_name = Variable_pb2.Variable.INT64
        variable_to_send.int64_value = value

    def sendVariableString(self, class_name, name, value):
        print("Sending double variable: " + class_name + ":" + name + ":" + value)
        variable_to_send = Variable_pb2.Variable()
        variable_to_send.class_name = class_name
        variable_to_send.name = name
        variable_to_send.variable_name = Variable_pb2.Variable.STRING
        variable_to_send.string_value = value

    def close_connection(self):
        self.sender_socket.close()


def main():
    insight_client = InsightClient('127.0.0.1', 8899)
    insight_client.sendPos(1, 1, 1)
    raw_input('Press Enter')

if __name__ == "__main__":
    main()