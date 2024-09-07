# Define a Circle class with radius r using constructor.
# then create area() & perimeter() method to calculate area & perimeter of the circle
class Circle:
    def __init__(self,radius):  # constructor
        self.radius = radius

    def area(self): # methods
        return 3.14*self.radius**2

    def perimeter(self):
        return 2*3.14*self.radius
    
c1 = Circle(5)  # object or instance
print("Radius of circle =",c1.radius)
print("Area = ",c1.area())
print("Perimeter = ",c1.perimeter())    
