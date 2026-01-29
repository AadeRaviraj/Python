
# 2: Design a Python application that creates two threads named EvenFactor and OddFactor.
# Both threads should accept one integer number as a parameter.
# The EvenFactor thread should: Identify all even factors of the given number.
# Calculate and display the sum of even factors.
# The OddFactor thread should: Identify all odd factors of the given number.
# Calculate and display the sum of odd factors.
# After both threads complete execution, the main thread should display the message: "Exit from main"

import threading 

def EvenFactor(No):
    Sumeven = 0
    for i in range(1 , No+ 1):
        if No % i == 0 and i % 2 == 0 :
 
            Sumeven = Sumeven + i
    print(f"Sum of Even Factor :{Sumeven}")

def OddFactor(No):
    SumOdd = 0
    for i in range(1 , No+ 1):
        if   No % i == 0 and i % 2 != 0:
            SumOdd = SumOdd + i
 
    print(f"Sum of Odd Factor :{SumOdd}")

    
def main():
    
    T1 = threading.Thread(target= EvenFactor, args=(12,))
    T2 = threading.Thread(target= OddFactor, args=(12,))
    
    T1.start()
    T2.start()
    
    T1.join()
    T2.join()
    print("Exit from main ")


if __name__ == "__main__":
    main()