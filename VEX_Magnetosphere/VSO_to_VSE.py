import pandas as pd
import numpy as np
from pandas.tslib import Timestamp
import matplotlib.pyplot as plt
from datetime import timedelta

def VSO_to_VSE(table,CA_select_in,CA_select_out):
    
    z_mean1 = np.nanmean(CA_select_in['Bz'].values)
    y_mean1 = np.nanmean(CA_select_in['By'].values)
    clk_in = -np.arctan2(z_mean1,y_mean1)
    
    z_mean2 = np.nanmean(CA_select_out['Bz'].values)
    y_mean2 = np.nanmean(CA_select_out['By'].values)
    clk_out = -np.arctan2(z_mean2,y_mean2)
    
    zmean = np.nanmean([z_mean1,z_mean2])
    ymean = np.nanmean([y_mean1,y_mean2])
    avg_clk = -np.arctan2(zmean,ymean)
    
    BS_in_t = CA_select_in.index[0]
    BS_out_t = CA_select_out.index[-1]
    print(BS_in_t,BS_out_t)
    
    
    #########################
    #model bow shock
    L = 1.303
    epsilon = 1.056
    x0 = 0.788
    x = table['XSC'].values
    
    #spacecraft location sqrt(YSC^2 + ZSC^2)
    rho = np.sqrt((table['YSC'].values)**2 + (table['ZSC'].values)**2)
    BS = []
    for xval in x:
        #if VEX is outside of the BS (past the subsolar point), BS = 0
        if xval > 1.39:
            xx = 0
        else:
            xx = 1.1*np.sqrt(L**2 - 2*epsilon*(xval-x0)*L - (epsilon**2 - 1)*(xval-x0)**2) #10% safety buffer
        BS = BS + [xx]
    a = BS - rho
    #concatenate BS-rho onto existing dataframe
    a_table = pd.DataFrame(data={'time':table.index,'BS-rho':list(a)})
    a_table = a_table.set_index('time')
    table = table.join(a_table)
    ##################################
    
    #find duration of time outside the BS/inside the IMF
    avg_BS = Timestamp(BS_out_t.value) - Timestamp(BS_in_t.value)
    #strip date off of original data, modulo 24hrs to find halfway point inside BS
    avg_BS = Timestamp(str(BS_in_t)[0:11] + (str((timedelta(hours=24) - avg_BS)/2))[7:15])
    #find halfway point outside the BS
    halfway_BS = timedelta(hours=12) + avg_BS
    
    #for each time in the index
    for time in table.index:
        if table['BS-rho'][time] > 0: #if inside BS
            dt1 = abs((time - BS_out_t).total_seconds())
            dt2 = abs((time - BS_in_t).total_seconds())
            if dt1 > dt2:
                pass
#         if (time < BS_in_t) and (time >= avg_BS) and (table['BS-rho'][time] > 0):
#             table['Clock'][time] = clk_in
#             #table['Clock'][time] = avg_clk
#         elif ((time > BS_out_t) or (time <= avg_BS)) and (table['BS-rho'][time] > 0):
#             table['Clock'][time] = clk_out
#             #table['Clock'][time] = avg_clk
            
#         if table['BS-rho'][time] > 0:
#             table['Clock'][time] = avg_clk
            
#         if (table['BS-rho'][time]<0):
#             table['Bx'][time] = 10000
#             table['By'][time] = 10000
#             table['Bz'][time] = 10000
#             table['|B|'][time] = 10000
    

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
       
    return VSE_table 