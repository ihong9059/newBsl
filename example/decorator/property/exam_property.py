class Rectangle(object):
    def __init__(self, w, h):
        self._width = w
        self._height = h

    def getArea(self):
        return self._width * self._height

    @property            #<---- 1
    def width(self):     #<---- 2
        print('@property.width')
        return self._width   #<---- 3

    @width.setter        #<---- 4
    def width(self, w):  #<---- 5
        print('@width.setter')
        self._width = max( 10, min(100, self._width) )

    @property
    def height(self):
        print('@property.height')
        return self._height

    @height.setter
    def height(self, h):
        print('@height.setter')
        self._height = max( 10, min(100, self._height) )

r1 = Rectangle(10, 10)
r2 = Rectangle(10, 10)

r1.width = 100        #<--- 6
r2.height = 20

print("rectangle({}, {})".format(r1.width, r1.height)) #<---- 7

print("area : {}".format(r1.getArea()))
