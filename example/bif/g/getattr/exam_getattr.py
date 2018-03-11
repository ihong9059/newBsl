# The getattr() method returns the value of the named attribute of an object.
# If not found, it returns the default value provided to the function.
# Example 1: How getattr() works in Python?
class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age)
print('The name is:', getattr(person, "name"))


# Example 2: getattr() when named attribute is not found
class Person:
    age = 23
    name = "Adam"

person = Person()

# when default value is provided
print('The sex is:', getattr(person, 'sex', 'Male'))

# when no default value is provided
print('The sex is:', getattr(person, 'sex'))
