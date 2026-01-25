# 1. Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
# Input: Number of elements: 6
# Input Elements: 13  5 45 7 4 56
# Output: 130

listSize = int(input("Number of element : "))

emptyList =  []
result = 0

for i in range(1, listSize + 1):
    inputElement = int(input("Enter element  : "))
    emptyList.append(inputElement)

print(emptyList)

for i in emptyList:
    result = result + i
print(result)
