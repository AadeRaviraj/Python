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


# 7. Use the trained model to predict result for a student with:
# • StudyHours = 6
# • Attendance = 85
# • PreviousScore = 66 
# • AssignmentsCompleted = 7
# • SleepHours = 7
# Will the student Pass or Fail? 

from sklearn import tree
import pandas as pd 
from sklearn.model_selection import train_test_split

from sklearn.metrics import     accuracy_score

def main():
    border = "*" * 50
    fileName = "student_performance_ml.csv"
    
    df = pd.read_csv(fileName) 
    modelObj = tree.DecisionTreeClassifier()

    print("Shape of Data Frame : ",df.shape)
    
    feature_column1 =[
    "StudyHours" ,
    "Attendance" ,
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours" 
    ]

    X = df[feature_column1]
    Y = df["FinalResult"]
    
    X_train, X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size= 0.2,
        random_state= 42
    )
    
    modelObj.fit(X_train,Y_train)
    
    Ypred = modelObj.predict(X_test)
    
    print("Predicted Answer :",Ypred)
    print("Expected Answer :",Y_test)
    
    accuracy =accuracy_score(Y_test,Ypred)
    print("Accurate Result is : ", accuracy * 100)
    
    print(border)
    
    
    feature_column ={
    "StudyHours" :7,
    "Attendance" : 60,
    "PreviousScore" : 50,
    "AssignmentsCompleted" : 6,
    "SleepHours" :7
    }
    df2 = pd.DataFrame([feature_column])
    
    
    print(df2)
    
    newDataPred = modelObj.predict(df2)
    print("New Data Predicted Result : ",newDataPred)
    
    if newDataPred[0] == 1:
        print("Student Will Pass ")
    else:
        print("Student Will fail ")




if __name__ == "__main__":
    main()
    


