# Q5) Search a Word in File
# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Display whether the word Marvellous is found in Demo. txt or not


FirstFilename = input("Enter File name : ")


fobj1 = open(FirstFilename, "r")

File1Data = fobj1.read()

Word = input("Enter Word : ")

if Word in File1Data:
    print(f"The Word {Word} is found in this file")
else:    
    print(f'The Word "{Word}" is not-found in this file')