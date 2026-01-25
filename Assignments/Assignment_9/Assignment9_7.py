# 7. Write a program which accept one number and display below pattern.
# Input: 5 
# Output: 1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5

num = int(input("Enter number : "))
for i in range(1, num+1):
    for j in range(1, num+1):
        print(j,end=" ")
    print()
