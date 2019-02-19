import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from VEX_Magnetosphere import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pytplot
import pydivide
from pydivide import bin
from scipy import stats
import _pickle as cPickle

def code_test(orbit):
    
    
    #GRAB RELEVANT FILES IN DATE RANGE
    #dates_file = mag_concat(start_time,end_time)
    dates_file = './VEX_data_files/' + orbit[0:10] + '_TO_' + orbit[0:10] + '.tab' 
    #LOAD DATA INTO PANDAS DATAFRAME
    table = vex_load_data(dates_file,disp=False)
    table = table.resample('T').mean()
    table = clock_cone_angle(table)
    #plt.plot(table['Clock'])
      
      
    table['XSC'] = table['XSC']/6051.8
    table['YSC'] = table['YSC']/6051.8
    table['ZSC'] = table['ZSC']/6051.8
    table['RSC'] = table['RSC']/6051.8
      
      
      
    #table = table.where((table['YSC']<=2)&(table['YSC']>=-2))
    #table = table.where((table['ZSC']<=2)&(table['ZSC']>=-2))
    #print(table)
    #vex_plot_data(table)
      
   
    CA_select_in,CA_select_out = magnetosphere(table)
    table = aberration(table)
    VSE_table = VSO_to_VSE(table,CA_select_in,CA_select_out)
    print(VSE_table)
    swdata = read_sw(flag=[0,1])
    swdata = mean_sw(swdata)
    VSE_table = append_sw(VSE_table,swdata)
    print(VSE_table)
    #VSE_table = append_sw(VSE_table,data,CA_select_in,CA_select_out)
#     #pd.set_option('display.max_rows', 10000)
#     print(VSE_table)
    #plt.plot(table['Clock'])
    #plt.show()
    #VSE_table = VSE_table.where((VSE_table['XSC']<-1)&(VSE_table['XSC']>-2))

    
#     plt.plot(table.index,table['Clock'])
#     plt.plot(CA_select_in.index,CA_select_in['Clock'])
#     plt.plot(CA_select_out.index,CA_select_out['Clock'])
#     plt.show()
    #clk_in = CA_select_in['
    #TRIM DATA TO THE SPECIFIED HH:MM:SS RANGE
    #table = date_vetting(table,start_time,end_time)

    #MAKE RAW LOCATION/MAG PLOTS
    
    
    #PLOT SAMPLED MAG VS ORBIT DATA
    #VSO_xyz_mag(table)

    #PLOT SAMPLED MAG VS ORBIT DATA INDIVIDUALLY
    #orbit_mag_plot_xy(table)    
    #orbit_mag_plot_xz(table)
    #orbit_mag_plot_yz(table)

    #PLOT 3D ORBIT VS MAG DATA
    #plot_3D(table)
    
    #PLOT 1-MINUTE CADENCE VSO DATA (2D)
    #VSO_avg(table)
    #VSO_avg(VSE_table,VSE=True)
    #PLOT 1-MINUTE CADENCE VSO DATA (3D)
    #VSO_3D_avg(table)

    #print(VSE_table['XSC'])
    #vex_plot_data(VSE_table)
    #plt.scatter(VSE_table['Bx'],VSE_table['By'],c=VSE_table['Bz'],cmap='jet')
    #plt.show()
code_test('2014-11-14 00:00:00')
#code_test('2014-10-02 00:00:00','2014-10-02 00:00:00')