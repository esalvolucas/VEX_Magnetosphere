import numpy as np
import pandas as pd
import glob
from VEX_Magnetosphere import *

def orbit_load(orbit_num):
    #remove column wrapping output
    orbit_num = str(orbit_num).zfill(4)
    pd.set_option('display.width', None)
    #open file, read into pandas dataframe
    path = "./VEX_data_files/ORBIT_"+orbit_num+"_BS_*"
    for filename in glob.glob(path):
        BS_in = int(filename[31:34])
        BS_out = int(filename[35:38])
        with open(filename) as f:
            table = pd.read_csv(f,delim_whitespace=True,index_col=0,header=None,names = ['UTC','Bx','By','Bz','|B|','XSC','YSC','ZSC','RSC','Clock','Cone','BS-rho'])

    #set UTC column to datetimeindex
    table = table.set_index(pd.DatetimeIndex(table.index))
    print(table)
    return table,BS_in,BS_out

table,BS_in,BS_out = orbit_load(0000)
print(table.iloc[BS_in],table.iloc[BS_out])