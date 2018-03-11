# The id() function returns identity (unique integer) of an object.
class Foo:
    b = 5

dummyFoo = Foo()
print('id of dummyFoo =',id(dummyFoo))

print('id of 5 =',id(5))

a = 5
print('id of a =',id(a))

b = a
print('id of b =',id(b))

c = 5.0
print('id of c =',id(c))
