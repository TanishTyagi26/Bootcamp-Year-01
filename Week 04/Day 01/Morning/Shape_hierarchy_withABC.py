# ================================ Shape Hierarchy with ABC ================================ 

# Create an abstract Shape base class with abstract methods area() and perimeter(). Implement Circle, Rectangle, and Triangle subclasses. Add a classmethod Shape. total_shapes() tracking count. Write a function print_report(shapes_list) that polymorphically calls describe() on each.

# (Hint: from abc import ABC, abstractmethod; use class variable_count in Shape._init_)


from abc import ABC, abstractmethod

class Shape(ABC):
    _count = 0

    def __init__(self, color):
        self.color = color
        Shape._count += 1

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"Color = {self.color} , Area = {self.area()}  , Perimeter = {self.perimeter()}"

    @classmethod
    def total_shapes(cls):
        return cls._count


class Circle(Shape):
    def __init__(self, r, color="blue"):
        super().__init__(color)
        self.r = r

    def area(self):
        return 3.14159 * self.r ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.r


class Rectangle(Shape):
    def __init__(self, w, h, color="yellow"):
        super().__init__(color)
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


class Triangle(Shape):
    def __init__(self, a, b, c, color="green"):
        super().__init__(color)
        self.a, self.b, self.c = a, b, c

    def area(self):
        semi_peri = (self.a + self.b + self.c) / 2
        return (semi_peri * (semi_peri - self.a) * (semi_peri - self.b) * (semi_peri - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


def print_report(shapes_list):
    for shape in shapes_list:
        print(shape.describe())


shapes = [Circle(7),Rectangle(4, 6),Triangle(3, 4, 5)]

print_report(shapes)

print("Total Shapes =", Shape.total_shapes())