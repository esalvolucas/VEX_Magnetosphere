from VEX_Magnetosphere import *
from pandas.tslib import Timestamp
from _datetime import time
from datetime import date, timedelta
import matplotlib.pyplot as plt
from VEX_Magnetosphere import magnetosphere_mmo

def main_multiorbit(start_time,end_time,
                    catorbit=None,
                    obo=True,
                    raw=None,
                    avg2d=None,
                    avg3d=None,
                    VSE=None):
    #if orbit-by-orbit (not concat)
    if catorbit==None:
        orbits = orbit_delta_list(start_time, end_time)
        print(orbits)
        fig,(ax1,ax2) = plt.subplots(nrows=1, ncols=2)
        for orbit in orbits:
            dates_file = mag_concat(orbit,orbit)
            table = vex_load_data(dates_file,disp=False)
            table = table.resample('T').mean()
            table = clock_cone_angle(table)
            table['XSC'] = table['XSC']/6051.8
            table['YSC'] = table['YSC']/6051.8
            table['ZSC'] = table['ZSC']/6051.8
            table['RSC'] = table['RSC']/6051.8

            #table = table.where((table['XSC']<-1)&(table['XSC']>-2))
            ax1.scatter(table['YSC'],table['ZSC'],c=table['Bx'],cmap='jet')
            
            CA_select_in,CA_select_out = magnetosphere_mmo(table)
            

            VSE_table = VSO_to_VSE(table,CA_select_in,CA_select_out)
            VSE_table = VSE_table.where((VSE_table['XSC']<-1)&(VSE_table['XSC']>-2))
            #print(VSE_table.loc[(VSE_table['XSC'] > -2) & VSE_table['XSC'] < -1])
            #print(VSE_table.where(VSE_table['XSC'].values<=-1 and VSE_table['XSC'].values>-2))
            ax2.scatter(VSE_table['YSC'],VSE_table['ZSC'],c=VSE_table['Bx'],cmap='jet')
            ax1.set_xlabel('By')
            ax1.set_ylabel('Bz')
            ax1.set_title('VSO Bx')
            ax2.set_xlabel('By')
            ax2.set_ylabel('Bz')
            ax2.set_title('VSE by Bx')
#             ax1.set_xlim(-2.5,-1.5)
#             ax2.set_xlim(-2.5,-1.5)
#             ax1.set_ylim(-1,1)
#             ax2.set_ylim(-1,1)
        plt.show()
        
        
        
def orbit_delta_list(start_time,end_time):
    orbits=[]
    s_ts = Timestamp(start_time)
    e_ts = Timestamp(end_time)
    delta = e_ts - s_ts
    for i in range(delta.days + 1):
        orbits = orbits + [str(s_ts + timedelta(i))]
        
    return orbits

main_multiorbit('2013-05-07 00:00:00','2013-05-27 00:00:00')