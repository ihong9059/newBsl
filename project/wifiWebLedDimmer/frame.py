class Frame:
    Master = 64; ServerReq = 100;
    returnPowerOrStatus = ''
    returnMac = ''

    pidOrg = [0,1]; rxtxOrg = [Master,1];
    sensor = [1,1]; micom = [1,1]; gidOrg = [0,2]
    high = [100,1]; low = [1,1]; level = [50,1]; Type = [1,1]; rate = [1,1]
    status = [1,1]; dtime = [1,2]
    cmd = [ServerReq,1]; sub = [1,1]; time = [1,2]
    pid = [1,1]; rxtx = [64,1];  gid = [2,2]; srcGid = [1,2]
    tbd0 = [1,2]; tbd1 = [1,2]; tbd2 = [1,2]; zone = [1,1]; CheckSum = [1,1]
    crc = [1,2]

    frameList = [ pidOrg, rxtxOrg, sensor, micom, gidOrg,
        high, low, level, Type, rate, status, dtime,
        cmd, sub, time,
        pid, rxtx, gid, srcGid, tbd0, tbd1, tbd2, zone, CheckSum, crc ]

    frame = ''
    byteList = []
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
        print('SendFrame:{}'.format(self.frame))
        # self.returnPowerOrStatus = 'No Ack From Gateway'
    def getCrc(self, data):
        from crc import CRC
        crc16 = CRC()
        return crc16.update(data)
