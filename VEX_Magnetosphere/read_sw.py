import pandas as pd
import numpy as np

def read_sw(flag=None):
    #read in data from MomentsScan.ascii, skip header
    data = pd.read_csv('./VEX_data_files/MomentsScan.ascii', header=None, 
                       skiprows=np.arange(0,23), delim_whitespace=True,
                       index_col=0,names=["UTC","density", "speed", "temperature","flag"])
    #set datetime index
    data = data.set_index(pd.DatetimeIndex(data.index))
    #append dynamic pressure
    #pdyn = mass_proton * conversion to m * 1/2 * rho * v^2
    pressure = 1.67*10**(-27)*(100**3)*(1000**2)*0.5*data['density']*data['speed']**2 #in Pa
    swpressure = pd.DataFrame(index=data.index,data={'pressure':pressure})
    data = data.join(swpressure)
    #resample to 1m cadence with average
    data = data.resample('T').mean()
    #nearest neighbor interpolate between pressures and data validity flags
    data['pressure'] = data['pressure'].interpolate(method='nearest')
    data['speed'] = data['speed'].interpolate(method='nearest')
    data['flag'] = data['flag'].interpolate(method='nearest')

    #if specific flags selected
    if flag is not None:
            if isinstance(flag,int):
                flag = [flag]
            data = data[data['flag'].isin(flag)]
        
    return data