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


# 10. Plot SleepHours against FinalResult.
# Does sleeping more guarantee success? Explain.

import pandas as pd 
import matplotlib.pyplot as plt


def main():
    border = "*" * 50
    fileName = "student_performance_ml.csv"
    
    csvData = pd.read_csv(fileName) 
    x = csvData["SleepHours"]
    y = csvData["FinalResult"]
    
    plt.scatter(x,y)
    plt.title("SleepHours vs FinalResult")

    plt.xlabel("Sleep hours")
    plt.ylabel("Final Result")
    plt.show()
    

if __name__ == "__main__":
    main()
    
    