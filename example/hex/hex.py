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
