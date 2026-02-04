# Q4) Copy File Contents into Another File
# Problem Statement:
# Write a program which accepts two file names from the user.
# First file is an existing file
# Second file is a new file
# Copy all contents from the first file into the second file.
# Input:
# ABC.txt Demo.txt
# Expected Output:
# Contents of ABC.txt copied into Demo.txt.

FirstFilename = input("Enter Existing(First) File name : ")


fobj1 = open(FirstFilename, "r")

File1Data = fobj1.read()

SecondFilename = input("Enter Second File name : ")

fobj2 = open(SecondFilename,"w")
fobj2.write(File1Data)

fobj1.close()
fobj2.close()

print("Second file data copied successfully")
f2Data = open(SecondFilename,"r")
f2 = f2Data.read()
f2Data.close()
print("File 2 Data : ", f2)


