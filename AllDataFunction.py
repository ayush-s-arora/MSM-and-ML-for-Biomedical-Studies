from data_extraction_pw_hbond_2_anya import data_anya
from For_AllDataFunction_2nd_HBond_MCMC_Extraction import data_ayush
from data_extraction_sasa_evan import data_evan
import pandas as pd

# Call data
data_anya = data_anya()
data_ayush = data_ayush()
data_evan = data_evan()
data_rmsd = pd.read_csv('Visual Studio/Data/MASTER_SG_rmsd-tph.csv')

# Plot data
data_anya.plot()
data_ayush.plot()
data_evan.plot()
data_rmsd.plot()