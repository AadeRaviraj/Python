# 1: Write a Python program to implement a class named Demo with the following specifications:
# The class should contain two instance variables: no1 and no2.
# . The class should contain one class variable named Value.
# Define a constructor (init) that accepts two parameters and initializes the instance variables.
# Implement two instance methods:
# 0 Fun()-displays the values of instance variables nol and no2.
# Gun()-displays the values of instance variables no1 and no2.
# Create two objects of the Demo class as follows:
# Objl Demo(11, 21)
# Obj2 Demo (51, 101)
# Call the instance methods in the given sequence:
# Objl.Fun()
# Obj2.Fun()
# Objl.Gun()
# Obj2.Gun()

class Demo :
    value = 10
    
    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B
    
    def fun(self):
        print("Instance Variable accessed from Fun() : ",self.No1, self.No2)
    
    def gun(self):
        print("Instance Variable accessed from Gun() : ",self.No1, self.No2)
    

Objl = Demo(11, 21)
Obj2 = Demo(51, 101)

print("Class Variable : ",Demo.value)
        
Objl.fun()
Obj2.fun()
Objl.gun()
Obj2.gun()