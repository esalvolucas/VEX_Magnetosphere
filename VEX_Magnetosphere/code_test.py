from VEX_Magnetosphere import *
import pandas as pd
def code_test(start_time,end_time):
    #GRAB RELEVANT FILES IN DATE RANGE
    dates_file = mag_concat(start_time,end_time)
    
    #LOAD DATA INTO PANDAS DATAFRAME
    table = vex_load_data(dates_file,disp=False)
    table = table.resample('T').mean()
    table = clock_cone_angle(table)
    
    CA_select_in,CA_select_out = magnetosphere(table)
    #TRIM DATA TO THE SPECIFIED HH:MM:SS RANGE
    #table = date_vetting(table,start_time,end_time)

    #MAKE RAW LOCATION/MAG PLOTS
    #vex_plot_data(table)
    
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
    
    #PLOT 1-MINUTE CADENC VSO DATA (3D)
    #VSO_3D_avg(table)
    
code_test('2013-05-21 00:00:00','2013-05-21 00:00:00')
#code_test('2014-10-02 00:00:00','2014-10-02 00:00:00')