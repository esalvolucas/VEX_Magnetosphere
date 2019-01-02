import pandas as pd
import numpy as np
#from __future__ import division
import glob
import os

def load_data(date):
    
    date = date[0:10]
    
    #for each file in MAG data directory path
    #MAC
    #dir_path = "/Volumes/Venus_Express/calibrated_level_3/**/DATA/**/*.TAB"
    #WINDOWS
    dir_path = "D:/calibrated_level_3/**/DATA/**/*.TAB"
    #dir_path = "./VEX_data_files/*.TAB"
    for filename in glob.iglob(dir_path,recursive=True):
        #remove hyphens
        date = date.replace('-','')
        filedate = (os.path.basename(filename))[4:12]
        #print(date)
        #print(filedate)
        #find files in between start/stop times
        if filedate == date:
     
            table = pd.read_csv(filename,skiprows=range(0,226),delim_whitespace=True,index_col=0,header=None,names = ['UTC','Bx','By','Bz','|B|','XSC','YSC','ZSC','RSC'])
            table[(table>=99999)|(table<=-99999)] = np.nan
            #set UTC column to datetimeindex
            table = table.set_index(pd.DatetimeIndex(table.index))
            print(table)

load_data("2014-05-27")