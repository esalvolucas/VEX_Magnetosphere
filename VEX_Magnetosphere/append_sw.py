import pandas as pd
import numpy as np
from pandas.tslib import Timestamp
from datetime import datetime,timedelta

    
def append_sw(table,swdata):
    #append solar wind pressure data onto table using table's indices
    indices = table.index.values
    table['Pressure'] = swdata['pressure'][indices]
    
    return table