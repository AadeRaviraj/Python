# 5. Write a program which accepts marks and displays grade.
# Condition Example:
# ≥75 Distinction
# ≥ 60 First Class
# ≥ 50 Second Class
# < 50 Fail

num = int(input("Enter marks "))

if num >= 75:
    print("Distinction")
elif(num >= 60):
    print("First class..")
elif(num >= 50):
    print("Second class")
else:
    print("fail")