import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def clock_cone_angle(table):
    #calculate clock and cone angle
    clk_angle = np.arctan(table['Bz']/table['By'])
    cone_angle = np.arctan(table['Bx']/table['By'])
    clk = pd.DataFrame({'Clock':clk_angle})
    cone = pd.DataFrame({'Cone':cone_angle})
    
    #concatenate to dataframe
    table = table.join(clk)
    table = table.join(cone)
    
    return table