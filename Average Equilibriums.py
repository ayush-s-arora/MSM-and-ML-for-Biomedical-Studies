import pandas as pd
import matplotlib.pyplot as plt
#initialize data variables
denoised_data = pd.read_csv('Data/SG_denoised_W99D5_rmsd-tph.csv')
x_data = denoised_data.iloc[:,1:len(denoised_data.columns)-1].values
y_data = denoised_data.iloc[:,len(denoised_data.columns)-1].values
mean_ys = []
#experimental temperature values
temp1 = 3
temp2 = 20
temp3 = 37
#axis for plotting data using matplotlib
x_axis = [1,2,3,4,5]
y_error = []
#take the averages and standard deviations of each column
for column in denoised_data:
  eachColumn = denoised_data[column]
  mean_ys.append(eachColumn.mean())
  y_error.append(eachColumn.std())
#remove first entry for mean and standard deviation (irrelevant - column numbers)
mean_ys.pop(0)
y_error.pop(0)
# graph 1 for 3°C
plt.plot(x_axis, mean_ys[0:5], marker = 'o')
plt.title('Average RMSD and pH at ' + str(temp1) + '\u00B0C')
plt.xlabel('pH')
plt.ylabel('Average RMSD (nm)')
# plt.errorbar(x_axis, mean_ys[0:5], yerr = y_error[0:5], fmt='o')
plt.show()
# graph 2 for 20°C
plt.plot(x_axis, mean_ys[5:10], marker = 'o')
plt.title('Average RMSD and pH at ' + str(temp2) + '\u00B0C')
plt.xlabel('pH')
plt.ylabel('Average RMSD (nm)')
# plt.errorbar(x_axis, mean_ys[5:10], yerr = y_error[5:10], fmt='o')
plt.show()
# graph 3 for 37°C
plt.plot(x_axis, mean_ys[10:15], marker = 'o')
plt.title('Average RMSD and pH at ' + str(temp3) + '\u00B0C')
plt.xlabel('pH')
plt.ylabel('Average RMSD (nm)')
# plt.errorbar(x_axis, mean_ys[10:15], yerr = y_error[10:15], fmt='o')
plt.show()
# graph 4 for relation between pH and RMSD for all temperatures
scatterPlot = plt.gca()
scatterPlot.scatter(x_axis, mean_ys[0:5], color='b', label = str(temp1) + '\u00B0C')
scatterPlot.scatter(x_axis, mean_ys[5:10], color='g', label = str(temp2) + '\u00B0C')
scatterPlot.scatter(x_axis, mean_ys[10:15], color='r', label = str(temp3) + '\u00B0C')
plt.title('Average RMSD vs pH at Varying Temperatures')
plt.xlabel('pH')
plt.ylabel('Average RMSD (nm)')
scatterPlot.legend()
plt.show()