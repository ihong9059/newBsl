# decimal number
print('oct(10) is:', oct(10))

# binary number
print('oct(0b101) is:', oct(0b101))

# hexadecimal number
print('oct(0XA) is:', oct(0XA))

# Example 2: How oct() for custom objects by implementing __index__()?
class Person:
    age = 23

    def __index__(self):
        return self.age

    def __int__(self):
        return self.age

person = Person()
print('The oct is:', oct(person))
