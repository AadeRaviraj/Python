# 4. Write a program which accept N numbers from user and store it into List. 
# Accept one another number from user and return frequency of that number from List.
# Input: Number of elements: 11
# Input Elements: 13  5  45 7  4  56  5  34  2  5 65
# Element to search: 5 
# Output: 3

listSize = int(input("Enter size of list : "))

list1 = []
for i in range(1, listSize + 1):
    element = int(input("Enter element : "))
    list1.append(element)
print(list1)

searElement = int(input("Element to search : "))

result = 0

for i in list1:
    if i == searElement:
        result = result + 1

print(result)