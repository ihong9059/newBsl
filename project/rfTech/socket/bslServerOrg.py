import socket
import time

host=''
port=40007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn, addr=s.accept()
print('Connected by',addr)
count = 0
while True:
    data=conn.recv(1024)
    serialInput=str(data,'utf-8')
    print(serialInput)
    time.sleep(1)
    print('count:',count)
    count += 1
    # if not data:
    #     break
    conn.send(data)
conn.close()
