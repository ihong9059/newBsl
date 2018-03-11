# The print() function prints the given object to the standard output device (screen) or to the text stream file.

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# Example 2: print() with separator and end parameters
a = 5
print("a =", a, sep='00000', end='\n\n\n')
print("a =", a, sep='0', end='')

# Example 3: print() with file parameter
sourceFile = open('python.txt', 'w')
print('Pretty cool, huh!', file = sourceFile)
sourceFile.close()
