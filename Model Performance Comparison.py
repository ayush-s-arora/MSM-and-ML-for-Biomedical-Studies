import pandas as pd

mcmcrange_outputs = pd.read_csv('Data/Model Predictions/MC-MC_range_outputs.csv')
pwrange_outputs = pd.read_csv('Data/Model Predictions/P-W_range_outputs.csv')
rmsdrange_outputs = pd.read_csv('Data/Model Predictions/RMSD_range_outputs.csv')
sasarange_outputs = pd.read_csv('Data/Model Predictions/SASA_range_outputs.csv')
rmsd_simerror = 0.0486799992137531
mcmc_simerror = 7.855255829042954
sasa_simerror = 13.785441517414181
pw_simerror = 25.388973984783238
rmsd_modelerror = 0.042
mcmc_modelerror = 7.84
pw_modelerror = 53.23
sasa_modelerror = 14.65