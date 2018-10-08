import VEX_Magnetosphere

def code_test(start_time,end_time):
    #GRAB RELEVANT FILES IN DATE RANGE
    dates_file = VEX_Magnetosphere.mag_concat(start_time,end_time)
    
    #LOAD DATA INTO PANDAS DATAFRAME
    table = VEX_Magnetosphere.vex_load_data(dates_file,disp=False)
    
    #TRIM DATA TO THE SPECIFIED HH:MM:SS RANGE
    #table = VEX_Magnetosphere.date_vetting(table,start_time,end_time)

    #MAKE RAW LOCATION/MAG PLOTS
    #VEX_Magnetosphere.vex_plot_data(table)
    
    #PLOT SAMPLED MAG VS ORBIT DATA
    #VEX_Magnetosphere.VSO_xyz_mag(table)

    #PLOT SAMPLED MAG VS ORBIT DATA INDIVIDUALLY
    #VEX_Magnetosphere.orbit_mag_plot_xy(table)    
    #VEX_Magnetosphere.orbit_mag_plot_xz(table)
    #VEX_Magnetosphere.orbit_mag_plot_yz(table)

    #PLOT 3D ORBIT VS MAG DATA
    #VEX_Magnetosphere.plot_3D(table)
    
    #PLOT 1-MINUTE CADENCE VSO DATA (2D)
    #VEX_Magnetosphere.VSO_avg(table)
    
    #PLOT 1-MINUTE CADENC VSO DATA (3D)
    VEX_Magnetosphere.VSO_3D_avg(table)
    
#code_test('2014-10-02 00:00:00','2014-10-02 00:00:00')
code_test('2014-10-02 00:00:00','2014-10-02 00:00:00')