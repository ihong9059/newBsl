# The isinstance() function checks if the object argument (first argument) is a subclass of classinfo class (second argument).


class Polygon:
  def __init__(polygonType):
    print('Polygon is a ', polygonType)

class Triangle(Polygon):
  def __init__(self):
    Polygon.__init__('triangle')

print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle, (list, Polygon)))
print(issubclass(Polygon, (list, Polygon)))
