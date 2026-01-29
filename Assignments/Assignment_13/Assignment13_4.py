# 4: Design a Python application that creates two threads.
# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display them.

import threading

result1 = []
result2 = []
def SumElement(data):
    sum = 0 
    for i in data:
        sum = sum + i
    result1.append(sum)

def ProductElement(data):
    sum = 1
    for i in data:
        sum =  sum * i 
    # print(sum)
    result2.append(sum)

listsize = int(input("Enter size of list : "))

Data = []
for i in range(listsize):
    element = int(input("Enter element : "))
    Data.append(element)
print(Data)

T1 = threading.Thread(target=SumElement, args=(Data,))

T2 = threading.Thread(target=ProductElement, args=(Data,))

T1.start()
T2.start()

T1.join()
T2.join()

print("Sum of all element : ", result1[0])

print("Product of all element : ", result2[0])
