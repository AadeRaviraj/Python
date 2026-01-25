
# 5.Write a program which accepts one number and prints all odd numbers till that number.
# Input :  10
# Output : 1, 3, 5, 7, 9


def OddNumber(No):
    Result = []
    for i in range(1, No + 1):
        if(i % 2 != 0 ):
            Result.append(i)
    return Result

num = int(input("Enter a value : "))

Ret = OddNumber(num)

print("Output :", Ret)