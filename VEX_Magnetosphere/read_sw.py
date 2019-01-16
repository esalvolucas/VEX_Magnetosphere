import pandas as pd
import numpy as np

def read_sw():
    data = pd.read_csv('./VEX_data_files/MomentsScan.ascii', header=None, 
                       skiprows=np.arange(0,23), delim_whitespace=True,
                       index_col=0,names=["UTC","density", "speed", "temperature","flag"])
    data = data.set_index(pd.DatetimeIndex(data.index))

    return data
