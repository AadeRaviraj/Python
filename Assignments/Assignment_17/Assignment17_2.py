# Q2) Count Words in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input:
# Demo.txt
# Expected Output:
# Total number of words in Demo.txt.




def CountWord():
    FileName = input("Enter File Name : ")
        
    fobj = open(FileName, "r")
    
    data = fobj.read()
    word = data.split()
    iCount = 0 
    for i in word:
        iCount = iCount + 1
        
    print(word) 
    print(iCount)  


CountWord()