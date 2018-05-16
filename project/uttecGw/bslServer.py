import socketserver
import time
from hksSer import serThread
from datetime import datetime
from frame import Frame

# port = '/dev/ttyS0'
# port = '/dev/ttyUSB0'
ttyS0 = serThread('COM7')
rs485Ser = serThread('COM30')
class MyTCPHandler(socketserver.BaseRequestHandler):
    myFrame = Frame()

    def FileSave(self,filename,content):
        import io
        with open(filename, "a+") as myfile:
            myfile.write(content)
    def procSerial(self, port):
        if port == 0:
            ser = mySer

    def handle(self):
        dt = datetime.now()
        # self.request is the TCP socket connected to the client
        print('Rasp-->------------------ server Start ----------------------')
        self.data = self.request.recv(1024).strip()
        self.myFrame.parseFrame(str(self.data,'utf-8'))
        print('Rasp-->Network Type:{}'.format(self.myFrame.micom1[0]))

        testStr = "Rasp-->{} wrote: when {}:{} \n".format(self.client_address[0],
        dt.date(), dt.time())
        testStr += str(self.data,'utf-8') + '\n'
        print(testStr)
        
        type = self.myFrame.micom1[0]
        if (type == 0) || (type == 1) ||(type == 2):
            mySer=ttyS0; print('Type0,1,2')
        else:
            mySer=rs485Ser; print('Tpye3,4')

        mySer.send(str(self.data,'utf-8'))
        end = True
        next = time.time() + 2
        while end:
            time.sleep(0.001)
            if next < time.time() or mySer.newFrameFlag :
                end = False
                if mySer.newFrameFlag:
                    print('from GW:'+mySer.returnFrame)
                    self.data = mySer.returnFrame
                    mySer.newFrameFlag = False
                else:
                    self.data = "{No received return data from Gateway}"

        testStr = "{} return: when {}:{} \n".format(self.client_address[0],
        dt.date(), dt.time())
        testStr += self.data + '\n'

        sendStr = bytearray(self.data.upper(),'utf-8')
        self.request.sendall(sendStr)
        print('Rasp-->' + self.data)
        print('Rasp-->------------------ server End ----------------------')
        # self.data = self.request.recv(1024).strip()

def runServer():
    HOST, PORT = "0.0.0.0", 40007
    # HOST, PORT = "192.166.0.3", 40007
    # HOST, PORT = "192.168.40.3", 40007
    # HOST, PORT = "192.168.185.11", 40007
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    ttyS0.start()
    rs485Ser.start()

    print('UTTEC Gateway Server::: interrupt the program with Ctrl-C')
    try:
        server.serve_forever()
    except:
        print('End of bslServer')
        ttyS0.runSerial = False
        rs485Ser.runSerial = False
        print('mySer.runSerial = False')

if __name__ == "__main__":
    runServer()
