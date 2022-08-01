from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

df = pd.read_csv('Data/rmsd-tph.csv')
temps = [3, 20, 37]
pHs = [1, 2, 3, 4, 5]

test_col = "t37-5"

# Inputs are of the form [time, temp, pH]
# Outputs are RMSD
x_train = []
y_train = []
x_test = []
y_test = []

# Min and Max Vals for Scaling
ti_min = 0.0
ti_max = float(df.at[len(df)-1, "Time"])
temp_min = 3
temp_max = 37
ph_min = 1
ph_max = 5

# Define minmax_scale
def minmax_scale(val, min, max):
    return (val - min) / (max - min)

# Split dataframe into train, test, input, and output arrays
# Total length of inputs and outputs: 148735
for t in temps:
    for p in pHs:
        col_header = "t" + str(t) + "-" + str(p)
        inputs = []
        outputs = []
        i = 0
        while i < len(df) and not math.isnan(df.at[i, col_header]):
            sct = minmax_scale(float(df.at[i, "Time"]), ti_min, ti_max)
            sctemp = minmax_scale(t, temp_min, temp_max)
            scph = minmax_scale(p, ph_min, ph_max)
            inputs.append([sct, sctemp, scph])
            outputs.append(df.at[i, col_header])
            i += 1
        if col_header == test_col:
            x_test.extend(inputs)
            y_test.extend(outputs)
        else:
            x_train.extend(inputs)
            y_train.extend(outputs)
def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0, x >= x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])
p , e = optimize.curve_fit(piecewise_linear, x_train, y_train)
xd = np.linspace(0, 15, 100)
plt.plot(x_train, y_train, "o")
plt.plot(xd, piecewise_linear(xd, *p))