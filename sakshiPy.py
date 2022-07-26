import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.getcwd()
os.listdir()

data = pd.read_csv('run10109.csv',sep = ',')

current_step = 0.0
for i in range(len(data['step_value_epics'])):
    if float(data['step_value_epics'][i][1:-1]) != current_step:
        if float(data['step_value_epics'][i][1:-1]) < current_step:
            data2 = data[:i]
            break
        current_step = float(data['step_value_epics'][i][1:-1])
        
data_group = data2.groupby('step_value_epics')

steps = list(data_group.groups.keys())

print(data_group)

plt.figure("Sakshi makes a plot")
plt.clf()
for i in steps:
    plt.plot(data_group.get_group(i).groupby('dipole_freq')['tof'].mean(), '-o', label = i[1:-1])
plt.legend()
plt.show()

plt.savefig('sakshiPlot.jpg')