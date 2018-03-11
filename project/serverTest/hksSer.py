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
class serVar:
    serFirstFlag = True
    serAlive = False
    writeFlag = False
    readFlag = False
    readStr = ''
    writeStr = ''

myVar = serVar()

class serThread(Thread):
    myVar = serVar()
    serFrame = Frame()

    serFirstFlag = True
    serAlive = False
    writeFlag = False
    readFlag = False
    readStr = ''
    writeStr = ''

    def __init__(self):
        print('Now Start SerialThread')
        Thread.__init__(self)

    def send(self, writeStr):
        self.writeStr = writeStr
        self.writeFlag = True
        myVar.writeFlag = True

    def getReadFlag(self):
        return self.readFlag

    def clearReadFlag(self):
        self.readFlag = False

    def getReadStr(self):
        return self.readStr

    def clearWriteFlag(self):
        self.writeFlag = False

    def getWriteFlag(self):
        return self.writeFlag

    def getWriteStr(self):
        return self.writeStr

    def getSerAlive(self):
        return self.serAlive

    def FileSave(self,filename,content):
        import io
        with open(filename, "a+") as myfile:
            myfile.write(content)

    def run(self):
        port = 'COM12'
        # port = 'COM38'
        # port = 'COM62'
        count = 0
        with serial.Serial(port, 115200, timeout = 0) as ser:
            print('serial Port:{}'.format(port))
            self.serDevice = ser
            self.serAlive = True
            count = 0
            while True:
                time.sleep(0.001)
                try:
                    self.readStr=str(ser.readline(),'utf-8')
                    if self.readStr != '':
                        self.readFlag = True
                        self.myVar.readFlag = True
                except:
                    print('Error Data')

                if self.readFlag:
                    count += 1
                    self.serFrame.parseFrame(self.readStr)

                    print(self.readStr, sep = '')
                    self.readFlag = False
                    if self.readStr.find('Quit Serial') != -1:
                        break

                if self.writeFlag:
                    ser.write(bytearray(self.writeStr,'ascii'))
                    self.writeFlag = False
                    self.myVar.writeFlag = False

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

class testThread1(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        while True:
            pass
        print('End of testThread')

if __name__ == "__main__":

    testSer = testThread()
    testSer.start()
