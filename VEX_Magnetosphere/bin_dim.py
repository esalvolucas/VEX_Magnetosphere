from VEX_Magnetosphere import *
import matplotlib.pyplot as plt
import numpy as np
from pydivide import bin
import _pickle as cPickle



def bin_dim(start_time,end_time,mag='Bx',dim=['YSC','ZSC'],pkl_name=None):
    if pkl_name == None:
        pkl_name = start_time[0:7]+'_'+end_time[0:7]+'_'+mag+'_'+dim[0]+'_'+dim[1]
        print(pkl_name)
    pkl_name3D = "./VEX_data_files/VEX_bin_" + pkl_name + "_3D.pkl"
    pkl_name2D = "./VEX_data_files/VEX_bin_" + pkl_name + "_2D.pkl"
     
    mag = 'VEX.'+mag
    
    #print(mag,dim)
    
    if 'XSC' not in dim:
        collapse = 0
    elif 'YSC' not in dim:
        collapse = 1
    elif 'ZSC' not in dim:
        collapse = 2
        
    print(collapse)
    
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
            VSE_binavg = bin(insitu,mag,['VEX.XSC','VEX.YSC','VEX.ZSC'],avg=True,
                               binsize=[0.1,0.1,0.1],mins=[-3,-3,-3],maxs=[3,3,3])
            VSE_binavg = VSE_binavg[0]
            np.set_printoptions(threshold=np.nan)
            xy_arr = np.nanmean(VSE_binavg,axis=collapse)
            xy_nan = np.logical_not(np.isnan(xy_arr))*1
            xy_arr[np.isnan(xy_arr)] = 0
            final_stat += xy_arr
            final_nan += xy_nan

        except:
            continue
 
    final_nan[np.where(final_nan==0)] = 1
    final_stat = np.divide(final_stat,final_nan)
    
    final_stat = final_stat.T
    
    cPickle.dump(VSE_binavg, open(pkl_name3D, "wb" ))
    cPickle.dump(final_stat, open(pkl_name2D,"wb"))
    print('Data dumped to:')
    print(pkl_name2D)
    print(pkl_name3D)
    
    return pkl_name2D,pkl_name3D,final_stat

bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='Bx',dim=['YSC','ZSC'])
bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='By',dim=['YSC','ZSC'])
bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='Bz',dim=['YSC','ZSC'])

bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='Bx',dim=['XSC','ZSC'])
bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='By',dim=['XSC','ZSC'])
bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='Bz',dim=['XSC','ZSC'])

# bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='Bx',dim=['XSC','YSC'])
# bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='By',dim=['XSC','YSC'])
# bin_dim('2013-05-07 00:00:00','2014-05-07 00:00:00',mag='Bz',dim=['XSC','YSC'])