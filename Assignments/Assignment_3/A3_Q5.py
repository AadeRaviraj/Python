# 5. Write a program which accepts one number and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome

def palindrome(No):
    
    Ans = No
    lastnum = 0
    RevValue = 0 
    while (No > 0 ):
        lastnum = No % 10 # Store  last number in Variable = lastnum
        RevValue = RevValue * 10 + lastnum
        No = No // 10 # Remove  last num
    if(RevValue == Ans ):
        return True 


number = int(input("Enter a number : "))

if(palindrome(number) == True):
    print("it is palindrome")
else :
    print("Not a palindrome")