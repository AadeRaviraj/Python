# 1. Write a program which accepts one number and prints multiplication table of that number.
# Input: 4
# Output:
# 4 8 12 16 20 24 28 32 36 40



def Multiply(No):
    Result = []
    for i in range(1,11): 
        Result.append(i * No)
    return Result


number = int(input("Enter a number : "))

Res = Multiply(number) 

print(Res)




#----------------------------------------------------------

# for i in range(1,11):
#     print( "5","*",i,"=",i * number)
    
