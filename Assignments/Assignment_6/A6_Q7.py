
# 7. Write a lambda function which accepts one number and returns True if divisible by 5.

res = lambda a : True if a % 5 == 0 else False

no = int(input("Input : "))
print("Output : ", res(no))