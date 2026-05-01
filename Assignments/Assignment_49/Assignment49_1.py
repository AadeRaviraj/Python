# Objective:
# Build a Machine Learning model to predict whether a patient is diabetic (1) or not (0) based on medical
# attributes.

# Task Instructions:
# You must complete the following steps
#  1. Exploratory Data Analysis (EDA):
#    • Load the dataset using pandas.
#    • Display the first 5 rows.
#    • Show column info and check for null values.
#    • Display basic statistics using .describe().
#    • Plot the distribution of the target variable (Outcome).
#    • Use graphs like hist, boxplot, or pairplot to identify patterns or outliers.


# 2. Data Preprocessing:
#   • Check and handle missing or zero values in columns like Glucose, BloodPressure, etc.
#   • Apply feature scaling using StandardScaler or MinMaxScaler.
#   • Split the dataset into features (X) and target (y).

# 3. Model Building:
# Train at least 2 different algorithms on the dataset:
#   • Logistic Regression
#   • K-Nearest Neighbors (KNN)
#   • Decision Tree
#   • Use train_test_split to divide the data.

# 4. Model Evaluation:
#   •  Print accuracy score, confusion matrix, precision, recall, and F1 score.
#   • Use matplotlib or seaborn to visualize confusion matrix.

# 5. Final Output:
#   • Predict whether a patient is diabetic based on test data.
#   • Display predictions on screen and save them in a CSV file.

import pandas as pd 
import matplotlib.pyplot as plt  
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler


######################################################################
####  Load the dataset 
######################################################################

border = "=" *50

print(border)
print("Load the dataset : ")
print(border)

df = pd.read_csv("diabetes.csv")

print("First 5 rows : ",df.head())

######################################################################
####  EDA  - Data Analysis
######################################################################
print(border)
print(" Step 2 : Data Analysis : ")
print(border)

print("Shape of data : ", df.shape)

print("Columns names : \n", df.columns)

print("If any missing value \n", df.isnull().sum())

print("Describe the Stastical report  :",df.describe())



######################################################################
####  Define the Dependent and independent variable 
######################################################################
print(border)
print(" Step 3 : Define  Dependent and independent variable  ")
print(border)

X = df.drop("Outcome",axis = 1)
Y = df["Outcome"]

print("Shape of Independent Variable : ", X.shape)
print("Shape of Dependent variable : ", Y.shape)


######################################################################
####  Visualize  the distribution of target variable 
######################################################################
print(border)
print(" Step 4  : Visualize the distribution of target variable ")
print(border)

# plt.figure(figsize=(8,8))

# df.hist(figsize=(8,8))
# plt.title("Distribution outcome :")
# plt.grid(True)
# plt.show()

# sns.boxplot(x='Outcome', y='BMI', data=df)
# plt.title('BMI distribution by Outcome')
# plt.show()


sns.countplot(x='Outcome', data=df)
plt.title("Target Variable Distribution")
plt.show()


######################################################################
####  Split the dataset into training and testing 
######################################################################

print(border)
print(" Step 5  : Split the dataset into training and testing  ")
print(border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

######################################################################
#### Create  models 
######################################################################
print(border)
print(" Step 6  : Create the model  ")
print(border)

# Step 3 : Create  models 
model_lr = LogisticRegression(max_iter=5000)
model_lr.fit(X_train,Y_train)
pred_lr = model_lr.predict(X_test)

acc_lr = accuracy_score(Y_test, pred_lr)
print("Logistic Regression Accuracy:", acc_lr)


print("Confusion Matrix (Logistic Regression):")

cm = confusion_matrix(Y_test, pred_lr)
sns.heatmap(cm,  annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Pred 0','Pred 1'], 
            yticklabels=['Actual 0','Actual 1'],
            linewidths=0.5, linecolor='black')
plt.show()


print("Classification report LR")
print(classification_report(Y_test, pred_lr))   # LR


print(border)

#########################################################################################################################################

model_dt = DecisionTreeClassifier(random_state=42)
model_dt.fit(X_train,Y_train)
pred_dt = model_dt.predict(X_test)


acc_dt = accuracy_score(Y_test, pred_dt)
print("DecisionTree Classifier Accuracy :", acc_dt)

print("Confusion Matrix : DecisionTree Classifier : ")
cmDTC = confusion_matrix(Y_test,pred_dt)
sns.heatmap( cmDTC, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Pred 0','Pred 1'], 
            yticklabels=['Actual 0','Actual 1'],
            linewidths=0.5, linecolor='black')
plt.show()



print("Classification Report DecisionTree :")
print(classification_report(Y_test, pred_dt))

print(border)

#########################################################################################################################################

model_knn = KNeighborsClassifier(n_neighbors=5)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model_knn.fit(X_train,Y_train)


pred_knn = model_knn.predict(X_test)

acc_knn = accuracy_score(Y_test, pred_knn)
print("Knn Classifier Accuracy :", acc_knn)

print("Confusion Matrix KNN:")
cm = confusion_matrix(Y_test, pred_lr)
sns.heatmap(cm,  annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Pred 0','Pred 1'], 
            yticklabels=['Actual 0','Actual 1'],
            linewidths=0.5, linecolor='black')
plt.show()

print("Classification Report KNN:")
print(classification_report(Y_test, pred_knn))
print(border)

# print(classification_report(Y_test, pred_lr))   # LR
# print(classification_report(Y_test, pred_dt))   # DT
# print(classification_report(Y_test, pred_knn))



#########################################################################################################################################
print("Export csv of predicted class patient diabeties or not ")





output = pd.DataFrame(X_test, columns=X.columns)
output['Actual'] = Y_test.values
output['PredictedLR'] = pred_lr
output['PredictedDT'] = pred_dt
output['PredictedKNN'] = pred_knn
output.to_csv("predict_result_04042026.csv", index=False)
