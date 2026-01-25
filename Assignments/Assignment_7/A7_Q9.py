# 9. Write a lambda function using reduce() 
# which accepts a list of numbers and returns the product of all elements.

from functools import reduce

Reduce = lambda a , b : a * b

_Data = [2, 3, 5, 4]

result = reduce(Reduce, _Data)

print(result)