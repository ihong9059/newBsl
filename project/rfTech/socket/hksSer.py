import serial
import time
from threading import Thread, Lock

# ser = serial.Serial('/dev/cu.SLAB_USBtoUART',115200,timeout=0)
# ser = serial.Serial('/dev/ttyUSB0',115200,timeout=0)
# ser = serial.Serial('/dev/ttyAMA0',115200,timeout=0)
serialName = 'COM62'
ser = serial.Serial(serialName, 115200, timeout=0)
print('serial port is {}'.format(ser.portstr))

hksFlag=False
hksCount=0

class readThread(Thread):
    inFlag = False
    inStr = ''

    def __init__(self):
        print('Now Start readThread')
        Thread.__init__(self)

    def run(self):
        global ser
        while True:
            self.inStr=str(ser.readline(),'utf-8')
            if serialInput != '':
                self.inFlag = True
                print(serialInput)
                hksCount += 1
                if hksCount>10:
                    hksFlag=True
                    break
        print('End of inThread')

class writeSer():
    pass

class testThread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        count=10
        while count:
            count -= 1
            testStr = 'Count = {}\n\r'.format(count)
            arr = bytearray(testStr,'ascii')
            ser.write(arr)
            time.sleep(1)
        print('End of inThread')

def sIn():
    print('This is sIn')
    testSer = readThread()
    testSer.start()

if __name__ == "__main__":
    sIn()

    testSer = testThread()
    testSer.start()
