
# 4. Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321

def ReverseNumber(No):
    Lastnum = 0 
    
    Ans = 0
    if No == 0 :
        return  0 
    while (No > 0):
        Lastnum = No % 10  # store last number        
        Ans = Ans * 10 + Lastnum        
        No = No // 10 # remove last number 
    
    return Ans

number = int(input("Enter a number :"))

Ret  = ReverseNumber(number)

print(Ret)