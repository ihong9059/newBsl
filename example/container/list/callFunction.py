def add(*arg):
    total = 0
    for i in arg:
        total += i
    return total

vals = [1,2]
print(add(*vals))

vals = (4,5)
print(add(*vals))

vals = range(1,10)
print(add(*vals))
