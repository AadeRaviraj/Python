# 2. Write a program which accepts one number and prints its factors.
# Input: 12
# Output: 1234 6 12

def Factors(No):
    Result = []
    for i in range(1, No+1):        
        if(No % i == 0 ):
            Result.append(i)
    return  Result


number = int(input("Enter a number : "))
Result = Factors(number)
print(list(Result))