# The range() constructor returns an immutable sequence object of integers between the given start integer to the stop integer.
# empty range
print(list(range(0)))

# using range(stop)
print(list(range(10)))

# using range(start, stop)
print(list(range(1, 10)))

# Example 2: Create a list of even number between the given numbers using range()
start = 2
stop = 14
step = 2

print(list(range(start, stop, step)))

# Example 3: How range() works with negative step?
start = 2
stop = -14
step = -2

print(list(range(start, stop, step)))

# value constraint not met
print(list(range(start, 14, step)))
