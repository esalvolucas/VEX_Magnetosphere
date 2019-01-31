import pandas as pd
import numpy as np

def read_sw(flag=None,density=None,speed=None,temp=None):
    #read in data from MomentsScan.ascii, skip header
    data = pd.read_csv('./VEX_data_files/MomentsScan.ascii', header=None, 
                       skiprows=np.arange(0,23), delim_whitespace=True,
                       index_col=0,names=["UTC","density", "speed", "temperature","flag"])
    #set datetime index
    data = data.set_index(pd.DatetimeIndex(data.index))
    #if specific flags selected
    if flag is not None:
            if isinstance(flag,int):
                flag = [flag]
            data = data[data['flag'].isin(flag)]
    #pick density within range
    if density is not None:
        dmin,dmax = density[0],density[1]
        print(dmin,dmax)
        data = data[(data['density']>=dmin)&(data['density']<=dmax)]
    #pick speed within range  
    if speed is not None:
        vmin,vmax = speed[0],speed[1]
        print(vmin,vmax)
        data = data[(data['speed']>=vmin)&(data['speed']<=vmax)]
    #pick temperature within range
    if temp is not None:
        tmin,tmax = temp[0],temp[1]
        print(tmin,tmax)
        data = data[(data['temperature']>=tmin)&(data['temperature']<=tmax)]
        
    return data

#print(read_sw(flag=4,density=[30,50]))