# Q1) Check File Exists in Current Directory
# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
# Input:
# Demo.txt
# Expected Output:
# Display whether Demo.txt exists or not.

import os


fileName = input("Enter File name :")

ret = os.path.exists(fileName)

if (ret == True):
    print(f"{fileName} This  exist in current directory")
else:
    print(f"{fileName} this file does not exist ")