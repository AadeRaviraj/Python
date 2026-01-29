# 3: Design a Python application where multiple threads update a shared variable.
# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution.

import threading

icnt = 0

lObj = threading.Lock()

def upgrade():
    global icnt    
    for i in range(10):
        with lObj:
            icnt = icnt+1
    
Thread1 = threading.Thread(target=upgrade)

Thread2 = threading.Thread(target=upgrade)

Thread1.start()
Thread2.start()

Thread1.join()
Thread2.join()

print("Value of icnt :", icnt)