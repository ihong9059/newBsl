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
        # pass

    def __init__(self):
        print('Now Start mainThread')
        Thread.__init__(self)
# edServerReq=100, edClientAck, edClientReq,
# edsCmd_Status=110
    def setSerFrame(self):
        self.myFrame.rate[0] = 1; self.myFrame.status[0] = 0;
        self.myFrame.Type[0] = 1;
        self.myFrame.level[0] = 0;
        self.myFrame.micom[0] = 0;  # communication Type0
        self.myFrame.rxtx[0] = 1; self.myFrame.sub[0] = 110; # edsCmd_Status=110
        self.myFrame.gid[0] = 101; self.myFrame.pid[0] = 101;
        self.myFrame.setFrame()
        print('------------ Frame End ----------------')
        # bslCtrClient.sendSocket(myFrame.getFrame())

    def run(self):
        print('------------------ server Start ----------------------')
        dt = datetime.now()
        nowSecond = dt.second + 1
        end = True
        count = 0
        num = 0
        while end:
            time.sleep(0.001)
            try:
                if count > 10:
                    pass
                    # end = False
                # if dt.second == (nowSecond%60):
                if datetime.now().second == (nowSecond%60):
                    nowSecond = datetime.now().second + 10
                    count += 1
                    # print('{}:{}'.format(count,datetime.now()))
                    print('{}:{}'.format(count,datetime.now()))
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
                            num += 1
                            if mySer.newFrameFlag:
                                print('from GW:'+mySer.returnFrame)
                                self.data = mySer.returnFrame
                                mySer.newFrameFlag = False
                                print('-----------Received return Frame, goto next')
                                endSer = False
                                result ='{},{}'.format(num, datetime.now())
                                result += ', Photo ={}\n'.format(self.myFrame.dtime1[0])
                            else:
                                self.data = "{No received return data from Gateway}\n"
                                mySer.send(self.myFrame.getFrame())
                                result = self.data
                            print(result)
                            self.FileSave('photo.txt', result)
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
