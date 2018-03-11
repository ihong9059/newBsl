# The slice() constructor creates a slice object representing the set of indices specified by range(start, stop, step).
# slice(start, stop, step)

# contains indices (0, 1, 2)
print(slice(3))

# contains indices (1, 3)
print(slice(1, 5, 2))

pyString = 'Python'

# contains indices (0, 1, 2)
# i.e. P, y and t
sObject = slice(3)

print(pyString[sObject])

# contains indices (1, 3)
# i.e. y and h
sObject = slice(1, 5, 2)

print(pyString[sObject])

# Example 3: Get substring from a given string using negative index
pyString = 'Python'

# contains indices (-1, -2, -3)
# i.e. n, o and h
sObject = slice(-1, -4, -1)

print(pyString[sObject])

# Example 4: Get sublist and sub-tuple from a given list and tuple respectively
pyList = ['P', 'y', 't', 'h', 'o', 'n']
pyTuple = ('P', 'y', 't', 'h', 'o', 'n')

# contains indices (0, 1, 2)
# i.e. P, y and t
sObject = slice(3)

# slice a list
print(pyList[sObject])

# contains indices (1, 3)
# i.e. y and h
sObject = slice(1, 5, 2)

# slice a tuple
print(pyTuple[sObject])

# Example 5: Get sublist and sub-tuple from a given list and tuple respectively using negative index
pyList = ['P', 'y', 't', 'h', 'o', 'n']
pyTuple = ('P', 'y', 't', 'h', 'o', 'n')

# contains indices (-1, -2, -3)
# i.e. n, o and h
sObject = slice(-1, -4, -1)

# slice a list
print(pyList[sObject])

# contains indices (-1, -3)
# i.e. n and h
sObject = slice(-1, -5, -2)

# slice a tuple
print(pyTuple[sObject])

# Example 6: Get substring from a given string by extending indexing syntax
pyString = 'Python'

# contains indices (0, 1, 2)
# i.e. P, y and t
print(pyString[0:3])

# contains indices (1, 3)
# i.e. y and h
print(pyString[1:5:2])
