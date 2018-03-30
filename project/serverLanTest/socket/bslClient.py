import socket
host='192.168.40.3'    #my Computer Address
# host='192.168.50.19'  #Windows Address
port=40007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
s.send(b'Hello, python Server')
data=s.recv(1024)
s.close()
print('Received',repr(data))
