# Example 1: Find minimum among the given numbers
# using min(arg1, arg2, *args)
print('Minimum is:', min(1, 3, 2, 5, 4))

# using min(iterable)
num = [3, 2, 8, 5, 10, 6]
print('Minimum is:', min(num))


def sumDigit(num):
    sum = 0
    while(num):
        sum += num % 10
        num = int(num / 10)
    return sum

# using min(arg1, arg2, *args, key)
print('Minimum is:', min(100, 321, 267, 59, 40, key=sumDigit))

# using min(iterable, key)
num = [15, 300, 2700, 821, 52, 10, 6]
print('Minimum is:', min(num, key=sumDigit))
