import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
myIp = s.getsockname()[0]
print(s.getsockname()[0])
s.close()

host=myIp    #my Computer Address
# host='192.168.185.2'    #my Computer Address
# host='192.168.50.19'  #Windows Address
port=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
s.send(b'Hello, python Server')
data=s.recv(1024)
s.close()
print('Received',repr(data))
