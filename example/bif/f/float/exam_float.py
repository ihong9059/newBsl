# The float() method returns a floating point number from a number or a string.

# Example 1: How float() works in Python?
# for integers
print(float(10))

# for floats
print(float(11.22))

# for string floats
print(float("-13.33"))

# for string floats with whitespaces
print(float("     -24.45\n"))

# string float error
# print(float("abc"))

# Example 2: float() for infinity and Nan(Not a number)?
# for NaN
print(float("nan"))
print(float("NaN"))

# for inf/infinity
print(float("inf"))
print(float("InF"))
print(float("InFiNiTy"))
print(float("infinity"))
