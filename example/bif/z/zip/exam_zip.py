# The zip() function take iterables (can be zero or more), makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples.

# The syntax of zip() is:
#
# zip(*iterables)

# Example 1: How zip() works in Python?
numberList = [1, 2, 3]
strList = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting itertor to list
resultList = list(result)
print(resultList)

# Two iterables are passed
result = zip(numberList, strList)
print(result)

# Converting itertor to set
resultSet = set(result)
print(resultSet)


# Example 2: Different Number of Elements in Iterables Passed to zip()
numbersList = [1, 2, 3]
strList = ['one', 'two']
numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')

result = zip(numbersList, numbersTuple)

# Converting to set
resultSet = set(result)
print(resultSet)

result = zip(numbersList, strList, numbersTuple)

# Converting to set
resultSet = set(result)
print(resultSet)


# Example 3: Unzipping the Value Using zip()
coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]

result = zip(coordinate, value)
resultList = list(result)
print(resultList)

c, v =  zip(*resultList)
print('c =', c)
print('v =', v)
