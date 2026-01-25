#2305843008139952128

num = 2305843008139952128

Ans = 0
for i in range(1,num):
    print("-",i)
    if num % i == 0 :
        Ans = Ans + i
        print("&",Ans)

if Ans == num:
    print("It is perfect number.. ")
else:
    print("Not A perfect number..")