# 1. Write a program which accepts length and width of rectangle and prints area.

def LengthWidth(No1, No2):
    return No1 * No2


length = int(input("Enter Length  : "))

width = int(input("Enter Width  : "))

Rectangle = LengthWidth(length, width)

print("Rectangle : ",Rectangle)