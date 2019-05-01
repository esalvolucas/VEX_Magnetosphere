import pandas as pd
import glob

def orbit_load(orbit_num):
    #establish 4-digit orbit number
    orbit_num = str(orbit_num).zfill(4)
    #prevent dataframe output wrapping
    pd.set_option('display.width', None)
    #open file, read into pandas dataframe
    path = "./VEX_data_files/VSE/ORBIT_"+orbit_num+"_BS_*"
    for filename in glob.glob(path):
        print(filename)
        with open(filename) as f:
            table = pd.read_csv(f,sep='\t',index_col=0,header=None,names = ['UTC','Bx','By','Bz','|B|','XSC','YSC','ZSC','RSC','Clock','Cone','BS-rho'])
            #set UTC column to datetimeindex
            table = table.set_index(pd.DatetimeIndex(table.index))
        f.close()
    return table
