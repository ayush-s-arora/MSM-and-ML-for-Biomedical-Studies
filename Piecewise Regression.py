import matplotlib.pyplot as plt
import pandas as pd
import pwlf
import numpy as np
from sympy import Symbol
from sympy.utilities import lambdify

# create x symbol for printing functions in output
x = Symbol('x')

# visualization of data, including piecewise functions
def visualize_og_df_type(og_df, graph_title):
    eqn_list = []
    f_list = []
    temps = [3, 20, 37]
    pHs = [1, 2, 3, 4, 5, 7]
    #limits = [0.7, 1.5, 1.5]
    #intervals = [0.1, 0.25, 0.5]

    # plot data
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
            # plot piecewise functions
            axis[i].plot(time, piecewise.predict(time), label='_nolegend_' + str(p), color = "black", linewidth = 1)
            # show piecewise functions and endpoints in output
            for s in range(piecewise.n_segments):
                eqn_list.append(get_symbolic_eqn(piecewise, s + 1))
                print('Equation number: ', s + 1)
                print(eqn_list[-1])
                print('Corresponding Endpoints: ', piecewise.fit_breaks)
                f_list.append(lambdify(x, eqn_list[-1]))
        axis[i].legend()
        # plot formatting
        axis[i].set_title(str(temps[i]) + " Celsius")
        axis[i].set_xlabel('Time (ns)')
        axis[i].set_ylabel('RMSD (nm)')
        axis[i].set_ylim(bottom=0)
        #axis[i].set_yticks(np.arange(0, limits[i] + intervals[i], intervals[i]))
    plt.tight_layout()
    plt.show()

# find piecewise equations
def get_symbolic_eqn(pwlf_, segment_number):
    if pwlf_.degree < 1:
        raise ValueError('Degree must be at least 1')
    if segment_number < 1 or segment_number > pwlf_.n_segments:
        raise ValueError('segment_number not possible')
    # assemble degree = 1 first
    for line in range(segment_number):
        if line == 0:
            my_eqn = pwlf_.beta[0] + (pwlf_.beta[1])*(x-pwlf_.fit_breaks[0])
        else:
            my_eqn += (pwlf_.beta[line+1])*(x-pwlf_.fit_breaks[line])
    # assemble all other degrees
    if pwlf_.degree > 1:
        for k in range(2, pwlf_.degree + 1):
            for line in range(segment_number):
                beta_index = pwlf_.n_segments*(k-1) + line + 1
                my_eqn += (pwlf_.beta[beta_index])*(x-pwlf_.fit_breaks[line])**k
    return my_eqn.simplify()

# import dataframe
df = pd.read_csv('Data/MASTER_SG_rmsd-tph.csv')
# remove null values
df = df.dropna(axis=0)
# visualize data and piecewise functions
visualize_og_df_type(df, 'New SG Denoised Data')