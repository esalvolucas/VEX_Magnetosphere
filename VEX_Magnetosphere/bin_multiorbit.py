from VEX_Magnetosphere import *
from pandas.tslib import Timestamp
from _datetime import time
from datetime import date, timedelta
import matplotlib.pyplot as plt
from VEX_Magnetosphere import magnetosphere_mmo
import matplotlib.colors
import numpy as np
from matplotlib import ticker
from pydivide import bin
from scipy import stats
import _pickle as cPickle


 
def bin_multiorbit_x(start_time,end_time):
     
    fig,ax = plt.subplots(nrows=1, ncols=1)
 
    orbits = orbit_delta_list(start_time, end_time)
    cax = plt.axes([0.85, 0.1, 0.05, 0.8])
     
    plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
     
    final_stat = np.zeros((60,60))
    final_nan = np.zeros((60,60))
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
        #table1 = table.where((table['XSC']<-1)&(table['XSC']>-2))
        #ax.scatter(table1['YSC'],table1['ZSC'],c=table1['Bx'],cmap='seismic',vmin=-20,vmax=20)
         
        try:
            CA_select_in,CA_select_out = magnetosphere_mmo(table)
        except:
            continue
            #CA_select_in,CA_select_out = magnetosphere(table)
 
        try:
            VSE_table = VSO_to_VSE(table,CA_select_in,CA_select_out)
            #VSE_table = VSE_table.where((VSE_table['XSC']<-1)&(VSE_table['XSC']>-2))
            insitu = {}
            insitu['VEX'] = VSE_table
            VSE_binavg_x = bin(insitu,'VEX.Bx',['VEX.XSC','VEX.YSC','VEX.ZSC'],avg=True,
                               binsize=[0.1,0.1,0.1],mins=[-3,-3,-3],maxs=[3,3,3])
            VSE_binavg_x = VSE_binavg_x[0]
            np.set_printoptions(threshold=np.nan)
            yz_arr = np.nanmean(VSE_binavg_x,axis=0)
            yz_nan = np.logical_not(np.isnan(yz_arr))*1
            #print(yz_nan)
            yz_arr[np.isnan(yz_arr)] = 0
            #final_stat = np.nansum(np.dstack((final_stat,yz_arr)),2)
            final_stat += yz_arr
            final_nan += yz_nan
            #VSE_table = VSE_table.where((VSE_table['XSC']<-1)&(VSE_table['XSC']>-2))
            #print(VSE_table.loc[(VSE_table['XSC'] > -2) & VSE_table['XSC'] < -1])
            #print(VSE_table.where(VSE_table['XSC'].values<=-1 and VSE_table['XSC'].values>-2))
        except:
            continue
 
    final_nan[np.where(final_nan==0)] = 1
    final_stat = np.divide(final_stat,final_nan)
    #print(np.shape(final_stat))
     
    #fig,ax = plt.subplots(nrows=1, ncols=1)
    #plt.gca().set_aspect('equal', adjustable='box')
#     yedges = np.arange(-3,3,0.1)
#     zedges = np.arange(-3,3,0.1)
#     ymesh,zmesh = np.meshgrid(yedges,zedges)
#     #print(ymesh)
#     #print(zmesh)
#     venus1=plt.Circle((0,0),1,color='k',fill=False)
#     ax.add_artist(venus1)
#     #plt.show()
#   
#     cmap = plt.get_cmap('seismic')
#     #o_mags = VSE_table['Bx'].values
#     bounds = np.linspace(-20, 20, 60)
#     norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
#     cb = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, ticks=bounds, orientation='vertical')
#     cb.set_label(r'$B_{x}$ Strength (nT)')
#     tick_locator = ticker.MaxNLocator(nbins=11)
#     cb.locator = tick_locator
#     cb.update_ticks()
    
    final_stat = final_stat.T
    
    ### PROBLEM: NEED TO STORE AVERAGED VSE_BINAVG_X (3D), NOT FINAL_STAT (2D)
    cPickle.dump(VSE_binavg_x, open("VEX_binx_3D.pkl", "wb" ))
    cPickle.dump(final_stat, open("VEX_binx_2D.pkl","wb"))
    print('Data dumped to .pkl file')
#     ymesh = ymesh.T
#     zmesh = zmesh.T
    
#     ax.pcolormesh(ymesh,zmesh,final_stat,cmap=cmap,vmin=-20,vmax=20)
#     #print(final_stat)
# 
# #      
#     ax.set_xlim(-3,3)
#     ax.set_ylim(-3,3)
#     ax.set(title='VEX Orbit MAG Data: ' + start_time + ' TO ' + end_time)
#     #ax.axis('equal')
#     plt.show()
    #ax1.axis('equal')
    #ax2.axis('equal')
       
  
  
