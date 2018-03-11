# The next() function returns the next item from the iterator.
# next(iterator, default)

# Example 1: How next() works?
random = [5, 9, 'cat']

# converting list to iterator
randomIterator = iter(random)
print(randomIterator)

# Output: 5
print(next(randomIterator))

# Output: 9
print(next(randomIterator))

# Output: 'cat'
print(next(randomIterator))

# This will raise Error
# iterator is exhausted
# print(next(randomIterator))


random = [5, 9, 'cat']

# converting list to iterator
randomIterator = iter(random)
print(random)

# Output: 5
print(next(random))
