# Predict whether a news article is Fake or Real using text classification techniques. This assignment
# demonstrates the power of ensemble learning using a Voting Classifier with models like Logistic Regression,
# Decision Tree.


# Dataset Information:


# Dataset Name: Fake News Dataset


# Columns include:
# • title – Title of the news article
# • text – Main content of the article
# • label – 0 = Fake, 1 = Real

# Part 1: Data Preprocessing
# 1. Load the dataset using Pandas
# 2. Drop null values and select useful columns (title or text)
# 3. Convert the target variable (label) to binary (0 or 1)


# Part 2: Feature Extraction
# 1. Use TF-IDF Vectorization to convert text into numerical features


# Part 3: Model Training
# 1. Train individual models:
# ◦ Logistic Regression
# ◦ Decision Tree Classifier
# 2. Combine them using:
# ◦ Hard Voting (majority rule)
# ◦ Soft Voting (average predicted probabilities)

# Part 4: Evaluation
# 1. Compare accuracies of all models
# 2. Display confusion matrices
# 3. Soft vs hard voting


# Note : Dataset is divided into 2 parts as fake.csv and true.csv

# 1. Load both CSV files
# Each CSV represents a class:
# • fake.csv contains fake news articles
# • true.csv contains real news articles

# 2. Add a 'label' column to both
# We need to combine the two datasets, so we must label them first:
# • 0 = Fake
# • 1 = Real

# 3. Combine the datasets
# Now concatenate them into one DataFrame:

# 4. Use only the relevant columns
# You may use either title, text, or both combined.




import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer # for text extraction text into numeric value 
import matplotlib.pyplot as plt  
import seaborn as sns
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier,RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder


######################################################################
####  Load the dataset of Fake.csv and True.csv
######################################################################

border = "- " *50

print(border)
print("Load the dataset : ")
print(border)

fakeData = pd.read_csv("Fake.csv") # Read from csv 
TrueData = pd.read_csv("True.csv")


print("\nFake Data Original : \n", fakeData.head()) # Show first five records 
print("\nTrue Data Original : \n", TrueData.head()) # show first five records of True dataset


# Delete other columns 
fakeData = fakeData.drop(['title','subject','date'], axis=1)

TrueData = TrueData.drop(['title','subject','date'], axis=1)



# Adding label to both Fake And True Dataset 
fakeData['label'] = 0
TrueData['label'] = 1

# print("Added the label to the Fake dataset : ",fakeData.head())
# print("Added the label to the True dataset : ", TrueData.head())


# ######################################################################
# ####  EDA  - Data Analysis
# ######################################################################
print(border)
print(" Step 2 : Data Analysis : ")
print(border)

# Combine the dataset of Fake news and True news

data = pd.concat([fakeData,TrueData])

print("Combined Data : ",data.head)

# if any null value or any value is missing 

print("If any missing value : ", data.isnull().sum())


vectorization = TfidfVectorizer()

X = vectorization.fit_transform(data['text'])
Y = data['label']

print(X.shape)
print(Y.shape)



# ###################################################################
# #   Train test split 
# ###################################################################


X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42)   # Split for testing 80 training 20 


# ##############################################################################
# # Model train 
# ##############################################################################

# ## Model train fro 


lr = LogisticRegression(max_iter= 1000)
lr.fit(X_train,Y_train)
YPredLr = lr.predict(X_test)


## Model train for dtc
dtc = DecisionTreeClassifier()
dtc.fit(X_train,Y_train)
YpredDtc = dtc.predict(X_test)


# Accuracy Calculate for logistic regression 
print("Accuracy of Logistic regression :", accuracy_score(Y_test, YPredLr))
print(confusion_matrix(Y_test, YPredLr))
print(classification_report(Y_test, YPredLr))


# # Accuracy Calculate for logistic DTC 
print("Accuracy of  DTC :", accuracy_score(Y_test, YpredDtc))
print(confusion_matrix(Y_test, YpredDtc))
print(classification_report(Y_test, YpredDtc))

#######################################################################
#  Voting classifier calculatte the voting 
#######################################################################

models = [("lr", lr), ("dt", dtc)]
hard_voting_classifier = VotingClassifier(estimators=models, voting="hard")
soft_voting_classifier = VotingClassifier(estimators=models, voting="soft")

# train voting class 
hard_voting_classifier.fit(X_train, Y_train)
soft_voting_classifier.fit(X_train, Y_train)

# predict voting class 
Ypred_hard = hard_voting_classifier.predict(X_test)
Ypred_soft = soft_voting_classifier.predict(X_test)

# check accuracy of voting 
print("Hard Voting Accuracy:", accuracy_score(Y_test, Ypred_hard))
print("Soft Voting Accuracy:", accuracy_score(Y_test, Ypred_soft))


######################################################################
####  Visualization   
######################################################################
print(border)
print(" Step 4  : Visualize ")
print(border)

# graph for Logistic regression 
sns.heatmap(confusion_matrix(Y_test, YPredLr), annot=True, fmt='d',
            xticklabels=['Fake','Real'], yticklabels=['Fake','Real'])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Logistic Regression")
plt.show()

# graph for Decision treee
sns.heatmap(confusion_matrix(Y_test, YpredDtc), annot=True, fmt='d',
            xticklabels=['Fake','Real'], yticklabels=['Fake','Real'])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Decision Tree")
plt.show()


# graph fo r Voting class 
sns.heatmap(confusion_matrix(Y_test, Ypred_hard), annot=True, fmt='d',
            xticklabels=['Fake','Real'], yticklabels=['Fake','Real'])
plt.title("Confusion Matrix - Hard Voting")
plt.show()

sns.heatmap(confusion_matrix(Y_test, Ypred_soft), annot=True, fmt='d',
            xticklabels=['Fake','Real'], yticklabels=['Fake','Real'])
plt.title("Confusion Matrix - Soft Voting")
plt.show()