import numpy as np
import pandas as pd

def clock_cone_angle(table):
    #calculate clock and cone angle
    clk_angle = np.arctan2(table['Bz'],table['By'])
    cone_angle = np.arctan2(table['Bx'],table['By'])
    clk = pd.DataFrame({'Clock':-clk_angle})
    cone = pd.DataFrame({'Cone':cone_angle})
    
    #concatenate to dataframe
    table = table.join(clk)
    table = table.join(cone)
    
    return table