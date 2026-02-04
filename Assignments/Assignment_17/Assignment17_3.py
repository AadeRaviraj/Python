# Q3) Display File Line by Line
# Problem Statement:
# Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.
# Input:
# Demo.txt
# Expected Output:
# Display each line of Demo.txt one by one.

FileName = input("Enter File name : ")

fobj = open(FileName, "r")
data = fobj.read()
print(data)
