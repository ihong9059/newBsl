import socket
host='192.166.0.3'    #my Computer Address
# host='192.166.0.3'    #my Computer Address
# host='192.168.185.2'    #my Computer Address

port=40007
print('hostName:{}, port:{}'.format(host, port))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

arr = '{0040010100006401010101010100646701000a20070001000100010001000101b672}'
barr = bytearray(arr, 'utf-8')
s.send(barr)
print('Sent:{}'.format(arr))
# s.send(b'Hello, python Server')
data=s.recv(1024)

s.close()

print('Received',repr(data))
