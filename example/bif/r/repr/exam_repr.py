# The repr() method returns a printable representation of the given object.

var = 'foo'

print(repr(var))


class Person:
    name = 'Adam'

    def __repr__(self):
        return repr(self.name)

print(repr(Person()))
