# Q1) Count Lines in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input:
# Demo.txt
# Expected Output:
# Total number of lines in Demo.txt.


def CountLines():
    FileName = input("Enter File Name : ")
    fobj = open(FileName, "r")

    data = fobj.read()

    lines = data.count("\n")
    lines += 1 
    print(lines) 


CountLines()
