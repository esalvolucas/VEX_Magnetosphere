#import os
#import sys
#sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
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

def code_test():
    
    VSE_table = orbit_load(3136)
    swdata = read_sw(flag=[0,1])
    
    print(append_sw(VSE_table,swdata))
    #fig,ax = plt.subplots(111)
    #swpressure = 0.5*swdata['density']*swdata['speed']**2
    #print(swdata)
    #plt.yscale('log', nonposy='clip')
#     hmean = np.mean(np.log(swdata['pressure']))
#     hstd = (np.std(np.log(swdata['pressure']))*np.arange(-3,3,0.5)) + hmean
#     print(hstd)
#     for i in hstd:
#         plt.axvline(x=i,color='r')
#     
#     plt.axvline(x=hmean,color='g')
# 
#     plt.hist(np.log(swdata['pressure']),bins=200)
#     plt.show()
#     print(np.mean(np.log(swdata['pressure'])))
#     print(np.std(np.log(swdata['pressure'])))
#     
# # theta = -0.104719755
#  
# c,s = np.cos(theta), np.sin(theta)
#  
# rot_ab = np.array(((c,-s,0),
#                    (s,c,0),
#                    (0,0,1)))
# print(table)
# ab_table = np.matmul(rot_ab,table)
# print(ab_table)
# CA = np.arctan2(ab_table[2],ab_table[1])
# print(CA)
# c,s = np.cos(-CA), np.sin(-CA)
# rot_VSE = np.array(((1,0,0),
#                     (0,c,-s),
#                     (0,s,c)))
# mag_VSE = np.matmul(rot_VSE,ab_table)
# print(mag_VSE) 
    #for i in 
#     
# #     #table = pd.DataFrame(data={'time':0,'Bx':0,'By':1,'Bz':1,'|B|':np.sqrt(2),'XSC':0,'YSC':0,'ZSC':0,'RSC':0})
# #     #table = table.set_index('time')
# #     #print(table)
# #      
# #     table = np.array([0,1,1])
# #      
# #     z_mean = np.nanmean(table[2])
# #     y_mean = np.nanmean(table[1])
# #     clk_in = -np.arctan2(z_mean,y_mean)
# #     print(clk_in)
# #  
# #     theta = clk_in
# #      
# #     c,s = np.cos(theta), np.sin(theta)
# #     rot_VSE = np.array(((1,0,0),
# #                         (0,c,-s),
# #                         (0,s,c)))
# #      
# #      
# #     Bx = table[0]
# #     By = table[1]
# #     Bz = table[2]
# #     #B = np.sqrt(2)
# #      
# #      
# #  
# #     mag_VSO = np.array(((Bx),(By),(Bz)))
# #     mag_VSE = np.matmul(rot_VSE,mag_VSO)
# #     print(mag_VSE[1])
# #     print(rot_VSE)
# #     new_table = np.array([1.0,1.0,1.0])
# #     new_table[0] = mag_VSE[0]
# #     new_table[1] = mag_VSE[1]
# #     new_table[2] = mag_VSE[2]
# #  
# #     print(new_table)
    #GRAB RELEVANT FILES IN DATE RANGE
    #dates_file = mag_concat(start_time,end_time)
#     orbit = '2013-05-21'
#     dates_file = './VEX_Magnetosphere/VEX_data_files/' + orbit[0:10] + '_TO_' + orbit[0:10] + '.tab' 
#     #LOAD DATA INTO PANDAS DATAFRAME
#     table = vex_load_data(dates_file,disp=False)
#     table = table.resample('T').mean()
#     table = clock_cone_angle(table)
#     #plt.plot(table['Clock'])
#          
#          
#     table['XSC'] = table['XSC']/6051.8
#     table['YSC'] = table['YSC']/6051.8
#     table['ZSC'] = table['ZSC']/6051.8
#     table['RSC'] = table['RSC']/6051.8
#       
#     print(table)
#         
#         
#         
#     #table = table.where((table['YSC']<=2)&(table['YSC']>=-2))
#     #table = table.where((table['ZSC']<=2)&(table['ZSC']>=-2))
#     #print(table)
#     vex_plot_data(table)
        
    #pd.set_option('display.max_rows', 10000)
  
    #CA_select_in,CA_select_out = magnetosphere(table)
    #table = aberration(table)
    #print(table.iloc[0:10])
    #VSE_table = VSO_to_VSE(table,CA_select_in,CA_select_out)
