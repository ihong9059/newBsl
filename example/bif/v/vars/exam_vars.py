# The vars() function returns the __dict__ attribute of the given object if the object has __dict__ attribute.




class Foo:
  def __init__(self, a = 5, b = 10):
    self.a = a
    self.b = b

InstanceOfFoo = Foo()
print(vars(InstanceOfFoo))
