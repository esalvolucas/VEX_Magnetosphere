import numpy as np
import pandas as pd
from datetime import timedelta
from pandas.tslib import Timestamp
from VEX_Magnetosphere import *

def mean_sw(data):
    t_orig = data.index
    t_shift = np.roll(t_orig,-1)
    t_delta = t_shift - t_orig
    
    print(t_delta)
    split_i = np.where(t_delta > timedelta(hours=1))
    split_i = split_i[0]#[0:-1]
    split_i_1 = split_i[0:-1]
    print(split_i)
    for i,val in enumerate(split_i_1):
        print(val)
        print(np.arange(split_i[i],split_i[i+1],1))
        #print(split_i[i],split_i[i+1])
        section = np.arange(split_i[i],split_i[i+1],1)
        time = data.index[section].mean()
        density = np.nanmean(data['density'][section])
        speed = np.nanmean(data['speed'][section])
        temperature = np.nanmean(data['temperature'][section])
        print(time,density,speed,temperature)
    
data = read_sw(flag=[0,1])
mean_sw(data)