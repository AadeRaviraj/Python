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


# 9. Create a new column:
# PerformanceIndex = (StudyHours * 2) + Attendance
# Train the model including this new feature.
# Does accuracy improve?



import pandas as pd  
from sklearn import tree
from sklearn.metrics import accuracy_score,confusion_matrix
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split


def accuracy_ScoreX(y_test,ypred): 
    correct = 0 
    wrongCount = 0
    for i in range (len(y_test)): 
        if y_test.iloc[i] == ypred[i]:
            correct += 1
        else:
            print("MissClasifed rows ")
            print(y_test.iloc[i])
            print(f"Actual row is : {y_test.iloc[i]} and Predicted row is : {ypred[i]}")
            wrongCount += 1
    
    print("Wrong count is ", wrongCount)
    accuracy = correct / len(y_test)
    return accuracy
    

def main():
    border = "-" * 80 
    # import csv data 
    fileName = "student_performance_ml.csv" 
    
    print("----------------------------- Load Data ---------------------------\n")
    df = pd.read_csv(fileName)
    # print(border) 
    
    df["PerformanceIndex"] = (df["StudyHours"]*2) + df["Attendance"]
    
    feature_column =[
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours",
        "PerformanceIndex"
    ]
    
    X = df[feature_column]
    Y = df["FinalResult"] 

    
    print(border)
    
        # splitting 
    X_train ,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size= 0.2,
        random_state= 10,

    ) 
    
    print(border) 
    
    print("---------------- Train Model -----------------")
    
    
    modelObj = tree.DecisionTreeClassifier()
    
    modelObj.fit(X_train,Y_train)        
    Ypred = modelObj.predict(X_test)
    
    # for i in Ypred:
    #     print("Predicted Answer :",i)
    
    # for j in Y_test:
    #     print("Expected Answer :",j)
        
        
    accuracy1 = accuracy_ScoreX(Y_test,Ypred)
    print("Accuracy --::",accuracy1 * 100)
    
    print(df.describe())
    
    # accuracy =accuracy_score(Y_test,Ypred)    
    # print("Accuracy of model is :",accuracy * 100)
    
    # importance = modelObj.feature_importances_    
    # print("importance feature ",importance )
    
    plt.figure(figsize=(12,7))
    plot_tree(modelObj, filled= True,feature_names=feature_column, class_names=["Fail","Pass"])
    plt.title("Trained model show")
    plt.show()

    

    

if __name__ == "__main__":
    main()
    
    