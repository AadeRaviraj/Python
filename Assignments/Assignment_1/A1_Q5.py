# 5. Write a program which accepts one number and checks whether it is divisible by 3 and 5
# Input: 15
# Output: Divisible by 3 and 5


uiNo = int(input("Enter a number : "))


if (uiNo % 3 == 0 and uiNo % 5 == 0):
    print("Divisible by 3 and 5 ")
else:
    print("Not divisible by 3 and 5")
    

