import socket
from frame import Frame

receiveFlag = False
returnMac = ''
returnPowerOrStatus = ''

def sendSocket(arr):
    myFrame = Frame()

    # host='192.166.1.2'    #my Computer Address
    host='127.0.0.1'    #my Computer Address
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
    print('Received:{}'.format(str(data)))

    s.close()

    myFrame.parseFrame(str(data))

    global receiveFlag
    global returnMac
    global returnPowerOrStatus
    receiveFlag = True
    returnMac = myFrame.returnMac
    returnPowerOrStatus = myFrame.returnPowerOrStatus
