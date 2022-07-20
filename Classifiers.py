import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
#initialize data variables
train_df = pd.read_csv('Data/SG_rmsdtph_train.csv')
test_df = pd.read_csv('Data/SG_rmsdtph_test.csv')
df = train_df[["Temperature", "pH", "RMSD"]]
df_test = test_df[["Temperature", "pH", "RMSD"]]
x_train = df[["Temperature", "pH"]]
y_train = df["RMSD"]
x_test = df_test[["Temperature", "pH"]]
y_test = df_test["RMSD"]
multipleRegressionModel = LinearRegression()
multipleRegressionModel.fit(x_train, y_train)
y_prediction = multipleRegressionModel.predict(x_test)
score = r2_score(y_test, y_prediction)
print(score)



















#old knn code, didn't work
# x_train = ["Temperature", "pH"]
# print(x_train)
# y_train = train_df.iloc[:,len(train_df.columns)-1].values.tolist()
# x_test = test_df.iloc[:,1:len(train_df.columns)-1].values.tolist()
# y_test = test_df.iloc[:,len(train_df.columns)-1].values.tolist()
# labelEncoder = preprocessing.LabelEncoder()
# categoricalsXTrain = labelEncoder.fit_transform(x_train)
# categoricalsYTrain = labelEncoder.fit_transform(y_train)
# knn = KNeighborsClassifier(n_neighbors = 5)
# knn.fit(x_train, y_train)
# print(knn.predict(x_test))