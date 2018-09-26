import VEX_Magnetosphere
import os

dates_file = VEX_Magnetosphere.mag_concat('2013-05-21','2013-08-07')
table = VEX_Magnetosphere.vex_load_data(dates_file,disp=False)
VEX_Magnetosphere.vex_plot_data(table)
try:
    os.remove(dates_file)
except:
    pass
