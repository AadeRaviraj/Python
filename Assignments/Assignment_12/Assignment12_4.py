# 4: Design a Python application that creates three threads named Small, Capital, and Digits.
# All threads should accept a string as input.
# The Small thread should count and display the number of lowercase characters.
# The Capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric digits.
# Each thread must also display:
# 0 Thread ID
# Thread Name  


import threading

VarUpper = []
VarLower = []
VarNUmber = []
    
def UpperChar(Uinput):
    for i in Uinput:
        if i.isupper():
            VarUpper.append(i)
    print(f"Upper character : {VarUpper}")

def LowerChar(Uinput):
    for i in Uinput:
        if i.islower():
            VarLower.append(i)
    print(f"Lower character : {VarLower}")
    
def  NumberChar(Uinput):
    for i in Uinput:
        if i.isdigit():
            VarNUmber.append(i)
    print(f"NUmbers  : {VarNUmber}")


input_ = "Python3IsFUN2025"

SmallThread  = threading.Thread(target=LowerChar, args=(input_,))
CapitalThread = threading.Thread(target=UpperChar, args=(input_,))
DigitsThread = threading.Thread(target=NumberChar, args=(input_,))

SmallThread.start() 
CapitalThread.start()
DigitsThread.start()

SmallThread.join()
CapitalThread.join()
DigitsThread.join()

print("Exiting program.....")
