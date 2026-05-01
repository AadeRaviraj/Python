# These data are the results of a chemical analysis of wines grown in the same region in Italy
# but derived from three different cultivars. The analysis determined the quantities of 13
# constituents found in each of the three types of wines.
# Wine data set contains 13 features as


# 1) Alcohol
# 2) Malic acid
# 3) Ash
# 4) Alcalinity of ash
# 5) Magnesium
# 6) Total phenols
# 7) Flavanoids
# 8) Nonflavanoid phenols
# 9) Proanthocyanins
# 10)Color intensity
# 11)Hue
# 12)OD280/OD315 of diluted wines
# 13)Proline


# According to the above features wine can be classified as
# • Class 1
# • Class 2
# • Class 3

# We have to design Machine Learning application which uses Classification
# technique.

# Design machine learning application which follows below steps as

# Step 1:
# Get Data

# Step 2:
# Clean, Prepare and Manipulate data

# Step 3:
# Train Data

# Step 4:
# Test Data

# Step 5:
# Calculate Accuracy


import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


def LogisticRegressionModelTrain():
    
    Border = "- " * 40 
    
    print("Step 1 : Load the data from csv")
    print(Border)
    
    df = pd.read_csv("WinePredictor.csv")
    
    print("\n --- Some Data from csv : ---- \n")
    print(df.head())
    
    
    print(Border)
    
    print("\nStep 2 : Clean Prepare and manipulate teh data and remove unwanted columns  \n")
    
    print("Columns before delete : ",df.shape)
    
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"],inplace=True)
    
    print(Border)
    print("Columns after delete  : ", df.shape)
    print(Border)
    
    print("\n Step 3 : --- Check is any null values --- \n ")
    
    print(Border)
    print("Check if the any column contain null values ")
    print(Border) 
    print(df.isnull().sum())
    
    # Fill the  value  with the  mean value 
    
    df = df.fillna(df.mean())
    
    
    print(Border)
    
    print(" Step 4 : Split data to dependent and independent variable  ")
    
    print(Border)
    
    X = df.drop(columns="Class")
    Y = df['Class']
    
    print("Independent Variable (X) : ",X.shape)
    print("Dependent Variable (Y) : ",Y.shape)
    
    print(Border)
    
    print("Step 5 : Split Data into training and testing 80% for training 20% for testing ")
    
    print(Border)
    
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state= 23
    )
    
    scale = StandardScaler()
    # Scaling the feature 
    X_trainScale = scale.fit_transform(X_train)
    X_testScale = scale.transform(X_test)
    
    print("\n ---- Create the model ---- \n")
    
    model = LogisticRegression( max_iter=200)
    
    print("\n ---- Train the model ---- \n")
    
    model.fit(X_trainScale,Y_train)
    
    print("\n ---- Test the model ---- \n")
    
    Ypred = model.predict(X_testScale)
    
    # print("\n Predicted Values : \n", Ypred)
    
    # print("\n Expected Values : \n", Y_test)
    
    result = pd.DataFrame({
        "Actual Values : " :  Y_test.values,
        "Predicted Values ": Ypred
    })
    
    print(result)
    
    
    print("Accuracy Calculation : ")
    
    accuracy = accuracy_score(Y_test,Ypred)
    
    print("Accuracy : ",accuracy * 100  )
    




def main():
    LogisticRegressionModelTrain()

if __name__ == "__main__":
    main()
