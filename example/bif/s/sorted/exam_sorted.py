# The sorted() method returns a sorted list from the given iterable.

# Example 1: Sort a given sequence: string, list and tuple

# vowels list
pyList = ['e', 'a', 'u', 'o', 'i']
print(sorted(pyList))

# string
pyString = 'Python'
print(sorted(pyString))

# vowels tuple
pyTuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(pyTuple))


# Example 2: Sort a given collection in descending order: set, dictionary and frozen set
# set
pySet = {'e', 'a', 'u', 'o', 'i'}
print(sorted(pySet, reverse=True))

# dictionary
pyDict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(pyDict, reverse=True))

# frozen set
pyFSet = frozenset(('e', 'a', 'u', 'o', 'i'))
print(sorted(pyFSet, reverse=True))


# Example 3: Sort the list using sorted() having a key function
# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sortedList = sorted(random, key=takeSecond)

# print list
print('Sorted list:', sortedList)
