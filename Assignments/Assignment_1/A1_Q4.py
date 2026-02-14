# 4. Write a program which accepts one number and prints cube of that number.


def CubeResult(No):
    return No * No * No


No = int(input("Enter a number :"))

Result = CubeResult(No)
print("Entered number cube will be :", Result)