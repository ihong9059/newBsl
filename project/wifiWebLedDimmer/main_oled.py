import usocket as socket
import machine
import network
from dispOled import dispOled
from machine import Pin
from time import sleep
import os

p0 = Pin(0, Pin.IN)

gCount = 0
def callback(p):
    global gCount
    gCount += 1
    print('pin change', p)
    print('gCount:{}'.format(gCount))
    receive = input('Wait, input your request now==> ')
    sleep(0.2)
    print('I received from Machine:{}'.format(receive))
    # input

p0.irq(trigger = Pin.IRQ_FALLING, handler = callback)

def wifiAp():
    import ubinascii
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(True)
    essid = b"UTTEC-%s" % ubinascii.hexlify(ap_if.config("mac")[-3:])
    ap_if.config(essid=essid, authmode=network.AUTH_WPA_WPA2_PSK, password=b"123456789a")
    print('mac:',b"UTTEC-%s" % ubinascii.hexlify(ap_if.config("mac")[:]))

def wifiSta():
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    # 8764b1
    # sta.connect("UTTEC-8764b1", "123456789a")
    sta.connect("uttecSale4", "123456789a")
    # sta.connect("utsol_tc140", "09090909")
    # sleep(3)
    count = 0
    while sta.isconnected() == False:
        sleep(1)
        print('wait wifi connection, elapsed Time:{}'.format(count))
        count +=1
    print('My ip Address:{}'.format(sta.ifconfig()))
    print('********************End of wifiSta')

wifiAp()
wifiSta()

def mySend(conn, msg, MSGLEN):
    print('MSGLEN:{}'.format(MSGLEN))
    totalsent = 0
    while totalsent < MSGLEN:
        sent = conn.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent
        print('totalsent:{}'.format(totalsent))
    # conn.close()

def webServer():
    print('------------------------- Setup Ap End -------------')
    print('Files:{}'.format(os.listdir()))
    html_org = ''
    with open('seju.html','r') as f:
        html_org=f.read()

    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    # addr = socket.getaddrinfo('192.168.185.14', 80)[0][-1]
    # addr = socket.getaddrinfo('192.168.4.1', 80)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.bind(('', 80))
    s.bind(addr)
    s.listen(1)
    print('My Addr:{}'.format(addr))
    count = 0
    dispList = ['SeJu FA','20180425','Red  Off', 'Blue Off','Ex   Off']
    dispOled(dispList)

    fileSize = 2048
    while True:
        html = html_org
        conn, addr = s.accept()
        request = conn.recv(fileSize)
        # request = myReceive(conn)
        count += 1
        if count%2:
            print("connection from %s" % str(addr))
            print("Content = %s" % str(request))
        request = str(request)
        LEDON_RED = request.find('/?LED=ON_R')
        LEDOFF_RED = request.find('/?LED=OFF_R')
        LEDON_BLUE = request.find('/?LED=ON_B')
        LEDOFF_BLUE = request.find('/?LED=OFF_B')
        LEDON_EX = request.find('/?LED=ON_E')
        LEDOFF_EX = request.find('/?LED=OFF_E')
        EXIT = request.find('/?LED=Exit')
        # print('LEDON_RED:{}'.format(LEDON_RED))
        if LEDON_RED == 6:
            print('Red Led ON')
            dispList[2] = 'Red   On'
        if LEDOFF_RED == 6:
            print('Red Led OFF')
            dispList[2] = 'Red  Off'

        if LEDON_BLUE == 6:
            print('Blue Led ON')
            dispList[3] = 'Blue  On'
        if LEDOFF_BLUE == 6:
            print('Blue Led OFF')
            dispList[3] = 'Blue Off'

        if LEDON_EX == 6:
            print('External Led ON')
            dispList[4] = 'Ex    On'
            # LED_EX.on()
        if LEDOFF_EX == 6:
            print('External Led OFF')
            dispList[4] = 'Ex   Off'
            # LED_EX.off()
        if EXIT == 6:
            print('Bye Bye Seju Demo')

            response = html
            mySend(conn, response, len(response))
            conn.close()
            break

        response = html
        mySend(conn, response, len(response))
        conn.close()
        dispOled(dispList)

if __name__ == '__main__':
    webServer()
