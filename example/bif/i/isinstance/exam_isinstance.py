# The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).

class Foo:
  a = 5

fooInstance = Foo()

print(isinstance(fooInstance, Foo))
print(isinstance(fooInstance, (list, tuple)))
print(isinstance(fooInstance, (list, tuple, Foo)))
