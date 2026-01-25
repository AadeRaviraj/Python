
# 6. Write a lambda function which accepts
# one number and returns True if number is odd otherwise False.

result = lambda a : True if a % 2 != 0 else False

num = int(input("Input : "))
print("Output : ", result(num))