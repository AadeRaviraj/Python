# 1: Design a Python application that creates two threads named Prime and NonPrime.
# Both threads should accept a list of integers.
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non-prime numbers from the list.

import threading


def PrimeNumber(list1):
    newlist = []
    for No in list1:
        if No <= 1:
            continue
        isPrime = True
        i = 2 
        while(i * i <= No):
            if(No % i == 0):
                isPrime = False
                break
            i = i +1
            
        if  isPrime:
            newlist.append(No)
        
    print(f"Prime Numbers : {newlist}")
    

def NotPrimeNumber(list1):
    newlist = []
    for No in list1:
        if No <= 1:
            continue
        isPrime = True
        i = 2 
        while(i * i <= No):
            if(No % i == 0):
                isPrime = False
                break
            i = i +1
            
        if  isPrime:
            pass
        else:
            newlist.append(No)
        
    print(f"Not Prime : {newlist}")




list1 = [13, 5, 45, 7, 4, 56, 10, 34, 2, 5, 8]

Thread1 = threading.Thread(target=PrimeNumber,args=(list1,))
Thread2 = threading.Thread(target=NotPrimeNumber,args=(list1,))

Thread1.start()
Thread1.join()

Thread2.start()
Thread2.join()

