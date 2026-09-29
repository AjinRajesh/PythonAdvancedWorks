#create an abstract class shape with abstract methods get_area() and get_perimeter()

from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        self.length=int(input("Length: "))
        self.breadth=int(input("Breadth: "))

    def get_area(self):
        print("Area:",self.length*self.breadth)

    def get_perimeter(self):
        print("Perimeter:",2*(self.length+self.breadth))
        print()


class Square(Shape):
    def __init__(self):
        self.side=int(input("Length of a side: "))


    def get_area(self):
        print("Area of square:",self.side**2)

    def get_perimeter(self):
        print("Perimeter of square:",4*self.side)


r=Rectangle()
r.get_area()
r.get_perimeter()

s=Square()
s.get_area()
s.get_perimeter()