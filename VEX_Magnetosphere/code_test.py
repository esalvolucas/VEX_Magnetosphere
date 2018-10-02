import VEX_Magnetosphere

def code_test(start_time,end_time):
    #grab any relevant files in date range
    dates_file = VEX_Magnetosphere.mag_concat(start_time,end_time)
    
    #load data into Pandas DataFrame
    table = VEX_Magnetosphere.vex_load_data(dates_file,disp=False)
    
    #trim data to HH:MM:SS time range
    #table = VEX_Magnetosphere.date_vetting(table,start_time,end_time)
    
    #make raw mag/location plots
    #VEX_Magnetosphere.vex_plot_data(table)
    
    #make mag data vs orbit plot data
    #VEX_Magnetosphere.orbit_mag_plot(table)
    
    #make 3D orbit plot
    VEX_Magnetosphere.plot_3D(table)
    
    
code_test('2011-03-04 00:00:00','2011-03-04 00:00:00')