import time

print(time.time)
print(time.gmtime())
print(time.localtime())
t = time.gmtime(1234567890)
print(t)

print(time.asctime(t))

from datetime import datetime
dt = datetime.now()
print(dt)

print(dt.date())
print(dt.time())
