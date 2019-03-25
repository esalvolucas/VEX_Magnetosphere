import pandas as pd
import numpy as np
from pandas.tslib import Timestamp
import matplotlib.pyplot as plt
from datetime import datetime
#from datetime import timedelta

def rotate_to_VSE(table,BS_in,BS_out,CA_select_in,CA_select_out):
    
    ### Calculate negative clock angle within BS
    z_mean1 = np.nanmean(CA_select_in['Bz'].values)
    y_mean1 = np.nanmean(CA_select_in['By'].values)
    clk_in = -np.arctan2(z_mean1,y_mean1)
    
    z_mean2 = np.nanmean(CA_select_out['Bz'].values)
    y_mean2 = np.nanmean(CA_select_out['By'].values)
    clk_out = -np.arctan2(z_mean2,y_mean2)
    
#     zmean = np.nanmean([z_mean1,z_mean2])
#     ymean = np.nanmean([y_mean1,y_mean2])
#     avg_clk = -np.arctan2(zmean,ymean)

    BS_in_t = str(table.index.values[BS_in])
    BS_out_t = str(table.index.values[BS_out])

    #create datetime values for BS in/out times
    BS_in_t = datetime(int(BS_in_t[0:4]),int(BS_in_t[5:7]),int(BS_in_t[8:10]),int(BS_in_t[11:13]),int(BS_in_t[14:16]),int(BS_in_t[17:19]))
    BS_out_t = datetime(int(BS_out_t[0:4]),int(BS_out_t[5:7]),int(BS_out_t[8:10]),int(BS_out_t[11:13]),int(BS_out_t[14:16]),int(BS_out_t[17:19]))
    
    #find duration of time outside the BS/inside the IMF
    avg_BS = BS_in_t + (BS_out_t - BS_in_t)/2

    #for each time in the index
    for time in table.index:
        if table['BS-rho'][time] > 0: #if inside BS
            if (time >= BS_in_t) and (time <= avg_BS):
                table['Clock'][time] = clk_in
            elif (time > avg_BS) and (time <= BS_out_t):
                table['Clock'][time] = clk_out
            
#         if table['BS-rho'][time] > 0:
#             table['Clock'][time] = avg_clk
            

    

    #copy VSO table to VSE table
    VSE_table = table
    #for each time, get clock angle
    for time in table.index:
        theta = table['Clock'][time]
        #perform 3D coordinate rotation about x-axis
        c,s = np.cos(theta), np.sin(theta)
        rot_VSE = np.array(((1,0,0),
                            (0,c,-s),
                            (0,s,c)))
        
        
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
       
#         if (table['BS-rho'][time]<0):
#             table['Bx'][time] = 10000
#             table['By'][time] = 10000
#             table['Bz'][time] = 10000
#             table['|B|'][time] = 10000
            
    return VSE_table 