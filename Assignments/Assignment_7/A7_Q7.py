# 7. Write a lambda function  using filter() 
# which accepts a list of strings and returns a list of strings having length greater than 5.

max_length = lambda _strlist : len( _strlist) > 5

_strData = ["Mahadev","Krishna", "Shiv", "Shriram", "Ganesh", "Vishnu", "Hanuman","Vayu"]


result = list(filter(max_length, _strData))

print(result)