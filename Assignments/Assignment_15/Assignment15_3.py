# 3: Write a Python program to implement a class named Numbers with the following specifications:
# The class should contain one instance variable:
# Value
# Define a constructor (init) that accepts a number from the user and initializes Value.
# Implement the following instance methods:
# ChkPrime() returns True if the number is prime, otherwise returns False
# ChkPerfect() returns True if the number is perfect, otherwise returns False
# 0 Factors() displays all factors of the number
# SumFactors() returns the sum of all factors
# (You may use this method as a helper in ChkPerfect() if required)
# Create multiple objects and call all methods.

class Numbers:
    def __init__(self, a):
        self.Value = a
    
    def ChkPrime(self):
        isPrime = True 
        if self.Value <= 0:
            return False
        i = 2
        while i * i <= self.Value:
            if self.Value % i  == 0 :
                isPrime=  False
                break
            i = i +1
        
        if isPrime:
            print("It is Prime number")
        else:
            print("It is Not prime number ")
            
        
    def ChkPerfect(self):
        ans = 0
        
        for i in range(1, self.Value):
            if self.Value %  i ==0 :
                ans = ans + i
        if ans ==self.Value:
            print("It is perfect number")
        else:
            print("it is not perfect number ")
        
    def Factors(self):
        result = []
        
        for i in range(1, self.Value):
            if self.Value % i == 0:
                result.append(i)
        print("Factors of entered number : ", result)
    
    def SumFactors(self):
        ans =0 
        for i in range(1, self.Value):
            if self.Value % i == 0:
                ans =ans + i
        print("Sum of Factors  : ", ans)
        print()

Obj1 = Numbers(10)
Obj1.ChkPrime()
Obj1.ChkPerfect()
Obj1.Factors()
Obj1.SumFactors()

Obj2 = Numbers(6)
Obj2.ChkPrime()
Obj2.ChkPerfect()
Obj2.Factors()
Obj2.SumFactors()

Obj3 = Numbers(3)
Obj3.ChkPrime()
Obj3.ChkPerfect()
Obj3.Factors()
Obj3.SumFactors()