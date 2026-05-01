# 3. Write a Python program using StandardScaler to perform feature scaling on the following dataset:
# [[25,20000],
# [30,40000],
# [35,80000]]
# Print the scaled dataset.



import numpy as np 
import pandas as pd 
from sklearn.preprocessing import StandardScaler

X = [6,7,8,9,10,11,12]

data = pd.DataFrame({
    'Age': [25,30,35],
    'Salary':[20000,40000,80000]
})
 
X = data["Age"]
Y = data["Salary"]

scaler = StandardScaler()

Scaled = scaler.fit_transform(data)
 
print("Scaled Dataset  :\n",Scaled)


# Output :- 

# Scaled Dataset  :
#  [[-1.22474487 -1.06904497]
#  [ 0.         -0.26726124]
#  [ 1.22474487  1.33630621]]