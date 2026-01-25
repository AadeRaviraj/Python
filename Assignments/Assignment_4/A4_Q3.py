
# 3. Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def MathematicalOp(No1,No2):
    
    Addition = 0
    Subtraction = 0 
    Multiplication = 0
    Division = 0
    
    Addition = No1 + No2
    Subtraction = No1 - No2
    Multiplication = No1 * No2
    Division = No1 / No2
    
    return Addition, Subtraction,Multiplication,Division

num1 = int(input("Enter First Number : "))

num2 = int(input("Enter Second number : "))

ResultAddition ,ResultSubtraction,ResultMultiplication,ResultDivision = MathematicalOp(num1, num2)
print("Addition : ", ResultAddition)
print("Subtraction : ", ResultSubtraction)
print("Multiplication : ", ResultMultiplication)
print("Division : ", ResultDivision)
    