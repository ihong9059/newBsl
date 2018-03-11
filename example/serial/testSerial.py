import serial
import time
# ser = serial.Serial('/dev/cu.SLAB_USBtoUART',115200,timeout=0)
# ser = serial.Serial('/dev/ttyUSB0',115200,timeout=0)
ser = serial.Serial('/dev/ttyAMA0',115200,timeout=0)
# ser = serial.Serial('COM11',115200,timeout=0)
print(ser.portstr)

from threading import Thread, Lock

hksFlag=False
hksCount=0

class inThread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        global hksCount
        global hksFlag
        global ser
        while True:
            serialInput=str(ser.readline(),'utf-8')
            if serialInput != '':
                print(serialInput)
                hksCount += 1
                if hksCount>10:
                    hksFlag=True
                    break
        print('End of inThread')

class outThread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        global hksFlag
        while True:
            if hksFlag:
                print('received the hksFlag from inThread')
                hksFlag=False
                break
            time.sleep(0.1)
        print('End of inThread')

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
            # ser.write(b'\x5A\x03\x02\x02\x02\x09')
            time.sleep(1)
        print('End of inThread')

def sIn():
    testSer = inThread()
    testSer.start()

if __name__ == "__main__":
    testSer = testThread()
    testSer.start()

# hksIn=inThread()
# hksIn.start()
# hksOut=outThread()
# hksOut.start()
# testSer=testThread()
# testSer=inThread()
# testSer.start()



# import threading
# import time
# import sys
# import serial
# import os
# import time
#
# def Task1(ser):
#
#     while 1:
#
#         print "Inside Thread 1"
#         ser.write('\x5A\x03\x02\x02\x02\x09') # Byte ArrayTo Control a MicroProcessing Unit
#         b = ser.read(7)
#         print b.encode('hex')
#         print "Thread 1 still going on"
#         time.sleep(1)
#
#
# def Task2(ser):
#
#     print "Inside Thread 2"
#     print "I stopped Task 1 to start and execute Thread 2"
#     ser.write('x5A\x03\x02\x08\x02\x0F')
#     c = ser.read(7)
#     print c.encode('hex')
#     print "Thread 2 complete"
#
#
# def Main():
#     ser = serial.Serial(3, 11520)
#     t1 = threading.Thread(target = Task1, args=[ser])
#     t2 = threading.Thread(target = Task2, args=[ser])
#     print "Starting Thread 1"
#     t1.start()
#     print "Starting Thread 2"
#     t2.start()
#
#     print "=== exiting ==="
#
#     ser.close()
#
# if __name__ == '__main__':
#
#     Main()
