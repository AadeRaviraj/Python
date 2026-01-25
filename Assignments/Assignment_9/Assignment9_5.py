# 5. Write a program which accept one number for user and check whether number is prime or not.
# Input:
# 5
# Output: It is Prime Number

num = int(input("Enter a number : "))

isPrime = True 

if num  <= 1:
    isPrime = False
else:
    a = 2 
    while(a * a <= num):
        if(num % a == 0):
            isPrime = False
            break
        a = a +1
        
    
    
if isPrime:
    print("It is prime number")
else:
    print("It is not prime number")
            
    