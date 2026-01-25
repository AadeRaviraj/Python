# 3. Write a program which accept one number from user and return its factorial.
# Input:
# 5
# Output: 120

num = int(input("Enter number : "))

result = 1
for i in range(1 , num + 1):
    result = result * i


print("Factorial is ",result)