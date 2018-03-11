# The iter() method returns an iterator for the given object.


# Example 1: How iter() works in Python?

# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

vowelsIter = iter(vowels)

# prints 'a'
print(next(vowelsIter))

# prints 'e'
print(next(vowelsIter))

# prints 'i'
print(next(vowelsIter))

# prints 'o'
print(next(vowelsIter))

# prints 'u'
print(next(vowelsIter))

# Example 2: How iter() works for custom objects?

class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

printNum = PrintNumber(3)

printNumIter = iter(printNum)

# prints '1'
print(next(printNumIter))

# prints '2'
print(next(printNumIter))

# prints '3'
print(next(printNumIter))

# raises StopIteration
# print(next(printNumIter))

# Example 3: How iter() works for callable objects with sentinel?
with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        print(line)
