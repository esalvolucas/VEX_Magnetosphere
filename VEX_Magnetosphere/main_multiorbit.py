from VEX_Magnetosphere import *
from pandas.tslib import Timestamp
from _datetime import time
from datetime import date, timedelta
import matplotlib.pyplot as plt
from VEX_Magnetosphere import magnetosphere_mmo
import matplotlib.colors
import numpy as np
from matplotlib import ticker

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
        #add_venus_2D((0,0), 1, angle=0, ax=ax1, colors=('k','k'))
        #add_venus_2D((0,0), 1, angle=0, ax=ax2, colors=('k','k'))
        venus1=plt.Circle((0,0),1,color='k',fill=False)
        venus2=plt.Circle((0,0),1,color='k',fill=False)
        ax1.add_artist(venus1)
        ax2.add_artist(venus2)
        cax = plt.axes([0.93, 0.1, 0.020, 0.8])
        plt.subplots_adjust(bottom=0.1, left=0.07, right=0.91, top=0.9)
        for orbit in orbits:
            print(orbit)
            try:
                dates_file = mag_concat(orbit,orbit)
            except:
                continue
            table = vex_load_data(dates_file,disp=False)
            table = table.resample('T').mean()
            table = clock_cone_angle(table)
            table['XSC'] = table['XSC']/6051.8
            table['YSC'] = table['YSC']/6051.8
            table['ZSC'] = table['ZSC']/6051.8
            table['RSC'] = table['RSC']/6051.8
            #table = table.where((table['XSC']<-1)&(table['XSC']>-2))
            #print(table)
            table1 = table.where((table['XSC']<-1)&(table['XSC']>-2))
            ax1.scatter(table1['YSC'],table1['ZSC'],c=table1['Bx'],cmap='seismic',vmin=-20,vmax=20)
            
            try:
                CA_select_in,CA_select_out = magnetosphere_mmo(table)
            except:
                continue
                #CA_select_in,CA_select_out = magnetosphere(table)

            try:
                VSE_table = VSO_to_VSE(table,CA_select_in,CA_select_out)
                VSE_table = VSE_table.where((VSE_table['XSC']<-1)&(VSE_table['XSC']>-2))
                #print(VSE_tab                                                                         le.loc[(VSE_table['XSC'] > -2) & VSE_table['XSC'] < -1])
                #print(VSE_table.where(VSE_table['XSC'].values<=-1 and VSE_table['XSC'].values>-2))
                ax2.scatter(VSE_table['YSC'],VSE_table['ZSC'],c=VSE_table['Bx'],cmap='seismic',vmin=-20,vmax=20)
                ax1.set_xlabel('YSC')
                ax1.set_ylabel('ZSC')
                ax1.set_title('VSO')
                ax2.set_xlabel('YSC')
                ax2.set_ylabel('ZSC')
                ax2.set_title('VSE')
            except:
                continue

        cmap = plt.get_cmap('seismic')
        #o_mags = VSE_table['Bx'].values
        bounds = np.linspace(-20, 20, 60)
        norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
        cb = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, ticks=bounds, orientation='vertical')
        cb.set_label(r'$B_{x}$ Strength (nT)')
        tick_locator = ticker.MaxNLocator(nbins=11)
        cb.locator = tick_locator
        cb.update_ticks()
         
        ax1.set_xlim(-2,2)
        ax2.set_xlim(-2,2)
        ax1.set_ylim(-2,2)
        ax2.set_ylim(-2,2)
        
        #ax1.axis('equal')
        #ax2.axis('equal')
        plt.show()
        
        
        
def orbit_delta_list(start_time,end_time):
    orbits=[]
    s_ts = Timestamp(start_time)
    e_ts = Timestamp(end_time)
    delta = e_ts - s_ts
    for i in range(delta.days + 1):
        orbits = orbits + [str(s_ts + timedelta(i))]
        
    return orbits

main_multiorbit('2013-05-07 00:00:00','2013-05-10 00:00:00')
#main_multiorbit('2006-04-24 00:00:00','2014-11-25 00:00:00')