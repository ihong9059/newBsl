import socketserver
import time
from hksSer import serThread
from datetime import datetime
from frame import Frame

mySer = serThread()

# tcpCount = 0
class MyTCPHandler(socketserver.BaseRequestHandler):
    myFrame = Frame()

    def FileSave(self,filename,content):
        import io
        with open(filename, "a+") as myfile:
            myfile.write(content)

    def handle(self):
        dt = datetime.now()
        # self.request is the TCP socket connected to the client
        print('------------------ server Start ----------------------')
        self.data = self.request.recv(1024).strip()
        testStr = "{} wrote: when {}:{} \n".format(self.client_address[0],
        dt.date(), dt.time())
        testStr += str(self.data,'utf-8') + '\n'
        print(testStr)
        self.FileSave('LanReceive.txt', 'From Server:'+testStr+'\n')
        mySer.send(str(self.data,'utf-8'))

        end = True
        next = time.time() + 1
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
        self.FileSave('LanSend.txt', 'From Gateway:'+testStr+'\n')

        sendStr = bytearray(self.data.upper(),'utf-8')
        self.request.sendall(sendStr)
        print('return:'+str(sendStr))
        print('------------------ server End ----------------------')
        self.data = self.request.recv(1024).strip()

if __name__ == "__main__":
    # HOST, PORT = "locallhost", 40007
    # HOST, PORT = "192.166.0.3", 40007
    HOST, PORT = "192.166.0.8", 40007
    # HOST, PORT = "192.166.0.3", 40007
    # HOST, PORT = "192.168.40.3", 40007
    # HOST, PORT = "192.168.185.11", 40007
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    mySer.start()
    print('Activate the server; this will keep running until you')
    print('interrupt the program with Ctrl-C')
    server.serve_forever()
