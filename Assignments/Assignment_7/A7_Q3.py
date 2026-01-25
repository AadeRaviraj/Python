# 3. Write a lambda function 
# using filter() which accepts a list of numbers and returns a list of odd numbers.

_Data = [2,3,4, 5, 6, 8, 7,1 ,9, 10, 11, 12, 13, 24, 25 ]

EvenNumber = lambda No : No % 2 != 0 

Result = list(filter(EvenNumber, _Data))
print(Result)
