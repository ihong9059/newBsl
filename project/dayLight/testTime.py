import time
from hksSer import serThread
from datetime import datetime
from frame import Frame

mySer = serThread()

dt = datetime.now()

end = True
print(type(dt))
print('dt.second:{}'.format(type(dt.second)))
nowSecond = dt.second + 1
count = 0
while end:
    if datetime.now().second == (nowSecond%60):
        nowSecond = datetime.now().second + 10
        count += 1
        print('{}:{}'.format(count,dt.now().isoformat(sep = '/', timespec='seconds')))
