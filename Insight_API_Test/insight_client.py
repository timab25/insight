

class InsightClient:

    def __init__(self):
        print "init"

    def sendPos(self, x, y):
        print "Sending pos(x,y): " + x + " " + y

    def sendBatteryStatus(self, level):
        print "Sending battery status: " + level

    def sendDetection(self, bearing, distance, r=255, g=255, b=255):
        print "Sending detection: Bearing = " + bearing + "  Distance = " + distance
