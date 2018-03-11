def print_args(**kwlist):
    print(kwlist)

vals = {'p3':'3', 'p2':'2', 'p1':'1'}
print_args(**vals)

print_args(p3='3', p2='2', p1='1')
