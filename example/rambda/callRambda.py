fruits = ['apple', 'banana', 'kiwi', 'watermelon']

def name_length(x):
    return len(x)

fruits.sort(key = name_length)
print(fruits)

fruits = ['apple', 'banana', 'kiwi', 'watermelon', 'orange']
fruits.sort(key = lambda x : len(x))
print(fruits)
