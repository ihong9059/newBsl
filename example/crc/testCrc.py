# from crc import CRC, CRC16, CRC32
from crc import CRC

print('Start Crc Test')
# crc16 = CRC(16, 0x8005, 0xffff, 0, False)
# crc16 = CRC(16, 0x8005, 0, 0)
crc16 = CRC()
a = list()
for i in range(0,128):
    a.append(i)
# print(a)

b =bytearray(a)
# print(b)

result = crc16.update(a)
print(result)
#
if __name__ == '__main__':
    print('End of CRC Test')
