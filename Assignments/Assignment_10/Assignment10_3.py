
# 3. Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
# Input: Number of elements: 4 
# Input Elements: 13 5 45 7
# Output: 5


listSize = int(input("Enter size of list : "))

emptyList = []
for i in range(1, listSize + 1):
    element = int(input("Enter element : "))
    emptyList.append(element)
print(emptyList)


minValue = emptyList[0]

for i in emptyList:
    if i < minValue: 
        minValue = i
        
        
print("Output : ",minValue)
    