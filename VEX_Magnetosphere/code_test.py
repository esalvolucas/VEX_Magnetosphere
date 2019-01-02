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

def code_test(start_time,end_time):
    
    Xxy = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bx_XSC_YSC_2D.pkl","rb"))
    Yxy = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_By_XSC_YSC_2D.pkl","rb"))
    Zxy = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bz_XSC_YSC_2D.pkl","rb"))
    #Bxy = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_B_XSC_YSC_2D.pkl","rb"))
    
    Xxz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bx_XSC_ZSC_2D.pkl","rb"))
    Yxz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_By_XSC_ZSC_2D.pkl","rb"))
    Zxz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bz_XSC_ZSC_2D.pkl","rb"))
    #Bxz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_B_XSC_ZSC_2D.pkl","rb"))
    
    Xyz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bx_YSC_ZSC_2D.pkl","rb"))
    Yyz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_By_YSC_ZSC_2D.pkl","rb"))
    Zyz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bz_YSC_ZSC_2D.pkl","rb"))
    #Byz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_B_YSC_ZSC_2D.pkl","rb"))
    
    
    ### NIGHTSIDE ###
    Xxyn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bx_XSC_YSC_2Dns.pkl","rb"))
    Yxyn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_By_XSC_YSC_2Dns.pkl","rb"))
    Zxyn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bz_XSC_YSC_2Dns.pkl","rb"))
    Bxyn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_B_XSC_YSC_2Dns.pkl","rb"))
    
    Xxzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bx_XSC_ZSC_2Dns.pkl","rb"))
    Yxzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_By_XSC_ZSC_2Dns.pkl","rb"))
    Zxzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bz_XSC_ZSC_2Dns.pkl","rb"))
    #Bxzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_B_XSC_ZSC_2Dns.pkl","rb"))
    
    Xyzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bx_YSC_ZSC_2Dns.pkl","rb"))
    Yyzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_By_YSC_ZSC_2Dns.pkl","rb"))
    Zyzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bz_YSC_ZSC_2Dns.pkl","rb"))
    #Byzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_B_YSC_ZSC_2Dns.pkl","rb"))
    
    
    
    #bin_3d(Zxy,Xxy,Yxy,dim='z',v_toggle='on')
    #bin_3d(B,X,Y,dim='z',v_toggle='on')
    #print(len(np.arange(-3,3,0.1)))
    #bin_3d(Yxz,Xxz,Zxz,dim='y',v_toggle='on')
    bin_3d(Xyz,Yyz,Zyz,dim='x',v_toggle='off')
    
    #bin_3d(Zxyn,Xxyn,Yxyn,dim='z',v_toggle='on')
    #bin_3d(Bxyn,Xxyn,Yxyn,dim='z',v_toggle='off')
    #print(len(np.arange(-3,3,0.1)))
    #bin_3d(Yxzn,Xxzn,Zxzn,dim='y',v_toggle='on')
    bin_3d(Xyzn,Yyzn,Zyzn,dim='x',v_toggle='off')
    
    
    # = cPickle.load(open("VEX_binx_3D.pkl","rb"))
    #X = cPickle.load(open("./VEX_data_files/VEX_bin_2013-05_2014-05_Bx_XSC_YSC_2D.pkl","rb"))
    #Y = cPickle.load(open("./VEX_data_files/VEX_bin_2013-05_2014-05_By_XSC_YSC_2D.pkl","rb"))
    #VEXbin3d = cPickle.load(open("VEX_biny_nightside3D.pkl","rb"))
    #VEXbin2d = cPickle.load(open("VEX_biny_nightside2D.pkl","rb"))
    #Z = cPickle.load(open("./VEX_data_files/VEX_bin_2013-05_2014-05_Bz_XSC_YSC_2D.pkl","rb"))
    
    #X = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bx_XSC_YSC_2Dns.pkl","rb"))
    #Y = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_By_XSC_YSC_2Dns.pkl","rb"))
    #VEXbin3d = cPickle.load(open("VEX_biny_nightside3D.pkl","rb"))
    #VEXbin2d = cPickle.load(open("VEX_biny_nightside2D.pkl","rb"))
    #Z = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bz_XSC_YSC_2Dns.pkl","rb"))
    #B = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_B_XSC_YSC_2Dns.pkl","rb"))
#     print(VEXbin3d)
#     print(np.shape(VEXbin3d))                             
#     
#     print(VEXbin2d)
#     print(np.shape(VEXbin2d))
    
    #bin_3d(VEXbin2d,dim='y',v_toggle='on')
    #bin_3d(Z,X,Y,dim='z',v_toggle='on')
    #bin_3d(B,X,Y,dim='z',v_toggle='on')
    #print(len(np.arange(-3,3,0.1)))
    #bin_3d(Y,X,Z,dim='y',v_toggle='on')
    #bin_3d(X,Y,Z,dim='x',v_toggle='on')
    #GRAB RELEVANT FILES IN DATE RANGE
