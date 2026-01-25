
# 1. Write a program which accepts one number and checks whether it is prime or not.
# Input: 11
# Output: Prime Number

def CheckPrime(No):
    isPrime = True
    
    if No <= 1:
        return False
    
    i = 2 
    while(i * i <= No):
        if(No % i == 0):
            isPrime = False
            break
        i = i +1
    return isPrime
    
number = int(input("Enter a number : "))

if(CheckPrime(number) == True):
    print("Prime Number..")
else:
    print("Not A Prime Number")