import pandas as pd
import numpy as np

def aberration(table):
    #make copy of VSE table
    ab_table = table.copy()
    #for each time in table
    for time in table.index:
        #set aberration angle at Venus (6 degrees) in radians
        theta = -0.104719755
        
        #establish rotation matrix (rotate around z-axis)
        c,s = np.cos(theta), np.sin(theta)
        rot_ab = np.array(((c,-s,0),
                           (s,c,0),
                           (0,0,1)))
        
        
        #rotate magnetic field and location values
        Bx = ab_table['Bx'][time]
        By = ab_table['By'][time]
        Bz = ab_table['Bz'][time]
        B = ab_table['|B|'][time]
        XSC = ab_table['XSC'][time]
        YSC = ab_table['YSC'][time]
        ZSC = ab_table['ZSC'][time]
        RSC = ab_table['RSC'][time]
        

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