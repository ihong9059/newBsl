# The int() method returns an integer object from any number or string.

# int(x=0, base=10)

# integer
print("int(123) is:", int(123))

# float
print("int(123.23) is:", int(123.23))

# string
print("int('123') is:", int('123'))


# binary 0b or 0B
print("For 1010, int is:", int('1010', 2))
print("For 0b1010, int is:", int('0b1010', 2))

# octal 0o or 0O
print("For 12, int is:", int('12', 8))
print("For 0o12, int is:", int('0o12', 8))

# hexadecimal
print("For A, int is:", int('A', 16))
print("For 0xA, int is:", int('0xA', 16))


class Person:
    age = 23

    def __index__(self):
        return self.age

    def __int__(self):
        return self.age

person = Person()
print('int(person) is:', int(person))
