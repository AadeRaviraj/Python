
# 6. Write a program which accept number from user and check whether that number is positive or negative or zero.
# Input: 11
# Input: -8
# Input: 0
# Output: Positive Number
# Output: Negative Number
# Output: Zero

num = int(input("Enter A number : "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
elif num == 0:
    print("Zero number ")