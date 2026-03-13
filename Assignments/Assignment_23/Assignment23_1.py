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

# 1. Import DecisionTreeClassifier from sklearn.
# Create a model object and train it using fit().


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
    
    feature_column =[
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]
    
    X = df[feature_column]
    Y = df["FinalResult"]
    
    
    print("X Shape : ", X.shape)
    print("Y Shape : ", Y.shape)
    
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
    
    
    
if __name__ == "__main__":
    main()