# write a python program to predict the marks for 6 study hour and display teh predicted value 



import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def LinearRegressionModelTrain():
    
    data = pd.DataFrame({
        'Hours': [1, 2, 3, 4, 5],
        'Marks': [50, 55, 60, 65, 70]
    })
    X = data[["Hours"]]
    Y = data[["Marks"]]
    print("Shape of Independent variables :",X.shape)
    print("Shape of Dependent variable ",Y.shape)
    
    

    print("Create & train the model ")
    
    model = LinearRegression()
    
    model.fit(X,Y) 
    
    # Predict for 6 hours using DataFrame
    new_data = pd.DataFrame({'Hours': [6]})
    Ypred = model.predict(new_data)    
    print("Predicted values for the 6 Hour is : ",Ypred)
    
    
    

    
    
    
    



def main():
    LinearRegressionModelTrain()

if __name__ == "__main__":
    main()