#     dates_file = mag_concat(start_time,end_time)
#     
#     #LOAD DATA INTO PANDAS DATAFRAME
#     table = vex_load_data(dates_file,disp=False)
#     table = table.resample('T').mean()
#     table = clock_cone_angle(table)
#     table['XSC'] = table['XSC']/6051.8
#     table['YSC'] = table['YSC']/6051.8
#     table['ZSC'] = table['ZSC']/6051.8
#     table['RSC'] = table['RSC']/6051.8
    
    
    
    #table = table.where((table['YSC']<=2)&(table['YSC']>=-2))
    #table = table.where((table['ZSC']<=2)&(table['ZSC']>=-2))
    #print(table)
    #vex_plot_data(table)
    
    
    #CA_select_in,CA_select_out = magnetosphere(table)
    
    #VSE_table = VSO_to_VSE(table,CA_select_in,CA_select_out)
    #VSE_table = VSE_table.where((VSE_table['XSC']<-1)&(VSE_table['XSC']>-2))
    #print(VSE_table)
    #print(len(VSE_table.index))
    #pytplot.store_data('vexmag',data={'x':list(str(VSE_table.index)),'y':[VSE_table['XSC'].values,VSE_table['YSC'].values,
    #                                                                   VSE_table['ZSC'].values,VSE_table['RSC'].values,
    #                                                                   VSE_table['Bx'].values,VSE_table['By'].values,
    #                                                                   VSE_table['Bz'].values,VSE_table['|B|'].values,
    #                                                                   VSE_table['Clock'].values,VSE_table['Cone'].values]})
    #print(pytplot.data_quants['vexmag'].data)
    
    #insitu = {}
    #insitu['VEX'] = VSE_table
#     insitu['VEX']['Bx'] = VSE_table['Bx'].values
#     insitu['VEX']['By'] = VSE_table['By'].values
#     insitu['VEX']['Bz'] = VSE_table['Bz'].values
#     insitu['VEX']['|B|'] = VSE_table['|B|'].values
#     insitu['VEX']['XSC'] = VSE_table['XSC'].values
#     insitu['VEX']['YSC'] = VSE_table['YSC'].values
#     insitu['VEX']['ZSC'] = VSE_table['ZSC'].values
#     insitu['VEX']['RSC'] = VSE_table['RSC'].values
    #print(insitu['VEX']['Bx'])
    #print('_______________')
    #make list of each 3D array per day
    #average at end
    #numpy.nansum?
    #VSE_binavg_x = bin(insitu,'VEX.Bx',['VEX.XSC','VEX.YSC','VEX.ZSC'],avg=True,binsize=[0.1,0.1,0.1],
                       #mins=[-2,-2,-2],maxs=[2,2,2])
    #print(VSE_binavg_x)
    #print(np.size(VSE_binavg_x))
    #print(np.all(np.isnan(VSE_binavg_x)))
    
    
    #VSE_binavg_x = VSE_binavg_x[0]
    #np.set_printoptions(threshold=np.nan)

    #for i in len(VSE_binavg_x[0]):
    #    print(VSE_binavg_x[1][?][?]
    #print(VSE_binavg_x[0])
    #print(np.array(VSE_binavg_x[0]).shape)
    #print(np.nanmean(VSE_binavg_x[0],axis=0).shape)
    #yz_arr = np.nanmean(VSE_binavg_x,axis=0)
    #print(yz_arr)
    #yedges = np.arange(-2,2,0.1)
    #zedges = np.arange(-2,2,0.1)
    #ymesh,zmesh = np.meshgrid(yedges,zedges)

    
#     fmean = lambda x: np.nanmean(x)
#     print(VSE_binavg_x[:][20][20])
#     print(VSE_binavg_x[20][:][20])
#     print(VSE_binavg_x[20][20][:])
# 
#     print(VSE_binavg_x[~np.isnan(VSE_binavg_x)])
#     xmean,xxe,xye,xbinn = stats.binned_statistic_2d(VSE_binavg_x[0][:][0],VSE_binavg_x[0][0][:],
#                                                     VSE_binavg_x[:][0][0],fmean,40,[[-2,2],[-2,2]])
    #print(xmean)
    #print(xxe)
    #print(np.all(np.isnan(xmean)))
    #print(yz_arr[0],yz_arr[1])
    #H, xedges, yedges = np.histogram2d(yz_arr[0], yz_arr[1], bins=(xedges, yedges))
    #H = H.T  # Let each row list bins with common y range.

#     fig,ax = plt.subplots(nrows=1, ncols=1)
#     plt.gca().set_aspect('equal', adjustable='box')
# 
#     plt.pcolormesh(ymesh,zmesh,yz_arr,cmap='seismic')
#     venus1=plt.Circle((0,0),1,color='k',fill=False)
#     ax.add_artist(venus1)
#     plt.show()
    #plt.imshow(xstats)
    #plt.imshow(H)#, interpolation='nearest', origin='low',
        #extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
    #bin_3d(VSE_table)
    
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
    #VSO_avg(table)
    #VSO_avg(VSE_table,VSE=True)
    #PLOT 1-MINUTE CADENC VSO DATA (3D)
    #VSO_3D_avg(table)

    #print(VSE_table['XSC'])
    #vex_plot_data(VSE_table)
    #plt.scatter(VSE_table['Bx'],VSE_table['By'],c=VSE_table['Bz'],cmap='jet')
    #plt.show()
code_test('2013-05-21 00:00:00','2013-06-21 00:00:00')
#code_test('2014-10-02 00:00:00','2014-10-02 00:00:00')