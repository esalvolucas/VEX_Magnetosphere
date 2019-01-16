from VEX_Magnetosphere import *
import matplotlib.pyplot as plt
import numpy as np
from pydivide import bin
import _pickle as cPickle
import pandas as pd


def bin_dim(start_time,end_time,mag='Bx',dim=['YSC','ZSC'],ns=False,counts=True,pkl_name=None):
    #if custom file name not given, create one
    if pkl_name == None:
        pkl_name = start_time[0:7]+'_'+end_time[0:7]+'_'+mag+'_'+dim[0]+'_'+dim[1]
        if mag == '|B|':
            pkl_name = start_time[0:7]+'_'+end_time[0:7]+'_B_'+dim[0]+'_'+dim[1]
    #indicate binning scheme
    if counts == True:
        pkl_name = pkl_name + "_C"
    print(pkl_name)
    #changes filename based on if binning nightside data only or not
    if ns == False:
        pkl_name3D = "./VEX_data_files/VEX_bin_" + pkl_name + "_3D.pkl"
        pkl_name2D = "./VEX_data_files/VEX_bin_" + pkl_name + "_2D.pkl"
    if ns == True:
        pkl_name3D = "./VEX_data_files/VEX_bin_" + pkl_name + "_3DNS.pkl"
        pkl_name2D = "./VEX_data_files/VEX_bin_" + pkl_name + "_2DNS.pkl"
    mag = 'VEX.'+mag
        
    #based on provided dimensions, set collapse axis to 3rd dimension
    if 'XSC' not in dim:
        collapse = 0
    elif 'YSC' not in dim:
        collapse = 1
    elif 'ZSC' not in dim:
        collapse = 2
 
    #get list of orbits between start and end time
    orbits = orbit_delta_list(start_time, end_time)
    #initialize 60x60 binning matrix
    final_stat = np.zeros((60,60))
    final_nan = np.zeros((60,60))
    #for each orbit
    for orbit in orbits:
        print(orbit)
        try:
            #get data file produced by prior run of mag_concat
            dates_file = './VEX_data_files/' + orbit[0:10] + '_TO_' + orbit[0:10] + '.tab'
            #load data into dataframe
            table = vex_load_data(dates_file,disp=False)
            #resample from 1s to 1min cadence, take mean of data in between
            table = table.resample('T').mean()
            #find clock and cone angles, append to table
            table = clock_cone_angle(table)
            #rescale spatial data from km to Rv
            table['XSC'] = table['XSC']/6051.8
            table['YSC'] = table['YSC']/6051.8
            table['ZSC'] = table['ZSC']/6051.8
            table['RSC'] = table['RSC']/6051.8
        except:
            print('table fail')
            pass
         
        try:
            #get CA selections based on BS entry/exit
            CA_select_in,CA_select_out = magnetosphere_mmo(table)
        except:
            print('CA fail')
            continue
 
        try:
            #perform coordinate rotation
            VSE_table = VSO_to_VSE(table,CA_select_in,CA_select_out)
            #choose just nightside data if keyword implemented
            if ns == True:
                VSE_table = VSE_table.where((VSE_table['XSC']<-1)&(VSE_table['XSC']>-2))
            #initialize insitu structre for pydivide.bin
            insitu = {}
            insitu['VEX'] = VSE_table
            #use pydivide.bin to bin data in 3D, bins of 0.1, between -3 and 3 Rv
            VSE_binavg,VSE_counts = bin(insitu,mag,['VEX.XSC','VEX.YSC','VEX.ZSC'],avg=True,
                                        density=True,binsize=[0.1,0.1,0.1],mins=[-3,-3,-3],
                                        maxs=[3,3,3])
            np.set_printoptions(threshold=np.nan)
            #take mean of binned data on axis to collapse
            xy_arr = np.nanmean(VSE_binavg,axis=collapse)
            
            #counts bases binning off of data points/bin/orbit, instead of logical 1 or 0 for (data or no data)/orbit
            if counts == False:
                xy_nan = np.logical_not(np.isnan(xy_arr))*1
                xy_arr[np.isnan(xy_arr)] = 0
            if counts == True:
                xy_nan = np.nanmean(VSE_counts,axis=collapse)
                xy_nan[np.isnan(xy_nan)] = 0
            #add data to final arrays
            final_stat += xy_arr
            final_nan += xy_nan
        except:
            print('bin fail')
            continue
    #replace any instances of 0 with 1 to not break np.divide
    final_nan[np.where(final_nan==0)] = 1
    #divide final data by final number of points per bin
    final_stat = np.divide(final_stat,final_nan)
    #transpose 2D data matrix
    final_stat = final_stat.T
    
    #open pkl files, dump final data
    output3D = open(pkl_name3D, "wb" )
    output2D = open(pkl_name2D,"wb")
    cPickle.dump(VSE_binavg, output3D)
    cPickle.dump(final_stat, output2D)
    print('Data dumped to:')
    print(pkl_name2D)
    print(pkl_name3D)
    #close files
    output3D.close()
    output2D.close()
    
    return pkl_name2D,pkl_name3D,final_stat

