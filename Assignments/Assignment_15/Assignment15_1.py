# 1: Write a Python program to implement a class named BookStore with the following specifications:
# The class should contain two instance variables:
# Name (Book Name)
# Author (Book Author)
# The class should contain one class variable:
# NoOf Books (initialize it to 0)
# Define a constructor (init) that accepts Name and Author and initializes instance variables.
# Inside the constructor, increment the class variable NoOf Books by 1 whenever a new object is created.
# Implement an instance method:
# Display() should display book details in the format:
# <BookName> by <Author>. No of books: <NoOfBooks>
# Example usage:
# Obj1 = BookStore ("Linux System Programming", "Robert Love")
# Objl. Display()
# # Linux System Programming by Robert Love. No of
# books: 1
# Obj2 = BookStore("C Programming", "Dennis Ritchie")
# Obj2.Display()
# # C Programming by Dennis Ritchie. No of books: 2

class BookStore :
    NoOfBooks = 0
    def __init__(self, A, B):
        self.Name =  A
        self.Author =  B
        BookStore.NoOfBooks = BookStore.NoOfBooks +1
    
    
    def Display(self):
        print(self.Name , self.Author)
        print("No Of Books : ",BookStore.NoOfBooks)

obj1 = BookStore("Linux System Programming ", "Robert Love")
obj1.Display()

Obj2 = BookStore("C Programming ", "Dennis Ritchie")
Obj2.Display()

Obj3 = BookStore("Python Programming ", "Reema Thareja ")
Obj3.Display()
        
        