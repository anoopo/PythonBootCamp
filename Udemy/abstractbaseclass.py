from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    side = 4
    def area(self):
        print ("Area of square = ", self.side * self.side)

class Rectangle(Shape):
    l = 4
    b = 5
    def area(self):
        print ("Area of Rectangle = ", self.l * self.b)

sq = Square()
rt = Rectangle()
sq.area()
rt.area()
