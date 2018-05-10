import time
from hksSer import serThread
from datetime import datetime
from frame import Frame
from threading import Thread, Lock

mySer = serThread()

class mainThread(Thread):
    myFrame = Frame()

    def FileSave(self,filename,content):
        import io
        with open(filename, "a+") as myfile:
            myfile.write(content)

    def __init__(self):
        print('Now Start mainThread')
        Thread.__init__(self)

    def setSerFrame(self):
        self.myFrame.rate[0] = 1; self.myFrame.status[0] = 0;
        self.myFrame.Type[0] = 1;
        self.myFrame.level[0] = 0;
        self.myFrame.micom[0] = 0;
        self.myFrame.rxtx[0] = 1; self.myFrame.sub[0] = 1
        self.myFrame.gid[0] = 1; self.myFrame.pid[0] = 1;
        self.myFrame.setFrame()
        print('------------ Frame End ----------------')
        # bslCtrClient.sendSocket(myFrame.getFrame())

    def run(self):
        print('------------------ server Start ----------------------')
        dt = datetime.now()
        nowSecond = dt.second + 1
        end = True
        count = 0
        while end:
            time.sleep(0.001)
            try:
                if count > 10:
                    end = False
                if datetime.now().second == (nowSecond%60):
                    nowSecond = datetime.now().second + 10
                    count += 1
                    print('{}:{}'.format(count,dt.now().isoformat(sep = '/', timespec='seconds')))
                    self.setSerFrame()
                    print('setSerFrame')
                    mySer.send(self.myFrame.getFrame())

                    endSer = True
                    countSer = 3
                    next = time.time() + 2

                    while endSer and countSer:
                        time.sleep(0.001)
                        if next < time.time() or mySer.newFrameFlag :
                            countSer -= 1
                            next = time.time() + 2
                            if mySer.newFrameFlag:
                                print('from GW:'+mySer.returnFrame)
                                self.data = mySer.returnFrame
                                mySer.newFrameFlag = False
                                print('-----------Received return Frame, goto next')
                                endSer = False
                            else:
                                self.data = "{No received return data from Gateway}"
                                mySer.send(self.myFrame.getFrame())
                                print(self.data)
            except:
                print('key exception')
                end = False

        mySer.serRun = False
        print('------------------ server End ----------------------')
        # self.data = self.request.recv(1024).strip()
if __name__ == "__main__":
    mySer.start()

    myMain = mainThread()
    myMain.start()
