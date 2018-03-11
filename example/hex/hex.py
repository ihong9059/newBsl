class Frame:
    pid = [1,1]; rxtx = [1,1]; sensor = [1,1]; micom = [1,1]; gid = [1,2];
    high = [100,1]; low = [1,1]; level = [50,1]; Type = [1,1]; rate = [1,1]
    status = [1,1]; dtime = [1,2]
    cmd = [1,1]; sub = [1,1]; time = [1,2]
    srcPid = [1,1]; dstPid = [1,1]; srcGid = [1,2]; dstGid = [1,2]
    tbd0 = [1,2]; tbd1 = [1,2]; tbd2 = [1,2]; zone = [1,1]; CheckSum = [1,1]
    crc = [1,2]
    frame = [ pid, rxtx, sensor, micom, gid,
        high, low, level, Type, rate, status, dtime,
        cmd, sub, time,
        srcPid, dstPid, srcGid, dstGid, tbd0, tbd1, tbd2, zone, CheckSum, crc ]
    # hks
    def getPid(self):
        return self.pid[0]
    def setPid(self, vaule):
        pid[0] = vaule

    def getRxTx(self):
        return self.rxtx[0]
    def setRxTx(self, vaule):
        rxtx[0] = vaule

    def getGid(self):
        return self.gid[0]
    def setGid(self, vaule):
        self.gid[0] = vaule

    def getHigh(self):
        return self.high[0]
    def setHigh(self, vaule):
        high[0] = vaule

    def getLow(self):
        return self.low[0]
    def setLow(self, vaule):
        low[0] = vaule

    def getLevel(self):
        return self.level[0]
    def setLevel(self, vaule):
        level[0] = vaule

    def getCmd(self):
        return self.cmd[0]
    def setCmd(self, vaule):
        cmd[0] = vaule

    def getSub(self):
        return self.sub[0]
    def setSub(self, vaule):
        sub[0] = vaule

    def getFrame(self):
        return self.frame

frame = Frame()
myFrame = frame.getFrame()

str_List = '{'
for numList in myFrame:
    if(numList[1]==2):
        str_List += '%04x' % numList[0]
    else:
        str_List += '%02x' % numList[0]
str_List += '}'
print(str_List)

with open("dict.txt","w") as f:
    print(str_List, file = f)

import crc16
print(crc16.crc16xmodem(b'123456789'))
