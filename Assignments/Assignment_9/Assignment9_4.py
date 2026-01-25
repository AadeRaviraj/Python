# 4. Write a program which accept one number form user and return addition of its factors.
# Input:
# 12
# Output: 16
# (1 + 2 + 3 + 4 + 6)

num = int(input("Enter a number : "))

sum = 0 
for i in range(1, num ): 
    if num % i == 0:
        sum = sum + i 

print("Output is : ",sum)