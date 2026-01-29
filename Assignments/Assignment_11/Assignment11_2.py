# 2. Write a program which contains one lambda function which accepts two parameters and return its multiplication.
# Input: 4 3
# Output: 12
# Input: 6 3
# Output: 18

multiplication = lambda a, b : a * b

num1 = int(input())
num2 = int(input())

result = multiplication(num1, num2)
print("output : ",result)