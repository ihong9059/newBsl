# The pow() method returns x to the power of y. If the third argument (z) is given, it returns x to the power of y modulus z, i.e. pow(x, y) % z.



# positive x, positive y (x**y)
print(pow(2, 2))

# negative x, positive y
print(pow(-2, 2))

# positive x, negative y (x**-y)
print(pow(2, -2))

# negative x, negative y
print(pow(-2, -2))


x = 7
y = 2
z = 5

print(pow(x, y, z))
