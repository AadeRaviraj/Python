
# 3. Write a lambda function which accepts two numbers and returns maximum number.

result = lambda a,b : a if a>b else b


num1= int(input("Input : "))
num2 = int(input("Input : "))
print("Max Value : ",result(num1,num2))