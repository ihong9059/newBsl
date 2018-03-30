# eMst: 64, eGw: 32,
from datetime import datetime

class Frame:
    Master = 64; ServerReq = 100

    pidOrg = [0,1]; rxtxOrg = [Master,1];
    sensor = [1,1]; micom = [1,1]; gidOrg = [0,2]
    high = [100,1]; low = [1,1]; level = [50,1]; Type = [1,1]; rate = [1,1]
    status = [1,1]; dtime = [1,2]
    cmd = [ServerReq,1]; sub = [1,1]; time = [1,2]
    pid = [1,1]; rxtx = [64,1];  gid = [2,2]; srcGid = [1,2]
    tbd0 = [1,2]; tbd1 = [1,2]; tbd2 = [1,2]; zone = [1,1]; CheckSum = [1,1]
    crc = [1,2]

    pidOrg1 = [0,1]; rxtxOrg1 = [Master,1];
    sensor1 = [1,1]; micom1 = [1,1]; gidOrg1 = [0,2]
    high1 = [100,1]; low1 = [1,1]; level1 = [50,1]; Type1 = [1,1]; rate1 = [1,1]
    status1 = [1,1]; dtime1 = [1,2]
    cmd1 = [ServerReq,1]; sub1 = [1,1]; time1 = [1,2]
    pid1 = [1,1]; rxtx1 = [64,1];  gid1 = [2,2]; srcGid1 = [1,2]
    tbd01 = [1,2]; tbd11 = [1,2]; tbd21 = [1,2]; zone1 = [1,1]; CheckSum1 = [1,1]
    crc1 = [1,2]

    frameList = [ pidOrg, rxtxOrg, sensor, micom, gidOrg,
        high, low, level, Type, rate, status, dtime,
        cmd, sub, time,
        pid, rxtx, gid, srcGid, tbd0, tbd1, tbd2, zone, CheckSum, crc ]

    frameList1 = [ pidOrg1, rxtxOrg1, sensor1, micom1, gidOrg1,
        high1, low1, level1, Type1, rate1, status1, dtime1,
        cmd1, sub1, time1,
        pid1, rxtx1, gid1, srcGid1, tbd01, tbd11, tbd21, zone1, CheckSum1, crc1 ]

    frame = ''
    frame1 = ''
    byteList = []
    byteList1 = []
    # input buffer clear
    clearBuffFlag = False
    newFrameFlag = False

    def setPid(self, vaule):
        self.pid[0] = vaule

    def setRxTx(self, vaule):
        self.rxtx[0] = vaule

    def setGid(self, vaule):
        self.gid[0] = vaule

    def setHigh(self, vaule):
        self.high[0] = vaule

    def setLow(self, vaule):
        self.low[0] = vaule

    def setLevel(self, vaule):
        self.level[0] = vaule

    def setCmd(self, vaule):
        self.cmd[0] = vaule

    def setSub(self, vaule):
        self.sub[0] = vaule

    def getFrame(self):
        return self.frame

    def setCrcFrame(self, frame):
        tempList = []

        for numList in frame:
            if(numList[1]==2):
                tempList.append(numList[0]%256)
                tempList.append(int(numList[0]/256))
            else:
                tempList.append(numList[0])
        tempList = tempList[0:(len(tempList)-2)]
        crcIn = bytearray(tempList)
        crcResult = self.getCrc(crcIn)
        self.crc[0] = crcResult

    def setFrame(self):
        self.setCrcFrame(self.frameList)
        self.frame = '{'
        for numList in self.frameList:
            if(numList[1]==2):
                self.frame += '%02x' % (numList[0]%256)
                self.frame += '%02x' % int(numList[0]/256)
            else:
                self.frame += '%02x' % numList[0]
        self.frame += '}'
        with open('send.txt','a') as fp:
            print(self.frame, file = fp)
        print(self.frame)

    def setReceiveFrame(self):
        dt = datetime.now()
        self.setCrcFrame(self.frameList1)
        self.frame1 = '{'
        for numList in self.frameList1:
            if(numList[1]==2):
                self.frame1 += '%02x' % (numList[0]%256)
                self.frame1 += '%02x' % int(numList[0]/256)
            else:
                self.frame1 += '%02x' % numList[0]
        self.frame1 += '}'
        with open('receive.txt','a') as fp:
            writeStr = 'Receive:: ' + str(dt.date()) + ':' + str(dt.time())
            print(writeStr, file = fp)
            print(self.frame1, file = fp)
        print(self.frame1)

    def getCrc(self, data):
        from crc import CRC
        crc16 = CRC()
        return crc16.update(data)

    def printSubName(self, sub):
        if(sub == 103):
            print('Control Ack')
        elif( sub == 108 ):
            print('GroupChange Ack')
        elif sub == 104:
            print('AutoMode Ack')
        elif sub == 110:
            print('Status Ack')
        elif sub == 101:
            print('PowerRead Ack')
        else:
            print('Sub Commend Error')

    def parseFrame(self, inFrame):
        first = inFrame.rfind('{')
        last = inFrame.rfind('}')
        if last > 150:
            self.clearBuffFlag = True
        else:
            self.clearBuffFlag = False

        if (last - first -1) == 68:
            self.clearBuffFlag = True
            result = inFrame[(first+1):last]

            count = 0
            temp = list(); self.byteList1 = list();
            for s in range(1,35):
                ss = result[count:count+2]
                temp.append(int(ss,16))
                self.byteList1.append(int(ss,16))
                count += 2
            temp = temp[0:(len(temp)-2)]
            crcIn = bytearray(temp)
            crcResult = self.getCrc(crcIn)

            count = 0
            for i in self.frameList1:
                if i[1] == 2:
                    i[0] = self.byteList1[count]
                    count += 1
                    i[0] += self.byteList1[count]*256
                else:
                    i[0] = self.byteList1[count]
                count += 1

            if crcResult == self.crc1[0]:
                print('Crc Ok --> Photo:{} traffic:{} status:{}'.format(self.dtime1[0],
                    (self.high1[0] + self.low1[0]*256), self.rate1[0]))
                self.printSubName(self.sub1[0])
                print('Cmd:{}, Sub:{}'.format(self.cmd1[0], self.sub1[0]))
                print('Power:{}'.format(self.rate1[0]+self.status1[0]*0x100+
                    self.dtime1[0]*0x10000))
                self.newFrameFlag = True
                self.setReceiveFrame()
            else:
                print('Crc error:{},{}'.format(crcResult, self.crc1[0]))
            return True

        else:
            return False

    def testFrame(self):
        print('----------- testFrame --------------')
        strTest = '{000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1fc36a}1234'
        # strTest = '{01010101123464013201010100010101000101010001000100010001000101010001}1234'
        print(strTest.find('}'))
        self.parseFrame(strTest)
        if self.getClearBuff():
            print('clear input buff')
            strTest = ''


if __name__ == '__main__':
    frame = Frame()
    myFrame = frame.getFrame()

    frame.setFrame()
    a = frame.getFrame()
    aa = bytearray(a, 'ascii')
    print(aa)
