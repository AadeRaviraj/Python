# 4. Write a program which accepts one number and prints binary equivalent.

num = int(input("Enter a number  : "))

binary = 0
start = 1
rem = 0
while num > 0:
    rem = num % 2
    binary = binary + rem * start 
    
    num = num // 2
    start = start * 10
    
    
    
print(binary)
    