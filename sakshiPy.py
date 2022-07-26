import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.getcwd()
os.listdir()

data = pd.read_csv('run10109.csv',sep = ',')

step_val = 0.0
stop = False
arr, data_arr = [], []
desc_vals=[]
for i in range(len(data['event'])):
    desc = float(data['step_value_epics'][i][1:-1])
    if  desc != step_val:
        if stop == True:
            break
        desc_vals.append(desc)
        data_arr.append(arr)
        arr = []
        arr.append([data['tof'][i],data['dipole_freq'][i]])
        step_val = desc
        if desc == 2100.0:
            stop = True
    if desc == step_val:
        arr.append([data['tof'][i],data['dipole_freq'][i]])
data_arr = data_arr[1:]
print(np.shape(data_arr[0]))

plt.figure('step_value_epics_'+str(desc_vals[0]))
plt.plot(np.array(data_arr[0])[:,1], np.array(data_arr[0])[:,0], 'bo')
plt.ylim(90,150)
plt.show()