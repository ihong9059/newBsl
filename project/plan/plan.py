import re
# This is explanation of bsl local server system
print('Main structure')
print('http web server for cloud server')
print('thread for serial input from LoRa gateway')
print('display with oled')
print('make database class for LoRa and cloud')
"""
typedef struct
{
	uint8_t PrivateAddr;
	RxTx_t RxTx;
	Sensor_t SensorType;
	Micom_t Micom;
	uint16_t GroupAddr;
} MyAddr_t;
typedef struct
{
	uint8_t High;
	uint8_t Low;
	uint8_t Level;
	uint8_t Type;
	uint8_t SensorRate;
	Status_t Status;
	uint16_t DTime;
} Ctr_t;

typedef struct
{
	uint8_t Command;
	uint8_t SubCmd;
	uint16_t Time;
} Cmd_t;

typedef struct{
	uint8_t pid;
	uint8_t rxtx;
	uint16_t gid;
} dst_t;
typedef struct
{
	uint8_t SrcPrivateAddr;
	uint8_t DstPrivateAddr;
	uint16_t SrcGroupAddr;
	uint16_t DstGroupAddr;
	uint16_t Reserve[3];
	uint8_t Zone;
	uint8_t CheckSum;
} Trans_t;
"""
class bslData:
    loraData = str()
    cloudData = str()
    myaddress = dict(gid = 1, pid = 2, rxtx =3)
    test = "[111, 222, 333]"

    def __init__(self):
        self.ctr = dict()
        self.cmd = dict()
        self.tran = dict()

    def returnAddr(self):
        return self.myaddress

    def incAddr(self):
        bslData.myaddress['gid'] += 1

    def testAddr(self):
        test = eval(self.test)
        i = 0
        for key in self.myaddress:
            self.myaddress[key] =  test[i]
            i += 1
    def testRe(self):
        #          012345678901234567890
        strTest = 'hks[1234[56789]01234]hong'
        h = strTest.rfind('[')
        print(h)
        h = strTest.rfind(']')
        print(h)
        h = strTest.find('[')
        print(h)
        h = strTest.find(']')
        print(h)
        h = strTest.find('*')
        print(h)
    """
    {111, 222, 333}
    loraData frame = {xxx,yyy,....}, element = 32
    cloudData frame = {xxx,yyy,...., security}, loraData + security

    basic data structure
    myaddress
    ctr
    cmd
    trans
    """
    pass

hks = bslData()
hks.incAddr()

hksData = hks.returnAddr()
print('hksData:', hksData['gid'])
# addrGid = hks.returnAddr()
print('myaddress:', hks.myaddress['gid'])

hks.testAddr()
print('myaddress:', hks.myaddress['gid'])

hks.testRe()
