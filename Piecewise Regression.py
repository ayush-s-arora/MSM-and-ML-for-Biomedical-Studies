import matplotlib.pyplot as plt
import pandas as pd
import pwlf
import numpy as np

def visualize_og_df_type(og_df, graph_title):
    temps = [3, 20, 37]
    pHs = [1, 2, 3, 4, 5, 7]
    #limits = [0.7, 1.5, 1.5]
    #intervals = [0.1, 0.25, 0.5]

    figure, axis = plt.subplots(len(temps))
    figure.suptitle(graph_title)
    figure.set_figheight(10)
    for i in range(len(temps)):
        for p in pHs:
            col_header = "t" + str(temps[i]) + "-" + str(p)
            rmsd = []
            time = []
            for j in range(len(og_df[col_header])):
                rmsd.append(og_df.at[j, col_header])
                time.append(og_df.at[j, "Time"])
            axis[i].plot(time, rmsd, label="pH" + str(p))
            piecewise = pwlf.PiecewiseLinFit(time,rmsd)
            piecewise.fit(3)
            axis[i].plot(time, piecewise.predict(time), label="pH" + str(p))
        axis[i].legend()
        axis[i].set_title(str(temps[i]) + " Celsius")
        axis[i].set_xlabel('Time (ns)')
        axis[i].set_ylabel('RMSD (nm)')
        axis[i].set_ylim(bottom=0)
        #axis[i].set_yticks(np.arange(0, limits[i] + intervals[i], intervals[i]))
    plt.tight_layout()
    plt.show()
df = pd.read_csv('Data/MASTER_SG_rmsd-tph.csv')
df = df.dropna(axis=0)
visualize_og_df_type(df, 'visualization')