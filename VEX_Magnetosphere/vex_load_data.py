#READS VEX MAG DATA FROM FILES


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def vex_load_data(filename,disp=False):
    #remove column wrapping output
    pd.set_option('display.width', None)
    #open file, read into pandas dataframe
    with open(filename) as f:
        table = pd.read_csv(f,delim_whitespace=True,index_col=0,header=None,names = ['UTC','Bx','By','Bz','|B|','XSC','YSC','ZSC','RSC'],skiprows=177)
    #clip outliers
    table[(table>=99999)|(table<=-99999)] = np.nan
    #set UTC column to datetimeindex
    table = table.set_index(pd.DatetimeIndex(table.index))
    if disp==True:
        print(table.iloc[0])
    return table
