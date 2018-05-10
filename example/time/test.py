import datetime

dt = datetime.now()

end = True
while end:
    if dt.minute != datetime.now().minute:
        print(datetime.now())
        dt.minute = datetime.now() + 1
