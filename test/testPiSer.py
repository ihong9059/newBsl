import serial
ser = serial.Serial('/dev/ttyS0', 115200, timeout = 0)
arr = bytearray('This is test frame from pi','ascii')
ser.write(arr)
ser.close()
