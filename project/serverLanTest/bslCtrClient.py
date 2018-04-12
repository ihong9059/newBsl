import socket
from frame import Frame

receiveFlag = False
returnMac = ''
returnPowerOrStatus = ''

def sendSocket(arr):
    host='192.166.0.6'    #my Computer Address
    # host='192.166.0.3'    #my Computer Address
    # host='192.166.0.3'    #my Computer Address
    # host='192.168.185.2'    #my Computer Address
    myFrame = Frame()

    port=40007
    print('hostName:{}, port:{}'.format(host, port))

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))

    # arr = '{0040010100006401010101010100646701000a20070001000100010001000101b672}'
    barr = bytearray(arr, 'utf-8')
    s.send(barr)
    print('Sent:{}'.format(arr))
    # s.send(b'Hello, python Server')
    data=s.recv(1024)
    print('Received',repr(data))

    s.close()
    myFrame.parseFrame(str(data))

    global receiveFlag
    global returnMac
    global returnPowerOrStatus
    receiveFlag = True
    returnMac = myFrame.returnMac
    returnPowerOrStatus = myFrame.returnPowerOrStatus
