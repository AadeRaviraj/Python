# 2: Design a Python application that creates two threads.
# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.

import threading

def maxNumber(data):
    num = 0
    for i in data:
        if i > num:
            num = i
    print(num)

def minNumber(data):
    num = data[0]
    for i in data:

        if i < num:
            num = i
    print(num)

listsize = int(input("Enter size of list : "))

Data = []
for i in range(listsize):
    element = int(input("Enter element : "))
    Data.append(element)
print(Data)

Thread1 = threading.Thread(target= minNumber, args=(Data,))

Thread2 = threading.Thread(target= maxNumber, args=(Data,))

Thread1.start()
Thread1.join()
Thread2.start()
Thread2.join()

