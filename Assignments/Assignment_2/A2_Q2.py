
# 2. Write a program which accepts one number and prints sum of first N natural numbers.
# Input: 5
# Output: 15

def SumOfNNumber(No):
    Sum = 0 
    
    for i in range(1,No+1):
        Sum = Sum + i
    return Sum

number = int(input("Enter a number : "))

Res = SumOfNNumber(number)

print("Output : ",Res)