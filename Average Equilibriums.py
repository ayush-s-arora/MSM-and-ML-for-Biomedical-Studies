import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit
import numpy as np
#initialize data variables
denoised_data = pd.read_csv('Data/SG_denoised_W99D5_rmsd-tph.csv')
x_data = denoised_data.iloc[:,1:len(denoised_data.columns)-1].values
y_data = denoised_data.iloc[:,len(denoised_data.columns)-1].values
mean_ys = []
pH = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
temperature = [3,3,3,3,3,20,20,20,20,20,37,37,37,37,37]
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
# graph 5 for a 3 dimensional relation between pH temp and RMSD
threeDDataFrame = pd.DataFrame({'pH':pH, 'AverageRMSD':mean_ys, 'Temperature':temperature})
threeD = plt.figure()
threeDax = threeD.add_subplot(111, projection='3d')
threeDScatter = threeDax.scatter(threeDDataFrame.pH, threeDDataFrame.AverageRMSD, threeDDataFrame.Temperature, s=100)
plt.title('3D Relationship Between Average RMSD, pH, and Temperature')
plt.xlabel('pH')
plt.ylabel('Average RMSD (nm)')
threeDax.set_zlabel('Temperature (\u00B0C)') 
plt.show()
#fit curve to data 
popt, pcov = curve_fit(lambda t, a, b, c: a * np.exp(b * t) + c, temperature, mean_ys, p0=(-0.1, -0.01, 0.5), bounds=((-1, -np.inf, 0), (0, -0.000001, 1)), maxfev = 1000)
a = float(popt[0])
b = float(popt[1])
c = float(popt[2])



# equation = 'y = ' + a + b + '^' + t + ' + ' + c
# show curve
# threeDax.plot3D(xline, yline, zline, 'gray')

# def fitCurve(temp, , b, c):
#   x,y = X
#   return np.log(a) + b*np.log(x) + c*np.log(y)
# x = np.linspace(pH)
# y = np.linspace(mean_ys)
# a, b, c = 10., 4., 6.
# z = fitCurve((x,y), a, b, c) * 1 + np.random.random(101) / 100
# p0 = 8., 2., 7.
# print(curve_fit(fitCurve, (x,y), z, p0))