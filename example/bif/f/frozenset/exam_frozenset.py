# The frozenset() method returns an immutable frozenset object initialized with elements from the given iterable.
# Example 1: How frozenset() works in Python?
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())

# Example 2: frozenset() for Dictionary
# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)
