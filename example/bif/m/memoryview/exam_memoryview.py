# Example 1: How memoryview() works in Python?

#random bytearray
randomByteArray = bytearray('ABC', 'utf-8')

mv = memoryview(randomByteArray)

# access memory view's zeroth index
print(mv[0])

# create byte from memory view
print(bytes(mv[0:2]))

# create list from memory view
print(list(mv[0:3]))

# Example 2: Modify internal data using memory view
#random bytearray
randomByteArray = bytearray('ABC', 'utf-8')
print('Before updation:', randomByteArray)

mv = memoryview(randomByteArray)

# update 1st index of mv to Z
mv[1] = 90
print('After updation:', randomByteArray)
