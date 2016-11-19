import Variable_pb2

class DataManager():

    def __init__(self):
        self.position = {'x': 0.0, 'y': 0.0, 'z': 0.0}
        self.pose = {'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0}
        self.battery_level = 0.0
        self.variable_values = dict()
        self.new_vars = []

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

    def updateVariable(self, variable_update):
        if variable_update.variable_type == Variable_pb2.Variable.FLOAT:
            if variable_update.variable_name in self.variable_values:
                self.variable_values[variable_update.variable_name].append(variable_update.float_value)
            else:
                self.variable_values[variable_update.variable_name] = []
                self.variable_values[variable_update.variable_name].append(variable_update.float_value)
                self.new_vars.append(variable_update.variable_name)

    def getVariableData(self, name):
        return self.variable_values[name]

    def getPosition(self):
        return self.position['x'], self.position['y'], self.position['z']

    def getPose(self):
        return self.pose['roll'], self.pose['pitch'], self.pose['yaw']

    def getBatteryLevel(self):
        return self.battery_level

    def getVariableKeys(self):
        return self.variable_values.keys()

    def getNewKeys(self):
        new_stuff = self.new_vars
        self.new_vars = []
        return new_stuff

