# 2. Write a program which accept one number and display below pattern.
# Input:
# 5
# Output: * * * * *
#         * * * * *
#         * * * * *
#         * * * * *
#         * * * * *

no = int(input("enter a number : "))

for i in range(1, no + 1):
    for j in range(1, no + 1):
        print("*", end=" ")
    print("")