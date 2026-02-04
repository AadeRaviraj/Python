# Q4) Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of both files.
# If both files contain the same contents, display Success
# Otherwise display Failure

# Input (Command Line): Demo.txt Hello.txt
# Expected Output: Success OR Failure



import sys
def CopyFile():
    if len(sys.argv) == 3:
        name1 = sys.argv[1]
        name2 = sys.argv[2]
        readobj1 = open(name1,"r")
        data1 = readobj1.read()
        readobj1.close()
        
        readobj2 = open(name2,"r")
        data2 = readobj2.read()
        readobj2.close()
        
        if data1 == data2:
            print("Success...")
        else:
            print("Failure...")
            

    else:
        print("Invalid arguments ....")


CopyFile()