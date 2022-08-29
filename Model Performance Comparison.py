import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# import data
mcmcrange_outputs = pd.read_csv('Visual Studio/Data/Model Predictions/MC-MC_range_outputs.csv')
pwrange_outputs = pd.read_csv('Visual Studio/Data/Model Predictions/P-W_range_outputs.csv')
rmsdrange_outputs = pd.read_csv('Visual Studio/Data/Model Predictions/RMSD_range_outputs.csv')
sasarange_outputs = pd.read_csv('Visual Studio/Data/Model Predictions/SASA_range_outputs.csv')
rmsd_simerror = 0.0486799992137531
mcmc_simerror = 7.855255829042954
sasa_simerror = 13.785441517414181
pw_simerror = 25.388973984783238
rmsd_modelerror = 0.042
mcmc_modelerror = 7.84
pw_modelerror = 53.23
sasa_modelerror = 14.65

# remove first column (column numbers) from dataframes
mcmcrange_outputs = mcmcrange_outputs.iloc[:,1:]
pwrange_outputs = pwrange_outputs.iloc[:,1:]
rmsdrange_outputs = rmsdrange_outputs.iloc[:,1:]
sasarange_outputs = sasarange_outputs.iloc[:,1:]


# plot 1 3D graph for each set of outputs
fig = plt.figure()
axmcmc = plt.axes(projection='3d')
mcmcxdata = mcmcrange_outputs['x']
mcmcydata = mcmcrange_outputs['y']
mcmczdata = mcmcrange_outputs['z']
axmcmc.scatter3D(mcmcxdata, mcmcydata, mcmczdata)
axmcmc.set_title('MC-MC Range Outputs')
axmcmc.set_xlabel('X')
axmcmc.set_ylabel('Y')
axmcmc.set_zlabel('Z')
plt.show()
axpw = plt.axes(projection='3d')
pwxdata = pwrange_outputs['x']
pwydata = pwrange_outputs['y']
pwzdata = pwrange_outputs['z']
axpw.scatter3D(pwxdata, pwydata, pwzdata)
axpw.set_title('P-W Range Outputs')
axpw.set_xlabel('X')
axpw.set_ylabel('Y')
axpw.set_zlabel('Z')
plt.show()
axrmsd = plt.axes(projection='3d')
rmsdxdata = rmsdrange_outputs['x']
rmsdydata = rmsdrange_outputs['y']
rmsdzdata = rmsdrange_outputs['z']
axrmsd.scatter3D(rmsdxdata, rmsdydata, rmsdzdata)
axrmsd.set_title('RMSD Range Outputs')
axrmsd.set_xlabel('X')
axrmsd.set_ylabel('Y')
axrmsd.set_zlabel('Z')
plt.show()
axsasa = plt.axes(projection='3d')
sasaxdata = sasarange_outputs['x']
sasaydata = sasarange_outputs['y']
sasazdata = sasarange_outputs['z']
axsasa.scatter3D(sasaxdata, sasaydata, sasazdata)
axsasa.set_title('SASA Range Outputs')
axsasa.set_xlabel('X')
axsasa.set_ylabel('Y')
axsasa.set_zlabel('Z')
plt.show()

# Plot all outputs on one 3D graph
# ax = fig.add_subplot(111, projection = '3d')
# for current_output, c in zip((mcmcrange_outputs, pwrange_outputs, rmsdrange_outputs, sasarange_outputs), ('b', 'r', 'g', 'm')):
#         ax.scatter(*current_output[['x', 'y', 'z']].values.T, color=c)
# plt.show()