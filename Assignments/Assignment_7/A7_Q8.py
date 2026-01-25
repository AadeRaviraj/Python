# 8. Write a lambda function using filter() 
# which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.


Divide_3_5 = lambda no : no % 3 == 0 and no % 5 == 0 


_Data = [2, 4, 3, 6, 8 , 9,5 , 15]

Result =list(filter(Divide_3_5 , _Data)) 
print(Result)

