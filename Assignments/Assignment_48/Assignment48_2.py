# Write a python program that calculate the mean of a dataset using numpy for the following values :
#   [6,7,8,9,10,11,12]

import numpy as np 

X = [6,7,8,9,10,11,12]
X_mean = np.mean(X)
print("Mean of array :",X_mean)

# variance calculation 

# Formula of variance Variance = Σ (x - mean)² / N
v_= 0 
v_1 = 0
for i in X:
    # print(i)
    v_ = i - X_mean
    v_ = v_ **2
    v_1 += v_   # Addition of (X-mean )^2
variance = v_1 / len(X)

print("Variance of array : ", variance)

StandardDeviation = np.sqrt(variance)

print("Standard Deviation : ",StandardDeviation)