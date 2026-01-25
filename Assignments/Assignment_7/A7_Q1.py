# 1. Write a lambda function 
# using map() which accepts a list of numbers and returns a list of squares of each number.


_Data = [2, 4, 3, 6, 8 , 9,5 ]

square = lambda a : a * a 

result = list(map(square, _Data))


print(result) #4, 16, 9, 36, 64, 81, 25
