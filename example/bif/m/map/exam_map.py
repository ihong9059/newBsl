# The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.

# Example 1: How map() works?
def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)


# Example 2: How to use lambda function with map()?
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)

# Example 3: Passing Multiple Iterators to map() Using Lambda
num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))
