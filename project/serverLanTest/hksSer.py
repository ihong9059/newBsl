import serial
import time
from threading import Thread, Lock
from frame import Frame

class serThread(Thread):
    serFrame = Frame()

    serFirstFlag = True
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
        # print('ser write')

    def FileSave(self,filename,content):
        import io
        with open(filename, "a+") as myfile:
            myfile.write(content)

    def run(self):
        # port = '/dev/ttyS0'
        # port = '/dev/ttyUSB0'
        # port = 'COM5'
        port = 'COM7'
        count = 0
        with serial.Serial(port, 115200, timeout = 0) as ser:
            print('serial Port:{}'.format(port))
            self.serDevice = ser
            while True:
                try:
                    time.sleep(0.001)
                    bytesToRead = ser.inWaiting()
                    if bytesToRead:
                        sTemp = str(ser.read(bytesToRead),'utf-8')
                        self.readStr += sTemp;
                        if self.readStr.find('}') != -1:
                            if self.serFrame.parseFrame(self.readStr):
                                self.returnFrame =  self.serFrame.frame1
                                self.readStr = ''
                                self.newFrameFlag = True
                        self.readFlag = True

                        if self.readStr.rfind('\n') != -1:
                            indexStr = self.readStr.rfind('\n')
                            print(self.readStr[:indexStr], end = '')
                            self.readStr = self.readStr[indexStr:]
                except:
                    print('Ser except')

                if self.writeFlag:
                    ser.write(bytearray(self.writeStr,'utf-8'))
                    self.writeFlag = False

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
