import math
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn import preprocessing
from sklearn import utils

df = pd.read_csv('Data/rmsd-tph.csv')
temps = [3, 20, 37]
pHs = [1, 2, 3, 4, 5]

test_col = "t37-5"

# Inputs are of the form [time, temp, pH]
# Outputs are RMSD
x_train = []
y_train = []
x_test = []
y_test = []

# Min and Max Vals for Scaling
ti_min = 0.0
ti_max = float(df.at[len(df)-1, "Time"])
temp_min = 3
temp_max = 37
ph_min = 1
ph_max = 5

# define minmax_scale
def minmax_scale(val, min, max):
    return (val - min) / (max - min)

# Split dataframe into train, test, input, and output arrays
# Total length of inputs and outputs: 148735
for t in temps:
    for p in pHs:
        col_header = "t" + str(t) + "-" + str(p)
        inputs = []
        outputs = []
        i = 0
        while i < len(df) and not math.isnan(df.at[i, col_header]):
            sct = minmax_scale(float(df.at[i, "Time"]), ti_min, ti_max)
            sctemp = minmax_scale(t, temp_min, temp_max)
            scph = minmax_scale(p, ph_min, ph_max)
            inputs.append([sct, sctemp, scph])
            outputs.append(df.at[i, col_header])
            i += 1
        if col_header == test_col:
            x_test.extend(inputs)
            y_test.extend(outputs)
        else:
            x_train.extend(inputs)
            y_train.extend(outputs)
# fix "ValueError: Unknown label type: 'continuous'"
lab_enc = preprocessing.LabelEncoder()
encodedx_train = lab_enc.fit_transform(x_train)
encodedy_train = lab_enc.fit_transform(y_train)

# Function to perform training with giniIndex.
def train_using_gini(X_train, X_test, y_train):
  
    # Creating the classifier object
    clf_gini = DecisionTreeClassifier(criterion = "gini",
            random_state = 100,max_depth=3, min_samples_leaf=5)
  
    # Performing training
    clf_gini.fit(encodedx_train, encodedy_train)
    return clf_gini
      
# Function to perform training with entropy.
def tarin_using_entropy(X_train, X_test, y_train):
  
    # Decision tree with entropy
    clf_entropy = DecisionTreeClassifier(
            criterion = "entropy", random_state = 100,
            max_depth = 3, min_samples_leaf = 5)
  
    # Performing training
    clf_entropy.fit(X_train, y_train)
    return clf_entropy
  
  
# Function to make predictions
def prediction(X_test, clf_object):
  
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred)
    return y_pred
      
# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
      
    print("Confusion Matrix: ",
        confusion_matrix(y_test, y_pred))
      
    print ("Accuracy : ",
    accuracy_score(y_test,y_pred)*100)
      
    print("Report : ",
    classification_report(y_test, y_pred))
  
# Driver code
def main():
      
    # Building Phase
    clf_gini = train_using_gini(x_train, x_test, y_train)
    clf_entropy = tarin_using_entropy(x_train, x_test, y_train)
      
    # Operational Phase
    print("Results Using Gini Index:")
      
    # Prediction using gini
    y_pred_gini = prediction(x_test, clf_gini)
    cal_accuracy(y_test, y_pred_gini)
      
    print("Results Using Entropy:")
    # Prediction using entropy
    y_pred_entropy = prediction(x_test, clf_entropy)
    cal_accuracy(y_test, y_pred_entropy)
      
      
# Calling main function
if __name__=="__main__":
    main()