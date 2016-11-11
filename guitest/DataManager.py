

class DataManager:

    def __init__(self):
        self.position = {'x': 0.0, 'y': 0.0, 'z': 0.0}
        self.pose = {'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0}
        self.battery_level = 0.0

    def updatePosition(self, xPos, yPos, zPos):
        self.position['x'] = xPos
        self.position['y'] = yPos
        self.position['z'] = zPos

    def updatePose(self, new_roll, new_pitch, new_yaw):
        self.pose['roll'] = new_roll
        self.pose['pitch'] = new_pitch
        self.pose['yaw'] = new_yaw

    def updateBatteryLevel(self, new_battery):
        self.battery_level = new_battery

    def getPosition(self):
        return self.position['x'], self.position['y'], self.position['z']

    def getPose(self):
        return self.pose['roll'], self.pose['pitch'], self.pose['yaw']

    def getBatteryLevel(self):
        return self.battery_level

