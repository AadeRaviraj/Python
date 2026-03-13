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


# 1. Write a Python program to load the file student_performance_ml.csv using pandas.
# Display:
# • First 5 records
# • Last 5 records
# • Total number of rows and columns
# • List of column names
# • Data types of each column

import pandas as pd


def main():
    border = "*" * 50
    fileName = "student_performance_ml.csv"
    csvData = pd.read_csv(fileName)
    print(csvData,"\n")
    print(border)
    
    firstFiveRecord = csvData.head(5)
    print("First Five Record",firstFiveRecord,"\n")
    print(border)
    
    
    lastFiveRecord = csvData.tail(5)
    print("Last 5 records :",lastFiveRecord , "\n")
    
    print(border)
    
    row = len(csvData.index) # index is indicates teh row in pandas csv 
    column = len(csvData.columns)
    print(f"Total Number of Rows is {row} and Columns is {column}  \n")
    
    print(border)
    
    columnName = csvData.columns
    for i in columnName:
        print("Column names :",i)

    print(border)
    
    
    columnDataType = csvData.dtypes
    print("Column Data type : ",columnDataType)
    print(border)
    




if __name__ == "__main__":
    main()
