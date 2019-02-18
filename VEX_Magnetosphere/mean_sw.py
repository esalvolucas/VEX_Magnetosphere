import numpy as np
import pandas as pd
from datetime import timedelta
from pandas.tslib import Timestamp
from VEX_Magnetosphere import *

def mean_sw(data):
    
    data = data.resample('T').mean()
    data = data.interpolate(method='nearest')
    print(data)
    
    return data