# 2. Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
# Input: Number of elements:  7
# Input Elements: 13    5  45  7  4  56 34
# Output: 56

listSize = int(input("Enter size of list : "))

emptyList = []
for i in range(1, listSize + 1):
    element = int(input("Enter element : "))
    emptyList.append(element)
print(emptyList)


maxvalue = 0
for i in emptyList:
    if i > maxvalue:
        maxvalue = i
        
        
print("Output : ",maxvalue)
    