# Create a Rectangle class that computes its own area and perimeter

# Create a class Rectangle with instance attributes width and height (set manually after creation). Add two methods, area() and perimeter(), that calculate and return the correct values using self. Create three Rectangle objects with different dimensions and print each one's area and perimeter using a loop.


class Rectangle:
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rect1 = Rectangle()
rect1.width = 10
rect1.height = 5

rect2 = Rectangle()
rect2.width = 8
rect2.height = 4

rect3 = Rectangle()
rect3.width = 12
rect3.height = 6

rectangles = [rect1, rect2, rect3]

for rect in rectangles:
    print(f"Area = {rect.area()}")
    print(f"Perimeter = {rect.perimeter()}")
    print()

