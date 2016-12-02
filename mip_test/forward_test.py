import mippy
import time

def main():
    print('Main')
    gt = mippy.GattTool('hci0', '7C:66:9D:A3:AC:AE')
    mip = mippy.Mip(gt)
    mip.setChestLed(1.0, 0.0, 0.0)
    voltage = mip.getBatteryLevel()
    print 'Battery Voltage (4.0v-6.4v): %f' % voltage

    mip.resetOdomemeter()
    distance = mip.getOdometer()

    print('Distance (cm): %f' % distance)

    time.sleep(2)


if __name__ == '__main__':
    main()