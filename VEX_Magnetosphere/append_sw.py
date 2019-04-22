import pandas as pd
import numpy as np
from pandas.tslib import Timestamp
from datetime import datetime,timedelta

    
def append_sw(table,swdata):
    #table['Density'] = np.nan
    #table['Speed'] = np.nan
    #table['Temperature'] = np.nan
    
    indices = swdata.index.values
    
    table['Density'] = swdata['density'][indices]
    table['Speed'] = swdata['speed'][indices]
    table['Temperature'] = swdata['temperature'][indices]
    table['Pressure'] = swdata['pressure'][indices]
    
    return table