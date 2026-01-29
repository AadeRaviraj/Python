# 1. Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input: 4
# Output: 16
# Input: 6
# Output: 64

power = lambda res: 2 ** res

num  = int(input())
result = power(num)

print(result)
