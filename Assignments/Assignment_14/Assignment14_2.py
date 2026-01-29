# 2: Write a Python program to implement a class named Circle with the following requirements:
# The class should contain three instance variables: Radius. Area, and Circumference.
# The class should contain one class variable named PI, initialized to 3.14.
# Define a constructor (init) that initializes all instance variables to 0.0.
# . Implement the following instance methods:
# Accept()accepts the radius of the circle from the user.
# CalculateArea()calculates the area of the circle and stores it in the Area variable.
# CalculateCircumference()-calculates the circumference of the circle and stores it in the Circumference variable.
# Display()-displays the values of Radius. Area, and Circumference.
# Create multiple objects of the Circle class and invoke all the instance methods for each object.

class Circle:
    
    PI = 3.14
    
    def __init__(self):
        self.Radius = 0.0
        self.Area =  0.0
        self.Curcumference = 0.0
        
    def Accept(self):
        self.Radius = float(input("Enter Radius : "))
            
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
    
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
    
    def Display(self):
        print("Radius:", self.Radius)
        print("Area:", self.Area)
        print("Circumference:", self.Circumference)

c1 = Circle()
c1.Accept()
c1.CalculateArea()
c1.CalculateCircumference()
c1.Display()

c2 = Circle()
c2.Accept()
c2.CalculateArea()
c2.CalculateCircumference()
c2.Display()
