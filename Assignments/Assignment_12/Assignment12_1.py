# 1: Design a Python application that creates two separate threads named Even and Odd.
# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module.
# Ensure proper thread creation and execution.

import threading

def evenNo():
    for i in range(1, 21):
        if i % 2 == 0 :
            print(f"Even Thread : {i}" )

def oddNo():
    for i in range(1,21):
        if i % 2 != 0 :
            print(f"Odd Thread : {i}" )

T1 = threading.Thread(target= evenNo,name= "Even")
 
T2 = threading.Thread(target= oddNo,  name = "Odd")
 
T1.start()
T2.start()
T1.join()
T2.join()