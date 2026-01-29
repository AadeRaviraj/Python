
# 3. Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6

def SumDigit(No):
    Sum = 0 
    while(No != 0 ):        
        Sum = Sum + No % 10 # get last digit and add
        No = No // 10  # remove last digit
    return Sum

def main():
    number = int(input("Enter A number "))

    Res1 = SumDigit(number)
    print("Result 1 :", Res1) 
    

if __name__ == "__main__":
    main()