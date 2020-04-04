class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return self.radius*self.radius*3.14
    def perimeter(self):
        return self.radius*2*3.14

a=int(input("Enter length of radius: "))
obj=Circle(a)
print("Area of Circle is:",obj.area())
print("Perimeter of Circle is:",obj.perimeter())
