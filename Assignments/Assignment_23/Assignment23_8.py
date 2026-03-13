#     Dataset Description – Student Performance ML Dataset

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
# • Understand concepts such as training, testing, accuracy, confusion matrix, overfitting, and model  evaluation.


# 8. Write a single structured Python program that performs:
# 1. Dataset loading
# 2. Data analysis
# 3. Visualization
# 4. Train-test split
# 5. Model training
# 6. Prediction
# 7. Accuracy calculation
# 8. Confusion matrix generation
# 9. Final conclusion
# Your code should include proper comments explaining each step.

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
    
    
    ############################################################################
    # Step 3 : Data Visualization 
    ############################################################################
    feature_column =[
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]
    
    X = df[feature_column]
    Y = df["FinalResult"]
    print("-------------------------- Data Visualization --------------------\n")
    
    plt.figure(figsize=(8,7))
    plt.scatter(df["StudyHours"],df["FinalResult"])
    plt.xlabel("Study Hours")
    plt.ylabel("Final Result ")
    plt.show()
    
    #############################################################################
    # Step 4 : Train Test Split 
    #############################################################################
    
    print(border)
     
        # splitting 
    X_train ,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size= 0.2,
        random_state= 42
    )
    print("--------------------- Data Splitting -----------------")
    
    
    print("X - Independent  ", X.shape) # (30,5)
    print("Y - Dependent ",Y.shape)  # (30,)

    print("X_train : ",X_train.shape)  # (24,5)
    print("X_test : ",X_test.shape)  # (6,5)

    print("Y_train : ",Y_train.shape)  # (24,1)
    print("Y_test : ",Y_test.shape)  # (6,)
    
    print(border)
    #############################################################################
    # Step 5 : Train model  
    #############################################################################
    modelObj = tree.DecisionTreeClassifier()
    print("---------------- Train Model -----------------")
    
    modelObj.fit(X_train,Y_train)
    
    
    #############################################################################
    # Step 6 : Prediction 
    #############################################################################
    Y_pred = modelObj.predict(X_test)
    print("Expected Answer : ",Y_test)
    print("Predicted Answer",Y_pred)
    
    ##############################################################################
    # Step 7 : Accuracy  calculation
    ##############################################################################
    print(border)
    print("-------------------------------- Accurate Result ----------------------------")
    accurate = accuracy_score(Y_pred,Y_test)
    
    print("Accurate Result  : ",accurate * 100)
    
    ##############################################################################
    # Step 9 : Confusion matrix generation
    ##############################################################################
    print("-------------------------------- Confusion Matrix ---------------------------")
    confusionMatrix = confusion_matrix(Y_pred,Y_test)
    print("Confusion Matrix : ",confusionMatrix)
    
    

    

if __name__ == "__main__":
    main()
    
    