# 4. Write a program which accepts one number and prints that many numbers starting from 1.
# Input: 5
# Output: 12345


def ShowStartNum(No):
    Result = []
    for i in range(1, No + 1):
        Result.append(i)
        
    return Result


num = int(input("Enter a number : "))

Ret = ShowStartNum(num)

print("Output :" , Ret)


# for i in range(1 , num + 1):
#     print(i)