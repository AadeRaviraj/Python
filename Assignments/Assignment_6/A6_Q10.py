
# 10. Write a lambda function which accepts three numbers and returns largest number.

result = lambda a, b , c : a if a > b and a > c else b  if b > c else c 

num1 = int(input("input Num 1 : "))
num2 =int(input("input Num 2: "))
num3 = int(input("input Num 3 : "))

print(result(num1, num2, num3))