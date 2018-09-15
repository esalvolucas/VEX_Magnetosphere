#READS VEX MAG DATA FROM FILES


import numpy as np
import pandas as pd

#with open('MAG_20071004_DOY277_D001_V1.TAB') as f:
pd.set_option('display.width', None)
with open('MAG_20071004_DOY277_D001_V1.TAB') as f:
    table = pd.read_csv(f,delim_whitespace=True,index_col=0,header=None,names = ['UTC','Bx','By','Bz','|B|','XSC','YSC','ZSC','RSC'],skiprows=300,encoding ='latin1')
    #df = pd.DataFrame(table, columns=['A', 'B', 'C', 'D'])
print(table)
