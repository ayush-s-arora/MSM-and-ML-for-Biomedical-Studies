import pandas as pd
train_df = pd.read_csv('Data/SG_rmsdtph_train.csv')
test_df = pd.read_csv('Data/SG_rmsdtph_test.csv')
x_train = train_df.iloc[:,1:len(train_df.columns)-1].values.tolist()
y_train = train_df.iloc[:,len(train_df.columns)-1].values.tolist()
x_test = test_df.iloc[:,1:len(train_df.columns)-1].values.tolist()
y_test = test_df.iloc[:,len(train_df.columns)-1].values.tolist()