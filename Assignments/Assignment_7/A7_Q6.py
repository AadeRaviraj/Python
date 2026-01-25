# 6. Write a lambda function 
# using reduce() which accepts a list of numbers and returns the minimum element.

from functools import reduce

min_value = lambda no1 , no2 : no1 if no1< no2 else no2

_Data = [2, 4, 3, 6, 8 , 9,5,50 ]

Result = reduce(min_value, _Data)

print(Result)