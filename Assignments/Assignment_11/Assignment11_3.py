# 3. Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
# Map function will increase each number by 10. Reduce will return product of all that numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70] List after filter = [76, 89, 86, 90, 70] 
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000


from functools import reduce

listSize = int(input("Enter Size of list : "))

Data = []
for i in range( listSize):
    num = int(input("Enter element : "))
    Data.append(num)
print(Data)

filterData = lambda no : no >= 70 and no <= 90

mapData = lambda no : no + 10

reduceData = lambda No1 , No2 : No1 * No2

FData = list(filter(filterData, Data))
print("Filter data : ",FData)

MData = list(map(mapData, FData))
print("Map Data : ", MData)

RData = reduce(reduceData,MData)
print("Reduce Data : ", RData)




