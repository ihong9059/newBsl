# The property() method a returns a property attribute.
# property(fget=None, fset=None, fdel=None, doc=None)

# Example 1: Create attribute with getter, setter and deleter using property()
class Person:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print('Getting name : ', end = '')
        return self._name

    def setName(self, value):
        print('Setting name to ' + value)
        self._name = value

    def delName(self):
        print('Deleting name')
        del self._name

    # Set property to use getName, setName
    # and delName methods
    name = property(getName, setName, delName, 'Name property')


p = Person('Adam')
print(p.name)

p.name = 'John'

del p.name

# Example 2: Create attribute with getter, setter and deleter using @property decorator
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Getting name : ', end = '')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name

p = Person('Adam')
print('The name is:', p.name)

p.name = 'John'

del p.name
