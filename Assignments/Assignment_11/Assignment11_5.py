# 5. Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all prime numbers. Map function will multiply each number by 2. 
# Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
# Input List = [2, 70, 11, 10, 17, 23, 31, 77] 
# List after filter = [2, 11, 17, 23, 31] List after map [4, 22, 34, 46, 62] Output of reduce = 62


from functools import reduce

listSize = int(input("Enter Size of list : "))

Data = []
for i in range( listSize):
    num = int(input("Enter element : "))
    Data.append(num)
print(Data)

def primeNumber(no):    
    if no <= 1:
        return False
    i = 2     
    while i * i <= no:
        if no % i == 0:
            return False
        i = i +1 
    return True

Multiply = lambda a : a * 2

MaxValue = lambda a , b: a if  a>b else b

Fdata = list(filter(primeNumber, Data))
print("List After Filter ",Fdata)

MData = list(map(Multiply, Fdata))
print("List After Map : ", MData)

ReduceData = reduce(MaxValue, MData)
print("List After Reduce : ", ReduceData)

