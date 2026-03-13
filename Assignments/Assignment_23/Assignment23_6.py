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

 
# 6. Train three Decision Tree models with:
# • max_depth = 1
# • max_depth = 3
# • max_depth = None
# Compare their testing accuracies and write your observations.





from sklearn import tree
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import     accuracy_score,confusion_matrix

def main():
    border = "*" * 50
    fileName = "student_performance_ml.csv"  # csv file name : 
    
    df = pd.read_csv(fileName) 
    
    
    # Build the model 
    model = DecisionTreeClassifier(
        criterion= "gini",
        max_depth=1,
        random_state=42
    )
    model2 = DecisionTreeClassifier(
        criterion= "gini",
        max_depth=3,
        random_state=42
    )
    model3 = DecisionTreeClassifier(
        criterion= "gini",
        max_depth=None,
        random_state=42
    )
    
    
    
    
    # modelObj = tree.DecisionTreeClassifier() # create ModelObject 

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
    
    
    print("---------------- Train Model 1 : Max Depth 1:-----------------")
    
    model.fit(X_train,Y_train)
    
    Y_Pred=model.predict(X_test)    
    
    print("Predicted Answer : ", Y_Pred)
    print("Expected Answer : ",Y_test)
    
    accuracy = accuracy_score(Y_test,Y_Pred)
    print("The Accuracy 1st of model is : ",accuracy * 100)
    
    
    print("---------------- Train Model 2 : MaxDepth 3-----------------")
    
    model2.fit(X_train,Y_train)
    
    Ypred = model2.predict(X_test)
    print("Predicted Answer : ",Ypred)
    print("Expected Answer : ",Y_test) 
    
    accuracy_ = accuracy_score(Y_test,Ypred)
    print("The Accuracy of 2nd model is : ",accuracy_ * 100)
    
    
    print("---------------- Train Model 3 : maxdepth none  -----------------")
    model3.fit(X_train,Y_train)
    yPred = model3.predict(X_test)
    print("Predicted Model : ",yPred)
    print("Expected Answer :",Y_test)
    acc = accuracy_score(Y_test,yPred)
    print("The Accuracy of 3rd  model is : ",acc * 100)    
    
    
    
    
if __name__ == "__main__":
    main()

