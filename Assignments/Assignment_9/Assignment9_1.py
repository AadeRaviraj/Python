# 1. Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction,
# Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. 
# Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.


import Arithmetic

num1 = int(input("Enter first number : "))

num2 = int(input("Enter Second number : "))

Addition = Arithmetic.Add(num1, num2)

Substraction = Arithmetic.Sub(num1, num2)

Multiplication = Arithmetic.Mult(num1, num2)

Division = Arithmetic.Div(num1, num2)

print("Addition  is ", Addition)
print("Substraction   is ", Substraction)
print("Multiplication  is ", Multiplication)
print("Division is ", Division)
