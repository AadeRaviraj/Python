# 9. Write a program which accept number from user and return number of digits in that number.
# Input: 5187934
# Output: 7

num = int(input("Enter a number  : "))

result = 0

while num != 0:
    num = num // 10 
    result = result + 1
    

print(result)