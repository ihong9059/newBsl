"""
Pi4IoT    -> https://www.youtube.com/pi4iot
draw symbol on the ssd1306 display
"""

import ssd1306
import machine
import sys
from machine import I2C, Pin
import time

i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(64, 48, i2c)
# display = ssd1306.SSD1306_I2C(128, 64, i2c)

def dispOled(strList):
    display.fill(0)
    lineY = 0
    for line in strList:
        display.text('{}'.format(line), 1, lineY*10)
        lineY += 1
    display.show()

def testDisp():
    while True:
        # if input() == 'q':
        #     print('End of loop')
        #     break
        count += 1
        if count > 2000:
            break
        strList = list()
        for i in range(6):
            strList.append(count+i)
        dispOled(strList)
        time.sleep(1)

# import signal
if __name__ == '__main__':
    testDisp()
