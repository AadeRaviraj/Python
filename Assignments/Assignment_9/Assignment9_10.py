# 10. Write a program which accept number from user and return addition of digits in that number.
# Input: 5187934
# Output: 37


num = int(input("Enter a number : "))

rem = 0
addition = 0
while(num != 0  ):
    rem = num % 10  # get remainder
    addition = addition + rem
    num = num // 10  # decrease value 
    
print("Addition  : ", addition)

