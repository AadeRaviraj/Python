# 8. Write a Python program that calculates TP, TN, FP, FN for the following arrays:
# actual = [1,1,1,1,0,0,0,0]
# predicted = [1,1,0,1,0,1,0,0]
# Display all four values.

from sklearn import metrics

actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

print("Actual Data :",actual)
print("Predicted Data :", predicted)


result = metrics.confusion_matrix(actual,predicted)

print("Confusion Matrix : \n",result)