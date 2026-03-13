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


# 5. Based on the dataset values, analyze whether:
# • Higher StudyHours increase the chance of passing.
# • Higher Attendance improves FinalResult.
# Write your observations in 4–5 lines.


# Students with lower StudyHours (around 1–4 hours) mostly have a FinalResult of 0 (Fail), 
# while students studying 5 hours or more mostly pass. 
# This suggests that higher StudyHours increase the chance of passing. 
# Similarly, students with Attendance below about 70–75% tend to fail, whereas those with Attendance above 80% mostly pass. 
# Therefore, higher attendance also improves the likelihood of a positive FinalResult.  
