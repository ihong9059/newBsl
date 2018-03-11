x = 5
print(callable(x))

def testFunction():
  print("Test")

y = testFunction
print(callable(y))


class Foo:
  def __call__(self):
    print('Print Something')

print(callable(Foo))

class Foo:
  def __call__(self):
    print('Print Something')

InstanceOfFoo = Foo()

# Prints 'Print Something'
InstanceOfFoo()

class Foo:
  def printLine(self):
    print('Print Foo Something')

print(callable(Foo))

InstanceOfFoo = Foo()
InstanceOfFoo.printLine()

# Raises an Error
# 'Foo' object is not callable
InstanceOfFoo()
