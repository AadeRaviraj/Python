# 4. Write a lambda function 
# using reduce() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

_Data = [2, 4, 3, 6, 8 , 9,5 ]

add = lambda No1 , No2: No1 + No2

Result = reduce(add, _Data)

print(Result)