# 2: Write a Python program to implement a class named BankAccount with the following requirements:
# The class should contain two instance variables:
# Name (Account holder name)
# Amount (Account balance)
# The class should contain one class variable:
#  ROI (Rate of Interest), initialized to 10.5
# Define a constructor (_init ) that accepts Name and initial Amount.
# Implement the following instance methods:
# Display()- displays account holder name and current balance
# Deposit() accepts an amount from the user and adds it to balance
# Withdraw() accepts an amount from the user and subtracts it from balance 
# (Ensure withdrawal is allowed only if sufficient balance exists)
# CalculateInterest() calculates and returns interest using formula: Interest = (Amount ROI) / 100
# Create multiple objects and demonstrate all methods.

class BankAccount :
    ROI = 10.5
    
    def __init__(self, name, amt):
        self.Name = name
        self.Amount = amt
    
    def Display(self):
        print(f"Your name is : {self.Name} and your current balance is : {self.Amount}")
    
    def Deposit(self):
        amount = int(input("Enter Your amount: "))
        self.Amount = self.Amount + amount
        print("Your Current balance is : ", self.Amount)
        
    def Withdraw(self):
        userAmount = int(input("Enter Withdrawn Amount : "))
        if  self.Amount >=  userAmount:
            self.Amount = self.Amount - userAmount
            print(f"You Withdrawn {userAmount} And Your Current Balance is : {self.Amount} ")
        else:
            print("You have insufficient balance.. ")
    
    def CalculateInterest(self):
        interest  =  self.Amount * BankAccount.ROI / 100
        print(f"Your Interest Amount will be the {interest}")
        print()
        print("-"* 20)

Obj1 = BankAccount("Raviraj Aade", 10)
Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
Obj1.CalculateInterest()

Obj1 = BankAccount("Arjun", 10)
Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
Obj1.CalculateInterest()

Obj2 = BankAccount("Rutvik", 10)
Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()
Obj2.CalculateInterest()


Obj3 = BankAccount("Vikas", 10)
Obj3.Display()
Obj3.Deposit()
Obj3.Withdraw()
Obj3.CalculateInterest()