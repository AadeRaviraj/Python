# Q5) Frequency of a String in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Count how many times "Marvellous" appears in Demo.txt.

def CountFreq():
    FileName = input("Enter File Name : ")
    TextName = input("Enter Text Name Want search : ")
    
    fobj = open(FileName, "r")
    
    data = fobj.read()
    word = data.count(TextName)
    print(word)   


CountFreq()

