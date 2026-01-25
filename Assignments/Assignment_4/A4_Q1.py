# 1. Write a program which accepts one character and checks whether it is vowel or consonant.
# Input: a
# Output: Vowel

vowels = ['A','E','I','O','U','a','e','i','o','u']

Chars = input("Input : ")

isVowel = False 
if len(Chars) == 1:
    for  i in vowels:
        if Chars == i :
            isVowel = True
            break
        else:
            isVowel = False
        
    if isVowel :
        print("Vowel...")
    else:
        print("Not vowel...")
else:
    print("Enter only one value...")