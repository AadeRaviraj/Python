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


# 4. Create a new DataFrame with details of 5 new students.
# Use the trained model to predict their results.
# Display predictions clearly.


# | StudyHours | Attendance | PreviousScore | AssignmentsCompleted | SleepHours |
# | ---------- | ---------- | ------------- | -------------------- | ---------- |
# | 4.5        | 75         | 55            | 5                    | 6          |
# | 6          | 85         | 70            | 7                    | 7          |
# | 2.5        | 60         | 45            | 3                    | 5          |
# | 7          | 90         | 80            | 8                    | 8          |
# | 5.5        | 82         | 65            | 6                    | 7          |




import pandas as pd  
from sklearn import tree
from sklearn.metrics import accuracy_score,confusion_matrix
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def main():
    border = "-" * 80 
    # import csv data 
    fileName = "student_performance_ml.csv" 
    
    print("----------------------------- Load Data ---------------------------\n")
    df = pd.read_csv(fileName)
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
        random_state= 42,
        shuffle= True
    ) 
    
    print(border) 
    print("---------------- Train Model -----------------")
    
    
    modelObj = tree.DecisionTreeClassifier()
    
    modelObj.fit(X_train,Y_train)        
    Ypred = modelObj.predict(X_test)
    
    # print("Predicted Answer :",Ypred)
    # print("Expected Answer :",Y_test)
    
    accuracy =accuracy_score(Y_test,Ypred)    
    print("Accuracy of model is :",accuracy * 100)
    
    # importance = modelObj.feature_importances_    
    # print("importance feature ",importance )
    # print(df)
    
    print(border)
    
    
    print("Predict teh new records on trained model ")
    new_students = [
        {"StudyHours": 4.5, "Attendance": 75, "PreviousScore": 55, "AssignmentsCompleted": 5, "SleepHours": 6},
        {"StudyHours": 6.0, "Attendance": 85, "PreviousScore": 70, "AssignmentsCompleted": 7, "SleepHours": 7},
        {"StudyHours": 2.5, "Attendance": 60, "PreviousScore": 45, "AssignmentsCompleted": 3, "SleepHours": 5},
        {"StudyHours": 7.0, "Attendance": 90, "PreviousScore": 80, "AssignmentsCompleted": 8, "SleepHours": 8},
        {"StudyHours": 5.5, "Attendance": 82, "PreviousScore": 65, "AssignmentsCompleted": 6, "SleepHours": 7}
    ]

    df_new = pd.DataFrame(new_students)
    

    
    newprediction = modelObj.predict(df_new)
    df_new["FinalResult_predicted"] = newprediction
    print(df_new)

    
    

if __name__ == "__main__":
    main()
    
    
    
