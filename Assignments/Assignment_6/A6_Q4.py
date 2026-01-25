
# 4. Write a lambda function which accepts two numbers and returns minimum number.

result = lambda a , b : a if a<b else b

num1= int(input("Input : "))
num2 = int(input("Input : "))
print("Min value : ", result(num1,num2))
