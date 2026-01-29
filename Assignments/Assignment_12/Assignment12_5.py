# 5: Design a Python application that creates two threads named Thread1 and Thread2.
# Thread1 should display numbers from 1 to 50.
# Thread2 should display numbers from 50 to 1 in reverse order.
# Ensure that
# Thread2 starts execution only after Thread1 has completed.
# Use appropriate thread synchronization

import threading

def print_forward():
    
        for i in range(1,51):

                print(f"Thread from 1 to 50 : {i}")

def print_reverse():
    for i in range(50,0,-1):
        print(f"Thread from 50 to 1 : {i}")

Thread1 = threading.Thread(target=print_forward)
Thread2 = threading.Thread(target=print_reverse)

Thread1.start()
Thread1.join()

print("---------------------------------")

Thread2.start()
Thread2.join()