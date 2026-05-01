# Assignment No 46  Quetion no 7

# Write a python program using LinearRegression to train a regression model using the dataset below
#
#
#   -------------------------------
#   |  Study Hours       | Marks |
#   -------------------------------
#   |     1              | 50    |
#   |     2              | 55    |
#   |     3              | 60    |
#   |     4              | 65    |
#   |     5              | 70    |
#
# Program contain the :
#   - Train the model 
#   - Print the Coefficient 
#   - Print teh Intercept 
#




import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def LinearRegressionModelTrain():
    
    X = [1,2,3,4,5]
    Y = [50,55,60,65,70]
    
    mean_X = 0
    mean_Y = 0
    for  i in X :
        mean_X = i + mean_X
    mean_X = mean_X / len(X)
    print("Mean of X ",mean_X)
    
    for j in Y :
        mean_Y = j + mean_Y
    mean_Y = mean_Y / len(Y)
    print("Mean of Y : ", mean_Y)
    
    
    
    # m = (summ(x-X_bar) * (Y- Y_bar)) / (Summ(X- X_bar) **2 )
    
    numerator = 0
    denominator = 0
    
    feature_len = len(X)
    
    for i in range(feature_len):
        numerator = numerator + ((X[i] - mean_X) * (Y[i]- mean_Y))
        denominator = denominator + ((X[i] - mean_X) ** 2)
    
    m = numerator / denominator
    print("Slope(m) (Coefficient)  Will be the   : ",m) # coefficient 
    
    # intercept formula  (C inyercept )
    # c ​=yˉ​−m​xˉ 
    
    c = mean_Y -(m * mean_X)
    
    print("intercept of c is : ", c)
    
    
    
    # Y = mX + C

    
    
    
    



def main():
    LinearRegressionModelTrain()

if __name__ == "__main__":
    main()