def bin_multiorbit_y(start_time,end_time):
     
    fig,ax = plt.subplots(nrows=1, ncols=1)
 
    orbits = orbit_delta_list(start_time, end_time)
    cax = plt.axes([0.85, 0.1, 0.05, 0.8])
     
    plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
     
    final_stat = np.zeros((60,60))
    final_nan = np.zeros((60,60))
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
         
        try:
            CA_select_in,CA_select_out = magnetosphere_mmo(table)
        except:
            continue
 
        try:
            VSE_table = VSO_to_VSE(table,CA_select_in,CA_select_out)
            #VSE_table = VSE_table.where((VSE_table['XSC']<-1)&(VSE_table['XSC']>-2))
            insitu = {}
            insitu['VEX'] = VSE_table
            VSE_binavg_y = bin(insitu,'VEX.By',['VEX.XSC','VEX.YSC','VEX.ZSC'],avg=True,
                               binsize=[0.1,0.1,0.1],mins=[-3,-3,-3],maxs=[3,3,3])
            VSE_binavg_y = VSE_binavg_y[0]
            np.set_printoptions(threshold=np.nan)
            xz_arr = np.nanmean(VSE_binavg_y,axis=1)
            xz_nan = np.logical_not(np.isnan(xz_arr))*1
            xz_arr[np.isnan(xz_arr)] = 0
            final_stat += xz_arr
            final_nan += xz_nan

        except:
            continue
 
    final_nan[np.where(final_nan==0)] = 1
    final_stat = np.divide(final_stat,final_nan)
    
    final_stat = final_stat.T
    
    cPickle.dump(VSE_binavg_y, open("VEX_biny_01073D.pkl", "wb" ))
    cPickle.dump(final_stat, open("VEX_biny_01072D.pkl","wb"))
    print('Data dumped to .pkl file')
    
    
def bin_multiorbit_z(start_time,end_time):
     
    fig,ax = plt.subplots(nrows=1, ncols=1)
 
    orbits = orbit_delta_list(start_time, end_time)
    cax = plt.axes([0.85, 0.1, 0.05, 0.8])
     
    plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
     
    final_stat = np.zeros((60,60))
    final_nan = np.zeros((60,60))
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
         
        try:
            CA_select_in,CA_select_out = magnetosphere_mmo(table)
        except:
            continue
 
        try:
            VSE_table = VSO_to_VSE(table,CA_select_in,CA_select_out)
            #VSE_table = VSE_table.where((VSE_table['XSC']<-1)&(VSE_table['XSC']>-2))
            insitu = {}
            insitu['VEX'] = VSE_table
            VSE_binavg_z = bin(insitu,'VEX.Bz',['VEX.XSC','VEX.YSC','VEX.ZSC'],avg=True,
                               binsize=[0.1,0.1,0.1],mins=[-3,-3,-3],maxs=[3,3,3])
            VSE_binavg_z = VSE_binavg_z[0]
            np.set_printoptions(threshold=np.nan)
            xy_arr = np.nanmean(VSE_binavg_z,axis=1)
            xy_nan = np.logical_not(np.isnan(xy_arr))*1
            xy_arr[np.isnan(xy_arr)] = 0
            final_stat += xy_arr
            final_nan += xy_nan

        except:
            continue
 
    final_nan[np.where(final_nan==0)] = 1
    final_stat = np.divide(final_stat,final_nan)
    
    final_stat = final_stat.T
    
    cPickle.dump(VSE_binavg_z, open("VEX_binz_nightside3D.pkl", "wb" ))
    cPickle.dump(final_stat, open("VEX_binz_nightside2D.pkl","wb"))
    print('Data dumped to .pkl file')
         
def orbit_delta_list(start_time,end_time):
    orbits=[]
    s_ts = Timestamp(start_time)
    e_ts = Timestamp(end_time)
    delta = e_ts - s_ts
    for i in range(delta.days + 1):
        orbits = orbits + [str(s_ts + timedelta(i))]
         
    return orbits
 
#bin_multiorbit_x('2013-05-07 00:00:00','2013-08-07 00:00:00')
bin_multiorbit_y('2013-01-01 00:00:00','2013-07-01 00:00:00')
#bin_multiorbit_z('2013-05-07 00:00:00','2013-08-07 00:00:00')

#bin_multiorbit_x('2006-04-24 00:00:00','2014-11-25 00:00:00')
#bin_multiorbit_y('2006-04-24 00:00:00','2014-11-25 00:00:00')
#bin_multiorbit_z('2006-04-24 00:00:00','2014-11-25 00:00:00')

#main_multiorbit('2006-04-24 00:00:00','2014-11-25 00:00:00')