#bin_dim('2013-05-07 00:00:00','2013-05-07 00:00:00',mag='Bx',dim=['YSC','ZSC'],ns=True)
# bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='By',dim=['YSC','ZSC'])
# bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='Bz',dim=['YSC','ZSC'])
# 
# bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='Bx',dim=['XSC','ZSC'])
# bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='By',dim=['XSC','ZSC'])
# bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='Bz',dim=['XSC','ZSC'])

# bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='Bx',dim=['XSC','YSC'])
# bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='By',dim=['XSC','YSC'])
# bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='Bz',dim=['XSC','YSC'])


bin_dim('2006-04-24 00:00:00','2014-11-25 00:00:00',mag='Bx',dim=['YSC','ZSC'],counts=True)
bin_dim('2006-04-24 00:00:00','2014-11-25 00:00:00',mag='By',dim=['YSC','ZSC'],counts=True)
bin_dim('2006-04-24 00:00:00','2014-11-25 00:00:00',mag='Bz',dim=['YSC','ZSC'],counts=True)
#bin_dim('2006-04-24','2014-11-25',mag='|B|',dim=['YSC','ZSC'])

  
bin_dim('2006-04-24 00:00:00','2014-11-25 00:00:00',mag='Bx',dim=['XSC','ZSC'],counts=True)
bin_dim('2006-04-24 00:00:00','2014-11-25 00:00:00',mag='By',dim=['XSC','ZSC'],counts=True)
bin_dim('2006-04-24 00:00:00','2014-11-25 00:00:00',mag='Bz',dim=['XSC','ZSC'],counts=True)
#bin_dim('2006-04-24 00:00:00','2014-11-25 00:00:00',mag='|B|',dim=['XSC','ZSC'])

bin_dim('2006-04-24 00:00:00','2014-11-25 00:00:00',mag='Bx',dim=['XSC','YSC'],counts=True)
bin_dim('2006-04-24 00:00:00','2014-11-25 00:00:00',mag='By',dim=['XSC','YSC'],counts=True)
bin_dim('2006-04-24 00:00:00','2014-11-25 00:00:00',mag='Bz',dim=['XSC','YSC'],counts=True)
#bin_dim('2006-04-24 00:00:00','2014-11-25 00:00:00',mag='|B|',dim=['XSC','YSC'])
# bin_dim('2006-11-24','2007-01-01',mag='Bx',dim=['YSC','ZSC'])


#years = pd.date_range('2006-04-24 00:00:00','2014-11-25 00:00:00',freq='YS').astype(str).tolist()
#years = ['2006-04-24'] + years + ['2014-11-25']
# years = pd.date_range('2010-01-01 00:00:00','2014-11-25 00:00:00',freq='YS').astype(str).tolist()
# years = years + ['2014-11-25']
# print(years)
# l = len(years)
# for i,val in enumerate(years):
#     if i != l-1:
#         print(years[i] + '   TO   ' + years[i+1])
#         bin_dim(years[i],years[i+1],mag='Bx',dim=['YSC','ZSC'],ns=True)
#         bin_dim(years[i],years[i+1],mag='By',dim=['YSC','ZSC'],ns=True)
#         bin_dim(years[i],years[i+1],mag='Bz',dim=['YSC','ZSC'],ns=True)
# 
#         bin_dim(years[i],years[i+1],mag='Bx',dim=['XSC','ZSC'],ns=True)
#         bin_dim(years[i],years[i+1],mag='By',dim=['XSC','ZSC'],ns=True)
#         bin_dim(years[i],years[i+1],mag='Bz',dim=['XSC','ZSC'],ns=True)
#         
#         bin_dim(years[i],years[i+1],mag='Bx',dim=['XSC','YSC'],ns=True)
#         bin_dim(years[i],years[i+1],mag='By',dim=['XSC','YSC'],ns=True)
#         bin_dim(years[i],years[i+1],mag='Bz',dim=['XSC','YSC'],ns=True)