# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)

# Example 1: Create Dictionary Using keyword arguments only
numbers = dict(x=5, y=0)
print('numbers = ',numbers)
print(type(numbers))

empty = dict()
print('empty = ',empty)
print(type(empty))

# Example 2: Create Dictionary Using Iterable
# keyword argument is not passed
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =',numbers1)

# keyword argument is also passed
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =',numbers2)

# zip() creates an iterable in Python 3
numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
print('numbers3 =',numbers3)

# Example 3: Create Dictionary Using Mapping
numbers1 = dict({'x': 4, 'y': 5})
print('numbers1 =',numbers1)

# you don't need to use dict() in above code
numbers2 = {'x': 4, 'y': 5}
print('numbers2 =',numbers2)

# keyword argument is also passed
numbers3 = dict({'x': 4, 'y': 5}, z=8)
print('numbers3 =',numbers3)
