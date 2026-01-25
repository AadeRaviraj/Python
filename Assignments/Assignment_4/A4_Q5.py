# 5. Write a program which accepts one number and prints that many numbers in reverse order.
# Input: 5
# Output: 54321



def ShowLastNum(No):
    Result = []
    for i in range(No, 0, -1):  # start , stop , step 
        Result.append(i)
        
    return Result


num = int(input("Enter a number : "))

Ret = ShowLastNum(num)

print("Output :" , Ret)
