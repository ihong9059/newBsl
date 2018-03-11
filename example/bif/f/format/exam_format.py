# The built-in format() method returns a formatted representation of the given value controlled by the format specifier.
# Example 1: Number formatting with format()
# d, f and b are type

# integer
print(format(123, "d"))

# float arguments
print(format(123.4567898, "f"))

# binary format
print(format(12, "b"))

# Example 2: Number formatting with fill, align, sign, width, precision and type
# integer
print(format(1234, "*>+7,d"))
print(format(1234, "*<+7,d"))
print(format(1234, "*>+10,d"))
print(format(1234, "*<+10,d"))

# float number
print(format(123.4567, "^-09.3f"))
