from VEX_Magnetosphere import *
import numpy as np
from pydivide import bin
import _pickle as cPickle
from VEX_Magnetosphere.date_to_orbit import *
from VEX_Magnetosphere.rotate_to_VSE import *

def orbit_bin(start_time,end_time,mag='Bx',dim=['YSC','ZSC'],ns=False,append=None,slice=None):
    table_fail = 0
    rotation_fail = 0
    bin_fail = 0
    
    pkl_name = start_time[0:10]+'_'+end_time[0:10]+'_'+mag+'_'+dim[0]+'_'+dim[1]
    if mag == '|B|':
        pkl_name = start_time[0:10]+'_'+end_time[0:10]+'_B_'+dim[0]+'_'+dim[1]

    #add suffix if needed
    if append is not None:
        pkl_name = pkl_name + "_" + append
        
    print(pkl_name)
    #changes filename based on if binning nightside data only or not
    if ns == False:
        pkl_name3D = "./VEX_data_files/VSE/VEX_bin_" + pkl_name + "_3D.pkl"
        pkl_name2D = "./VEX_data_files/VSE/VEX_bin_" + pkl_name + "_2D.pkl"
    if ns == True:
        pkl_name3D = "./VEX_data_files/VSE/VEX_bin_" + pkl_name + "_3DNS.pkl"
        pkl_name2D = "./VEX_data_files/VSE/VEX_bin_" + pkl_name + "_2DNS.pkl"
    mag = 'VEX.'+mag
        
    #based on provided dimensions, set collapse axis to 3rd dimension
    if 'XSC' not in dim:
        collapse = 0
    elif 'YSC' not in dim:
        collapse = 1
    elif 'ZSC' not in dim:
        collapse = 2
 
    #get list of orbits between start and end time
    start_o = date_to_orbit(start_time)
    end_o = date_to_orbit(end_time)
    orbits = np.arange(start_o,end_o,1)
    #initialize 60x60 binning matrix
    #final_stat = np.zeros((60,60))
    #final_nan = np.zeros((60,60))
    final_stat = np.zeros((31,31))
    final_nan = np.zeros((31,31))
    #for each orbit
    for orbit in orbits:
        print(orbit)
        try:
            #load data into dataframe
            VSE_table = orbit_load(orbit)
            #select hour of data outside BS crossings
            #CA_select_in = table.iloc[BS_in-60:BS_in]
            #CA_select_out = table.iloc[BS_out:BS_out+60]
        except:
            print('table load fail')
            table_fail += 1
            pass
 
#         try:
#             #perform coordinate rotation
#             #ab_table = aberration(table)
#             VSE_table = rotate_to_VSE(table,BS_in,BS_out,CA_select_in,CA_select_out)
#             #print(VSE_table)
#         except:
#             print('rotation fail')
#             rotation_fail += 1
#             pass
        
        #try:
            #choose just nightside data if keyword implemented
        if ns == True:
            VSE_table = VSE_table.where((VSE_table['XSC']<-1)&(VSE_table['XSC']>-2))
        if slice is not None:
            plane = slice[0]
            minus_delta = slice[1]
            plus_delta = slice[2]
            VSE_table = VSE_table.where((VSE_table[plane]<plus_delta)&(VSE_table[plane]>minus_delta))
        
        #initialize insitu structre for pydivide.bin
        insitu = {}
        insitu['VEX'] = VSE_table
        #use pydivide.bin to bin data in 3D, bins of 0.1, between -3 and 3 Rv
    #             VSE_binavg,VSE_counts = bin(insitu,mag,['VEX.XSC','VEX.YSC','VEX.ZSC'],avg=True,
    #                                         density=True,binsize=[0.1,0.1,0.1],mins=[-3,-3,-3],
    #                                         maxs=[3,3,3])
        VSE_binavg,VSE_counts = bin(insitu,mag,['VEX.XSC','VEX.YSC','VEX.ZSC'],avg=True,
                                    density=True,binsize=[0.2,0.2,0.2],mins=[-3,-3,-3],
                                    maxs=[3.2,3.2,3.2])
        VSE_binavg = VSE_binavg*VSE_counts
        #print((np.isnan(VSE_binavg)).all())

        #print(VSE_binavg)
        #np.set_printoptions(threshold=np.nan)
        #take mean of binned data on axis to collapse
        xy_arr = np.nansum(VSE_binavg,axis=collapse)
        #print(xy_arr)
        #print(xy_arr[np.where(xy_arr<0)])
        #print(xy_arr)
        #counts bases binning off of data points/bin/orbit, instead of logical 1 or 0 for (data or no data)/orbit

        xy_nan = np.nansum(VSE_counts,axis=collapse)
        xy_nan[np.isnan(xy_nan)] = 0
        #add data to final arrays
        final_stat = np.nansum(np.dstack((final_stat,xy_arr)),2)
        #print(final_stat)
        #final_nan = 
        #final_stat += xy_arr
        #print(final_stat)
        final_nan += xy_nan
        
        #except:
        #    print('bin fail')  
        #    bin_fail += 1
        #    continue
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
    
    print('******* ORBIT BIN STATISTICS *******')
    print('Table Failures:',100*table_fail/len(orbits),'%')
    print('Rotation Failures:',100*rotation_fail/len(orbits),'%')
    print('Bin Failures:',100*bin_fail/len(orbits),'%')
    
    return pkl_name2D,pkl_name3D,final_stat