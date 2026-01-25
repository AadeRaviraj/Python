# 2. Write a program which accepts radius of circle and prints area of circle.
# formula Area = pi * r*r

import math 

def AreaOfCircle(radius):
    Pi = 3.14
    # Area = math.pi  * radius * radius
    Area = Pi  * radius * radius
    return Area

radius = int(input("Enter radius :"))

Ret = AreaOfCircle(radius)
print("Output : ", Ret)