import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.getcwd()
os.listdir()

data = pd.read_csv('run10109.csv',sep = ',')

step_val = 0.0
stop = False
desc_vals=[]
step_start = []
for i in range(len(data['event'])):
    desc = float(data['step_value_epics'][i][1:-1])
    if  desc != step_val:
        if stop == True:
            step_start.append(i)
            break
        desc_vals.append(desc)
        step_start.append(i)
        step_val = desc
        if desc == 2100.0:
            stop = True

plt.figure("Sakshi's Best Plot Ever")
plt.clf()
for i in range(len(step_start)-1):
    data_group = data[step_start[i]:step_start[i+1]].groupby('dipole_freq')['tof'].mean()
    plt.plot(data_group,'-o')