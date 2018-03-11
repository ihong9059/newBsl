# The eval() method parses the expression passed to this method and runs python expression (code) within the program.
# Example 1: How eval() works in Python?
x = 1
print(eval('x + 1'))

# Example 2: Practical Example to Demonstrate Use of eval()
# Perimeter of Square

print('Type calculateArea(l)')
def calculatePerimeter(l):
  return 4*l

# Area of Square
def calculateArea(l):
  return l*1

property = input("Type a function: ")

for l in range(1, 5):
    if (property == 'calculatePerimeter(l)'):
        print("If length is ", l , ", Perimeter = ", eval(property))
    elif (property == 'calculateArea(l)'):
        print("If length is ", l , ", Area = ", eval(property))
    else:
        print('Wrong Function')
        break

from math import *
print(eval('dir()'))
