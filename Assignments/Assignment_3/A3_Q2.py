
# 2.Write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

def CountNumber(No):
    Count = 0
    
    while(No != 0):
        No = No // 10
        Count = Count + 1
    return Count

number = int(input("Enter a number :"))

Ret = CountNumber(number)
print(Ret)