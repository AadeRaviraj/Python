# Cluster students into different academic performance groups based on features like:
# • Final grades
# • Study time
# • Failures
# • Absences
# This helps identify:
# • Top Performers
# • Average Students
# • Struggling Students

# Dataset Details:
# • Dataset Name: Student Performance Data Set

# Selected Features:
# Use these numerical features for clustering:

# • G1, G2, G3 → First, second, final grades
# • studytime → Weekly study hours
# • failures → Number of past class failures
# • absences → Number of school absences

# You should create below clusters as

# • Top Performers (Cluster 0):
# ◦ High grades and low failure count
# ◦ High study time and few absences

# • Average Students (Cluster 1):
# ◦ Moderate scores and study time
# ◦ Some failures or absences

# • Struggling Students (Cluster 2):
# ◦ Low grades, high failure and absence rate
# ◦ Low study time

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def main():
    # - -----------------------------------------------------------
    # Step 1 : Load the dataset 
    # -------------------------------------------------------------
    print("Load the dataset ")
    df = pd.read_csv("student.csv")
    
    print("First few records --")
    print(df.head())
    print("Shape of dataset :")
    print(df.shape)
    
    
 
    
    # - -----------------------------------------------------------
    # Step 2 : Select feature (independent) 
    # -------------------------------------------------------------
    print("Step 2 : Select feature (independent) ")
    
    X = df[["G1", "G2", "G3", "studytime", "failures", "absences"]]

    print("First few records --")
    print(X.head())
    print("Shape of dataset :")
    print(X.shape)
    
    print("Missing values : ")
    print(X.isnull().sum())
    
    
    
    # - -----------------------------------------------------------
    # Step 3 : Scale the data
    # -------------------------------------------------------------
    
    
    scaler = StandardScaler()
    X_Scale = scaler.fit_transform(X)
    
    print("Data after Scaling : ")
    
    print(X_Scale[:5])  # Show the first five Scaled rows 
    
    
    # - -----------------------------------------------------------
    # Step 4 : Use elbow method 
    # -------------------------------------------------------------
    
    WCSS = [] 
    # it tells us  which is teh best k value for cluster 
    
    for i in range(1,11):
        model = KMeans(n_clusters=i,random_state= 42,n_init=10)
        model.fit(X_Scale)
        WCSS.append(model.inertia_)
    
    plt.figure(figsize=(8,5))
    plt.plot(range(1,11),WCSS,marker ="o")
    plt.xlabel("Number of  cluster")
    plt.ylabel("WCSS")
    plt.title("Elbow method")
    plt.grid(True)
    plt.show()

    
    # - -----------------------------------------------------------
    # Step 5 :Train the model
    # -------------------------------------------------------------
    
    
    model = KMeans(n_clusters=3,random_state=42,n_init=10)
    
    clusters  = model.fit_predict(X_Scale)
    
    print("Clusters \n",clusters)
    
    print(X.groupby(clusters).mean())
    
    print("Dataset with clusters : ")
    # print(X.head(40))
    
    # Final visualize :
    
    # plt.scatter(X["G3"],X["studytime"],c=clusters)  For bydefault cluster  colrrs
    
    colors =["green","blue","red"]
    plt.scatter(X['G3'],X['studytime'],c=[colors[i] for i in clusters])
    plt.xlabel("Final grade")
    plt.ylabel("Study time")
    plt.grid(False)
    plt.title("Student Clusters")
    plt.show()
    
    
    
if __name__ == "__main__":
    main()