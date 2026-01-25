# 7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
# Input: 8
# Output: False
# Input: 25
# Output: True

def ChkDivisible5(no):
    if no % 5 == 0 :
        return True
    else:
        return False

num = int(input("Enter number : "))

result = ChkDivisible5(num)
print(result)