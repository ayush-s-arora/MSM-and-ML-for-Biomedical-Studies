import pandas as pd
import matplotlib.pyplot as plt
denoised_data = pd.read_csv('Data/SG_denoised_W99D5_rmsd-tph.csv')
x_data = denoised_data.iloc[:,1:len(denoised_data.columns)-1].values
y_data = denoised_data.iloc[:,len(denoised_data.columns)-1].values
mean_ys = []
for column in denoised_data:
  eachColumn = denoised_data[column]
  mean_ys.append(eachColumn.mean())
mean_ys.pop(0)