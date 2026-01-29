# 3: Write a Python program to implement a class named Arithmetic with the following characteristics:
# The class should contain two instance variables: Valuel and Value2.
# Define a constructor (init) that initializes all instance variables to 0.
# Implement the following instance methods:
# Accept() accepts values for Valuel and Value2 from the user.
# Addition()returns the addition of Valuel and Value2.
# Subtraction()returns the subtraction of Valuel and Value2.
# 0 Multiplication() returns the multiplication of Valuel and Value2.
# Division() returns the division of Valuel and Value2 (handle division by zero properly).
# Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmetic():
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self):
        self.Value1 = int(input("Enter First value : "))
        
        self.Value2 = int(input("Enter Second value : "))
        
    def Addition(self):
        print("Addition :",self.Value1 + self.Value2)
            
    def Subtraction(self):
        print("Subtraction : ", self.Value1 - self.Value2)
            
    def Multiplication(self):
        print("Multiplication : ", self.Value1 * self.Value2)
            
    def Division(self):
        print("Division : ",self.Value1 / self.Value2)
    

Obj1 = Arithmetic()

Obj1.Accept()
Obj1.Addition()
Obj1.Subtraction()
Obj1.Multiplication()
Obj1.Division()