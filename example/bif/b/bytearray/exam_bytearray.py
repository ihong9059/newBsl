# If you want to use the mutable version, use bytearray() method.
string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)

size = 5

arr = bytearray(size)
print(arr)


rList = [1, 2, 3, 4, 5, 11]

arr = bytearray(rList)
print(arr)
