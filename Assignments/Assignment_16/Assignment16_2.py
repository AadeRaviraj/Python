# Q2) Display File Contents
# Problem Statement:
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
# Input:
# Demo.txt
# Expected Output:
# Display contents of Demo.txt on console.

import os 


fileName = input("Enter File Name : ")

fileExits = os.path.exists(fileName)

if fileExits == True:
    res= open(fileName,"r")
    data = res.read()
    print(data)
else:
    print("File does not exists")