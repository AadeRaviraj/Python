# 5. Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. 
# Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum.
# Name of the function from main python file should be ListPrime().
# Input: Number of elements: 11
# Input Elements: 13  5  45  7  4  56  10 34  2  5  8
# Output: 54 (13+5+7+2 + 5)

from Marvellousnum import ChkPrime


def ListPrime(No):
    Result = []
    sum = 0
    for i in No:
        Result = Result + ChkPrime(i)
    
    for j in Result:
        sum = sum + j
    return Result


listSize = int(input("Enter size of list : "))

list1 = []
for i in range(1, listSize + 1):
    element = int(input("Enter element : "))
    list1.append(element)

res = ListPrime(list1)

ResultSum = 0
for i in res: 
    ResultSum = ResultSum + i
print(res)

print("Output : ",ResultSum)