#     for i,val in enumerate(VSE_table.index):
#         print(VSE_table['By'][val])
#         if VSE_table['By'][val]<0:
#             print('VSO')
#             print(table.iloc[i])
#             print('VSE')
#             print(VSE_table.iloc[i])
#             print('STOP')
#             break
#     #pos_table = VSE_table.where(VSE_table['By']>0)
#     #VSOpos = table.where(VSE_table['By']<=0)
#     #print(len(table))
#     #print(pos_table)
#     #print(VSOpos)
#     print(aaaaa)
#     swdata = read_sw(flag=[0,1])
#     swdata = mean_sw(swdata)
#     VSE_table = append_sw(VSE_table,swdata)
#     print(VSE_table)
#     VSE_table = append_sw(VSE_table,swdata,CA_select_in,CA_select_out)
#     print(VSE_table)
#     
#     
#     insitu = {}
#     insitu['VEX'] = VSE_table
#     #use pydivide.bin to bin data in 3D, bins of 0.1, between -3 and 3 Rv
# #             VSE_binavg,VSE_counts = bin(insitu,mag,['VEX.XSC','VEX.YSC','VEX.ZSC'],avg=True,
# #                                         density=True,binsize=[0.1,0.1,0.1],mins=[-3,-3,-3],
# #                                         maxs=[3,3,3])
#     VSE_binavg,VSE_counts = bin(insitu,mag,['VEX.XSC','VEX.YSC','VEX.ZSC'],avg=True,
#                                 density=True,binsize=[0.2,0.2,0.2],mins=[-3,-3,-3],
#                                 maxs=[3,3,3])
#     np.set_printoptions(threshold=np.nan)
#     #take mean of binned data on axis to collapse
#     xy_arr = np.nanmean(VSE_binavg,axis=collapse)
#     #print(xy_arr)
#     #counts bases binning off of data points/bin/orbit, instead of logical 1 or 0 for (data or no data)/orbit
#     if counts == False:
#         xy_nan = np.logical_not(np.isnan(xy_arr))*1
#         xy_arr[np.isnan(xy_arr)] = 0
#     if counts == True:
#         xy_nan = np.nansum(VSE_counts,axis=collapse)
#         xy_nan[np.isnan(xy_nan)] = 0
#     #add data to final arrays
#     final_stat = np.nansum(np.dstack((final_stat,xy_arr)),2)
#     #final_nan = 
#     #final_stat += xy_arr
#     #print(final_stat)
#     final_nan += xy_nan
# 
#     #replace any instances of 0 with 1 to not break np.divide
#     final_nan[np.where(final_nan==0)] = 1
#     #divide final data by final number of points per bin
#     final_stat = np.divide(final_stat,final_nan)
#     #transpose 2D data matrix
#     final_stat = final_stat.T
#     
#     #open pkl files, dump final data
#     output3D = open(pkl_name3D, "wb" )
#     output2D = open(pkl_name2D,"wb")
#     cPickle.dump(VSE_binavg, output3D)
#     cPickle.dump(final_stat, output2D)
#     print('Data dumped to:')
#     print(pkl_name2D)
#     print(pkl_name3D)
#     #close files
#     output3D.close()
#     output2D.close()
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
    VSO_avg(table)
    VSO_avg(VSE_table,VSE=True)
    #PLOT 1-MINUTE CADENCE VSO DATA (3D)
    #VSO_3D_avg(table)

    #print(VSE_table['XSC'])
    #vex_plot_data(VSE_table)
    #plt.scatter(VSE_table['Bx'],VSE_table['By'],c=VSE_table['Bz'],cmap='jet')
    #plt.show()
code_test()
