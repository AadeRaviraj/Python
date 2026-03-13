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


# 7. Create a scatter plot of:
# StudyHours vs PreviousScore
# Use different colors for Pass and Fail students.

import pandas as pd 
import matplotlib.pyplot as plt


def main():
    border = "*" * 50
    fileName = "student_performance_ml.csv"
    
    csvData = pd.read_csv(fileName)
    passCount = csvData[csvData["FinalResult"] == 1]
    failCount = csvData[csvData["FinalResult"] == 0]


    plt.scatter(passCount["StudyHours"],passCount["PreviousScore"],marker="*",color="#1fb421")
    plt.scatter(failCount["StudyHours"],failCount["PreviousScore"],marker="o",color="#b41f1f")
    plt.xlabel("Study Hour")
    plt.ylabel("Previous Score")
    plt.title("Pass Fail on the previous StudyHour and previousStudy hour")
    plt.show()
    
if __name__ =="__main__":
    main()