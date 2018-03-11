# The locals() method updates and returns the dictionary of the current local symbol table.

def localsNotPresent():
    return locals()

def localsPresent():
    present = True
    return locals()

print('localsNotPresent:', localsNotPresent())
print('localsPresent:', localsPresent())

def localsPresent():
    present = True
    print(present)
    locals()['present'] = False;
    print(present)

localsPresent()
