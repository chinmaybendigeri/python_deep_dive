class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError
        else:
            self._height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def __repr__(self):
        return "Rectangle({0},{1})".format(self.width, self.height)

    def __lt__(self, other):
        if isinstance(self, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

r1 = Rectangle(10,20)
print(r1)

print(r1.width)

r1.width = 100

print(r1)

print(str(r1))

r2 = Rectangle(2,3)
print(r2 < r1)
print(r2)

print(r2._width)


