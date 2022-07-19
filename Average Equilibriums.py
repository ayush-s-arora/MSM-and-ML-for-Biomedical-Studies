import pandas as pd
train_df = pd.read_csv('Data/SG_rmsdtph_train.csv')
test_df = pd.read_csv('Data/SG_rmsdtph_test.csv')
x_train = train_df.iloc[:,1:len(train_df.columns)-1].values.tolist()
y_train = train_df.iloc[:,len(train_df.columns)-1].values
x_test = test_df.iloc[:,1:len(train_df.columns)-1].values.tolist()
y_test = test_df.iloc[:,len(train_df.columns)-1].values
mean_y_train = y_train.mean()
mean_y_test = y_test.mean()
mean_y = (mean_y_train + mean_y_test) / 2
print(mean_y)