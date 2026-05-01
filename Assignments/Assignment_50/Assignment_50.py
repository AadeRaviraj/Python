# Domain: Banking, Marketing


# Problem Statement:


# A Portuguese bank conducted marketing campaigns to promote term deposit subscriptions. The goal is to
# predict whether a client will subscribe (yes or no) to a term deposit based on their profile and campaign
# interaction details.

# Dataset Overview:
# You will use the Bank Marketing Dataset from UCI repository.
# Target Column: y
# (yes = client subscribed to term deposit, no = did not subscribe)
#
# ---------------------------------------------------------
# Feature   |     Description                             |
# ---------------------------------------------------------
# age       |    age of the client                        |
# job       |    job type (admin., technician, etc.)      |
# marital   |    marital status                           |
# education |    education level                          |
# default   |    has credit in default?                   |
# balance   |    average yearly account balance           |
# housing   |    has housing loan?                        |
# loan      |    has personal loan?                       |
# contact   |    contact communication type               |
# day       |    last contact day of the month            |
# month     |    last contact month of year               |
# duration  |    last contact duration                    |
# campaign  |    number of contacts during campaign       |
# previous  |    number of contacts before this campaign  |
# poutcome  |    outcome of previous campaign             |
# ---------------------------------------------------------


# Assignment Tasks:
    
# 1. Load and Explore the Dataset
# ◦ Handle missing or unknown values (e.g., unknown in categorical features).
# ◦ Display basic stats and visualize class distribution.

# 2. Preprocess the Data
# ◦ Convert categorical variables using Label Encoding or One-Hot Encoding.
# ◦ Scale numeric features (e.g., using StandardScaler).

# 3. Split the Data
# ◦ Use 80% data for training and 20% for testing.
# ◦ Apply train_test_split().

# 4. Train Classification Models
# ◦ Train the following models:
# ▪ Logistic Regression
# ▪ K-Nearest Neighbors
# ▪ Random Forest Classifier

# 5. Evaluate the Models
# ◦ Compare using:
# ▪ Accuracy
# ▪ Confusion Matrix
# ▪ Classification Report
# ▪ ROC-AUC score

# 6. Visualize Results
# ◦ Plot confusion matrix and ROC curves.





import pandas as pd 
import matplotlib.pyplot as plt  
import seaborn as sns
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder


######################################################################
####  Load the dataset 
######################################################################

border = "- " *50

print(border)
print("Load the dataset : ")
print(border)

df = pd.read_csv("bank_full.csv")

print("First 5 rows : ",df.head())

# ######################################################################
# ####  EDA  - Data Analysis
# ######################################################################
print(border)
print(" Step 2 : Data Analysis : ")
print(border)

print("Shape of data : ", df.shape)

print("Columns names : \n", df.columns)

# handling the Unkonwn values by filling 

df.replace("unknown",np.nan,inplace= True)

for col in ['job','education','contact','poutcome','marital']:
    df[col].fillna("missing",inplace= True)
    

df = pd.get_dummies(df,drop_first=True) # label encoding 


print("If any Missing values:\n", df.isnull().sum())  # if any missing values 

print("Describe the Stastical report  :",df.describe())

print("Starting Some data : ", df.head)
print("Ending some data : ", df.tail)

# df.to_csv("new.csv", index= False)


###################################################################
#   Feature Scaling :-
###################################################################
scaler = StandardScaler()

X = df.drop("y_yes",axis=1)
X = scaler.fit_transform(X)


###################################################################
#  Convert the Y column into yes no 
###################################################################

# df["Y"] = df['y'].map({'yes':1,'no':0})

###################################################################
#   Train test split 
###################################################################

# X = df.drop('y',axis=1)
Y = df["y_yes"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42)   # Split for testing 80 training 20 


##############################################################################
# Model train 
##############################################################################

## Model train fro 


lr = LogisticRegression(max_iter= 1000)
lr.fit(X_train,Y_train)
YPredLr = lr.predict(X_test)


## Model train for KNN
knn = KNeighborsClassifier(n_neighbors= 5)
knn.fit(X_train,Y_train)
YpredKNN = knn.predict(X_test)

## model train for random forest :
rf = RandomForestClassifier(n_estimators= 5 , random_state=42)
rf.fit(X_train,Y_train)
YpredRF = rf.predict(X_test)




# Accuracy Calculate for logistic regression 
print("Accuracy of Linear regression :", accuracy_score(Y_test, YPredLr))
print(confusion_matrix(Y_test, YPredLr))
print(classification_report(Y_test, YPredLr))



# Accuracy Calculate for logistic KNN 

print("Accuracy of  KNN :", accuracy_score(Y_test, YpredKNN))
print(confusion_matrix(Y_test, YpredKNN))
print(classification_report(Y_test, YpredKNN))


# Accuracy Calculate for logistic randomForest  

print("Accuracy of Random Forest :", accuracy_score(Y_test, YpredRF))
print(confusion_matrix(Y_test, YpredRF))
print(classification_report(Y_test, YpredRF))


######################################################################
####  Visualize  the distribution of target variable 
######################################################################
print(border)
print(" Step 4  : Visualize the distribution of target variable ")
print(border)


sns.heatmap(confusion_matrix(Y_test, YpredRF), annot=True, fmt='d')
plt.show()

sns.heatmap(confusion_matrix(Y_test, YPredLr), annot=True, fmt='d')
plt.show()
