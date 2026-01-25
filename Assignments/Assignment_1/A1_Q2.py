# 2. Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
# 
# Input: 10 20
# Output: 20 is greater



def ChkGreater(Value1, Value2):
    if Value1 > Value2:
        print(Value1, "Is greater..")
    else:
        print(Value2, "Is greater...")


input1, input2 = input().split(",")
# input2 = int(input("Enter second number : "))

input1 = int(input1)
input2 = int(input2)
ChkGreater(input1,input2)