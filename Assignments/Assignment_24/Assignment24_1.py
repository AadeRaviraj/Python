    ###################### Assignment - 40 #################
#     Dataset Description – Student Performance ML
# Dataset
# The dataset student_performance_ml.csv contains academic and behavioral information of
# students. The objective of this dataset is to predict whether a student will Pass (1) or Fail (0) based on various
# input features.
# Each row in the dataset represents one student, and each column represents a measurable factor that may
# influence academic performance.
# Features Description
# • StudyHours – Number of hours a student studies per day.
# • Attendance – Percentage of class attendance.
# • PreviousScore – Marks obtained in the previous examination.
# • AssignmentsCompleted – Number of assignments completed by the student.
# • SleepHours – Average number of hours the student sleeps per day.
# • FinalResult – Target variable (Output):
# ◦ 1 → Pass
# ◦ 0 → Fail

# Objective of the Dataset
# The goal is to:
# • Analyze how different factors affect student performance.
# • Build a Machine Learning model to predict whether a student will pass or fail.
# • Understand concepts such as training, testing, accuracy, confusion matrix, overfitting, and model
# evaluation.

 

# 1. After training the Decision Tree model, use:
# model.feature_importances_
# • Display importance score of each feature.
# • Which feature contributes the most in predicting FinalResult?
# • Which feature contributes the least?

import pandas as pd  
from sklearn import tree
from sklearn.metrics import accuracy_score,confusion_matrix
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def main():
    border = "=" * 80 
    # import csv data 
    fileName = "student_performance_ml.csv"
    
    ############################################################################
    # Step 1 : load data using pandas 
    ############################################################################
    
    print("----------------------------- Load Data ---------------------------\n")
    df = pd.read_csv(fileName)
    print(border)
    
    
    ############################################################################
    # Step 2 : Data Analysis 
    ############################################################################
    
    print("---------------------------  Data Analysis ------------------------\n")
    print("Shape of Database : ",df.shape)
    print("Columns Name : ",list(df.columns))
    print("is null values of Missing values per column :",df.isnull().sum())
    
    print(df.describe())
    
    print(border)
    
     
    feature_column =[
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]
    
    X = df[feature_column]
    Y = df["FinalResult"] 

    
    print(border)
     
        # splitting 
    X_train ,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size= 0.2,
        random_state= 42
    ) 
    
    print(border)
    #############################################################################
    # Step 5 : Train model  
    #############################################################################
    
    modelObj = tree.DecisionTreeClassifier()
    
    print("---------------- Train Model -----------------")
    
    modelObj.fit(X_train,Y_train)
    
    Ypred = modelObj.predict(X_test)
    
    print("Predicted Answer :",Ypred)
    print("Expected Answer :",Y_test)
    
    accuracy =accuracy_score(Y_test,Ypred)
    
    importance = modelObj.feature_importances_
    
    print("importance feature ",importance)
    
# most important feature is  StudyHours 
# and least one is PreviousScore
    

    

if __name__ == "__main__":
    main()
    
    
    
