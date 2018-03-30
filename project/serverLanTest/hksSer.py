import serial
import time
from threading import Thread, Lock
from frame import Frame


# ser = serial.Serial('/dev/cu.SLAB_USBtoUART',115200,timeout=0)
# ser = serial.Serial('/dev/ttyUSB0',115200,timeout=0)
# ser = serial.Serial('/dev/ttyAMA0',115200,timeout=0)
# serialName = 'COM62'
# ser = serial.Serial(serialName, 115200, timeout=0)
# print('serial port is {}'.format(ser.portstr))

class serThread(Thread):
    serFrame = Frame()

    serFirstFlag = True
    serAlive = False
    writeFlag = False
    readFlag = False
    readStr = ''
    writeStr = ''
    newFrameFlag = False
    returnFrame = ''

    def __init__(self):
        print('Now Start SerialThread')
        Thread.__init__(self)

    def send(self, writeStr):
        self.writeStr = writeStr
        self.writeFlag = True
        print('ser write')

    def FileSave(self,filename,content):
        import io
        with open(filename, "a+") as myfile:
            myfile.write(content)

    def run(self):
        # port = '/dev/ttyS0'
        port = 'COM7'
        count = 0
        with serial.Serial(port, 115200, timeout = 0) as ser:
            print('serial Port:{}'.format(port))
            self.serDevice = ser
            self.serAlive = True
            count = 0
            while True:
                time.sleep(0.001)
                try:
                    bytesToRead = ser.inWaiting()
                    if bytesToRead:
                        sTemp = str(ser.read(bytesToRead),'utf-8')
                        self.readStr += sTemp;
                        if bytesToRead == 1:
                            print(sTemp)
                        if self.readStr.find('}') != -1:
                            if self.serFrame.parseFrame(self.readStr):
                                self.returnFrame =  self.serFrame.frame1
                                self.readStr = ''
                                self.newFrameFlag = True
                        self.readFlag = True
                except:
                    print('Error Data')

                if self.writeFlag:
                    ser.write(bytearray(self.writeStr,'utf-8'))
                    self.writeFlag = False

        self.serAlive = False
        # self.serFirstFlag = True
        print('End of inThread')

class testThread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        while True:
            pass
        print('End of testThread')

if __name__ == "__main__":

    testSer = testThread()
    testSer.start()
