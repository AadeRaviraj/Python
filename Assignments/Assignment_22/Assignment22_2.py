# Dataset Description – Student Performance ML
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


# 2. Write a program to:
# • Display total number of students in the dataset
# • Count how many students Passed (FinalResult = 1)
# • Count how many students Failed (FinalResult = 0)

import pandas as pd

def main():
    border = "*" * 50
    fileName = "student_performance_ml.csv"
    
    csvData = pd.read_csv(fileName)
    
    totalNoFoStudents = len(csvData.index)
    print(border)
    print("Total Number of Students : ",totalNoFoStudents)    
    print(border)
    
    studentPassed = csvData["FinalResult"]
    passed = 0
    failed = 0
    for i in studentPassed:
        print(i)
        if i == 1:
            passed += i
        else:
            failed = failed + 1
        
        
        
    print("Passed Students : ",passed)  
    print(border)  
    print("Failed students : ",failed)
    


if __name__ == "__main__":
    main()