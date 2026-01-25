# 3. Write a program which accepts one number and checks whether it is perfect number or not.
# Input: 6
# Output: Perfect Number


num = int(input("Enter a number : "))

Ans = 0
for i in range(1,num):
    if num % i == 0 :
        Ans = Ans + i

if Ans == num:
    print("It is perfect number.. ")
else:
    print("Not A perfect number..")