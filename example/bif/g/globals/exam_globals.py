# The globals() method returns the dictionary of the current global symbol table.
age = 23

globals()['age'] = 25
print('The age is:', age)

print(globals())
