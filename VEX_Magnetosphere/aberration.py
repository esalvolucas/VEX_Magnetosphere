import pandas as pd
import numpy as np

def aberration(table):
    ab_table = table
    for time in table.index:
        theta = -0.104719755
        
        c,s = np.cos(theta), np.sin(theta)

        rot_ab = np.array(((c,-s,0),
                            (s,c,0),
                            (0,0,1)))
        
        
        Bx = table['Bx'][time]
        By = table['By'][time]
        Bz = table['Bz'][time]
        B = table['|B|'][time]
        XSC = table['XSC'][time]
        YSC = table['YSC'][time]
        ZSC = table['ZSC'][time]
        RSC = table['RSC'][time]
        

        mag_VSO = np.array(((Bx),(By),(Bz)))
        mag_ab = np.matmul(rot_ab,mag_VSO)
        
        ab_table['Bx'][time] = mag_ab[0]
        ab_table['By'][time] = mag_ab[1]
        ab_table['Bz'][time] = mag_ab[2]
        ab_table['|B|'][time] = np.sqrt(mag_ab[0]**2 + mag_ab[1]**2 + mag_ab[2]**2)

        sc_VSO = np.array(((XSC),(YSC),(ZSC)))
        sc_ab = np.matmul(rot_ab,sc_VSO)
    
        ab_table['XSC'][time] = sc_ab[0]
        ab_table['YSC'][time] = sc_ab[1]
        ab_table['ZSC'][time] = sc_ab[2]
        ab_table['RSC'][time] = np.sqrt(sc_ab[0]**2 + sc_ab[1]**2 + sc_ab[2]**2)
       
    return ab_table 
    #print(clk_in,clk_out)