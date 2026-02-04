# Q3) Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt. and copies all contents from the given file into Demo.txt.
# Input (Command Line):
# ABC.txt
# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import sys
import os  
def CopyFile():
    if len(sys.argv) == 2:
        name = sys.argv[1]
        if os.path.exists(name) == True:
            readobj = open(name,"r")
            data = readobj.read()
            readobj.close()

            if len(data) > 0 :
                print("Old File Data :",data)
                fileName = "Hello.txt"
                fObj = open(fileName, "w")
                fObj.write(data)                 
                print("Data Written Successfully")
                fObj.close()

                newfileObj = open(fileName, "r")
                newfileData = newfileObj.read()
                newfileObj.close()
                print("New File Data : ",newfileData) 
            else:
                print("File is empty...")
        else:
            print("File Does not exist...")
    else:
        print("Invalid arguments ....")


CopyFile()