# The hex() function converts an integer number to the corresponding hexadecimal string.

number = 435
print(number, 'in hex =', hex(number))

number = 0
print(number, 'in hex =', hex(number))

number = -34
print(number, 'in hex =', hex(number))

returnType = type(hex(number))
print('Return type from hex() is', returnType)
