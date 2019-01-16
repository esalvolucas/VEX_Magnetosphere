import pandas as pd
import numpy as np
from pandas.tslib import Timestamp


def append_sw(table,data,CA_select_in,CA_select_out):
    
    #establish where ends of selections are
    BS_in_t = CA_select_in.index[0]
    BS_in_t2 = CA_select_in.index[-1]
    BS_out_t = CA_select_out.index[-1]
    BS_out_t2 = CA_select_out.index[0]
    
    #separate inbound/outbound BS data
    data_in = data[(data.index > BS_in_t) & (data.index < BS_in_t2)]
    data_out = data[(data.index > BS_out_t2) & (data.index < BS_out_t)]
    
    #take means of columns within in/outbound data
    density_in = np.nanmean(data_in['density'].values)
    speed_in = np.nanmean(data_in['speed'].values)
    temp_in = np.nanmean(data_in['temperature'].values)
    
    density_out = np.nanmean(data_out['density'].values)
    speed_out = np.nanmean(data_out['speed'].values)
    temp_out = np.nanmean(data_out['temperature'].values)
    
    #find halfway point in orbit
    avg_BS = Timestamp((BS_in_t.value + BS_out_t.value)/2.0)
    #make new columns in data table
    table['density'] = np.nan
    table['speed'] = np.nan
    table['temperature'] = np.nan
    
    #(nearest neighbor interpolation)
    for time in table.index:        
        if time < avg_BS:
            table['density'][time] = density_in
            table['speed'][time] = speed_in
            table['temperature'][time] = temp_in
        else:
            table['density'][time] = density_out
            table['speed'][time] = speed_out
            table['temperature'][time] = temp_out