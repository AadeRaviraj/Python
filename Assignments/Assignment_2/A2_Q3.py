
# 3. Write a program which accepts one number and prints factorial of that number.
# Input: 5
# Output: 120


def Factorial(No):  # 5 * 4 * 3 * 2 * 1  = 120
    result = 1
    
    for i in range(1, No + 1):
        result =  result * i          
    return result

number  = int(input("Enter a number : "))

Ret = Factorial(number)

print("Output : ", Ret)