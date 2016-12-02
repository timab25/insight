import mippy
from insight_client import *


def main():
    current_position = [0.0, 0.0]
    debug_client = InsightClient('127.0.0.1', 8899)
    gt = mippy.GattTool('hci0', '7C:66:9D:A3:AC:AE')
    mip = mippy.Mip(gt)
    mip.setChestLed(1.0, 1.0, 1.0)
    debug_client.sendPos(current_position[0], current_position[1], 0)
    debug_client.sendPose(0, 0, 0)
    voltage = mip.getBatteryLevel()
    print 'Battery Voltage (4.0v-6.4v): %f' % voltage
    debug_client.sendBatteryStatus((voltage/6.4)*100)
    debug_client.sendVariableDouble("main", "battery_voltage", voltage)
    raw_input('Press Enter to send next\n')

    mip.resetOdomemeter()
    distance = mip.getOdometer()
    print('Distance (cm): %f' % distance)

    mip.continuousDriveForwardUntilRadar(15)

    distance = mip.getOdometer()
    print('Distance (cm): %f' % distance)

    current_position[0] += distance
    debug_client.sendPos(current_position[0], current_position[1], 0)

    radar_response = mip.getRadarResponse()
    print('Radar: %d' % radar_response)

    if radar_response == 2:
        debug_client.sendDetection(0, 30, current_position[0], current_position[1], 255, 255, 255)
        mip.setChestLed(1.0, 0.0, 0.0)
    elif radar_response == 3:
        debug_client.sendDetection(0, 10, current_position[0], current_position[1], 255, 255, 255)
        mip.setChestLed(0.0, 0.0, 1.0)
    else:
        mip.setChestLed(0.0, 1.0, 0.0)

    time.sleep(2)

if __name__ == '__main__':
    main()

