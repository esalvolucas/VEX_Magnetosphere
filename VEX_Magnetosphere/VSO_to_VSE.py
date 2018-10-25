import pandas as pd
import numpy as np
from pandas.tslib import Timestamp

def VSO_to_VSE(table,CA_select_in,CA_select_out):
    
    z_mean = np.nanmean(CA_select_in['Bz'].values)
    y_mean = np.nanmean(CA_select_in['By'].values)
    clk_in = np.arctan(z_mean/y_mean)
    
    z_mean = np.nanmean(CA_select_out['Bz'].values)
    y_mean = np.nanmean(CA_select_out['By'].values)
    clk_out = np.arctan(z_mean/y_mean)
    
    BS_in_t = CA_select_in.index[0]
    BS_out_t = CA_select_out.index[-1]
    
    #print(BS_in_t, BS_out_t)
    avg_BS = Timestamp((BS_in_t.value + BS_out_t.value)/2.0)
    
    
    for time in table.index:        
        if time > BS_in_t and time < BS_out_t:
            if time < avg_BS:
                table['Clock'][time] = clk_in
            else:
                table['Clock'][time] = clk_out
    
    #print(table['Clock'])
    #print((BS_in_t + BS_out_t)/2)
    
    VSE_table = table
    for time in table.index:
        theta = table['Clock'][time]
        
        c,s = np.cos(theta), np.sin(theta)
        rot_VSE = np.array(((1,0,0),(0,c,-s),(0,s,c)))
        
        
        Bx = table['Bx'][time]
        By = table['By'][time]
        Bz = table['Bz'][time]
        B = table['|B|'][time]
        XSC = table['XSC'][time]
        YSC = table['YSC'][time]
        ZSC = table['ZSC'][time]
        RSC = table['RSC'][time]
        

        mag_VSO = np.array(((Bx),(By),(Bz)))
        mag_VSE = np.matmul(rot_VSE,mag_VSO)
        
        VSE_table['Bx'][time] = mag_VSE[0]
        VSE_table['By'][time] = mag_VSE[1]
        VSE_table['Bz'][time] = mag_VSE[2]
        VSE_table['|B|'][time] = np.sqrt(mag_VSE[0]**2 + mag_VSE[1]**2 + mag_VSE[2]**2)

        sc_VSO = np.array(((XSC),(YSC),(ZSC)))
        sc_VSE = np.matmul(rot_VSE,sc_VSO)
    
        VSE_table['XSC'][time] = sc_VSE[0]
        VSE_table['YSC'][time] = sc_VSE[1]
        VSE_table['ZSC'][time] = sc_VSE[2]
        VSE_table['RSC'][time] = np.sqrt(sc_VSE[0]**2 + sc_VSE[1]**2 + sc_VSE[2]**2)
       
    return VSE_table 
    #print(clk_in,clk_out)