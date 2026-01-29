# 3: Design a Python application that creates two threads named EvenList and OddList.
# Both threads should accept a list of integers as input.
# The EvenList thread should: 
# Extract all even elements from the list.
# Calculate and display their sum.
# The OddList thread should:
# Extract all odd elements from the list.
# Calculate and display their sum.
# Threads should run concurrently.

import threading

def EvenSum(No):
    sum = 0
    for i in No:
        if i % 2 ==0 :
            sum = sum +i 
    print(f"Even Sum {sum}")

def OddSum(No):
    sum = 0
    for i in No:
        if i % 2 != 0 :
            sum = sum +i 
    print(f"Odd Sum {sum}")

Data = [1,2,3,4,5,6,7,8,9,10]

T1 = threading.Thread(target= EvenSum, args=(Data,), name = "EvenList")
T2 = threading.Thread(target= OddSum, args=(Data,), name = "OddList ")

T1.start()
T2.start()

T1.join()
T2.join()

print("End of program....")
