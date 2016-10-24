

class InsightClient:

    def __init__(self):
        print("init")

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
        print("Sending pos(x,y): " + x + " " + y)

    def sendBatteryStatus(self, level):
        """
        send battery level of robot to Insight GUI

        This method is used to send the battery/fuel level of the robot to the Insight GUI

        Args:
            level: battery level

        Return:
            no return value
        """
        print("Sending battery status: " + level)

    def sendDetection(self, bearing, distance, r=255, g=255, b=255):
        print("Sending detection: Bearing = " + bearing + "  Distance = " + distance)
