from VEX_Magnetosphere import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pytplot
import pydivide
from pydivide import bin

def code_test(start_time,end_time):
    #GRAB RELEVANT FILES IN DATE RANGE
    dates_file = mag_concat(start_time,end_time)
    
    #LOAD DATA INTO PANDAS DATAFRAME
    table = vex_load_data(dates_file,disp=False)
    table = table.resample('T').mean()
    table = clock_cone_angle(table)
    
    
    #table = table.where((table['XSC']<-1)&(table['XSC']>-2))
    #print(table)
    
    #vex_plot_data(table)
    
    
    CA_select_in,CA_select_out = magnetosphere(table)
    
    VSE_table = VSO_to_VSE(table,CA_select_in,CA_select_out)
    #print(VSE_table)
    #print(len(VSE_table.index))
    #pytplot.store_data('vexmag',data={'x':list(str(VSE_table.index)),'y':[VSE_table['XSC'].values,VSE_table['YSC'].values,
    #                                                                   VSE_table['ZSC'].values,VSE_table['RSC'].values,
    #                                                                   VSE_table['Bx'].values,VSE_table['By'].values,
    #                                                                   VSE_table['Bz'].values,VSE_table['|B|'].values,
    #                                                                   VSE_table['Clock'].values,VSE_table['Cone'].values]})
    #print(pytplot.data_quants['vexmag'].data)
    VSE_binavg_x = bin(VSE_table,'Bx',['XSC','YSC','ZSC'],avg=True,binsize=[0.1,0.1,0.1])
    print(VSE_binavg_x)
    #bin_3d(VSE_table)
    
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
    #PLOT 1-MINUTE CADENC VSO DATA (3D)
    #VSO_3D_avg(table)

    #print(VSE_table['XSC'])
    #vex_plot_data(VSE_table)
    #plt.scatter(VSE_table['Bx'],VSE_table['By'],c=VSE_table['Bz'],cmap='jet')
    #plt.show()
code_test('2013-05-21 00:00:00','2013-05-21 00:00:00')
#code_test('2014-10-02 00:00:00','2014-10-02 00:00:00')