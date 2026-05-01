# 4. Write a Python program to calculate the Euclidean distance between two points before and after applying
# feature scaling, and explain the difference in results.

# formula : Two Dimensions (2D):  

import numpy as np  
import pandas as pd 
from sklearn.preprocessing import StandardScaler


def EuclideanDistance(P1,P2):
    ans = np.sqrt((P1['Age'] - P2["Age"])**2 + (P1["Salary"] - P2["Salary"])**2)
    return ans



data = pd.DataFrame({
    'Age': [25,30,35],
    'Salary':[20000,40000,80000]
})

p1 = data.iloc[0]
p2 = data.iloc[1]
Ans = EuclideanDistance(p1,p2)


scaler = StandardScaler()

Scaled = scaler.fit_transform(data) 
print("Before Scaling:", Ans)

scaledans = pd.DataFrame(Scaled,columns=['Age','Salary'])

p12 = scaledans.iloc[0]
p22 = scaledans.iloc[1]
Ans2 = EuclideanDistance(p12,p22)

print("After Scaling:", Ans2)

