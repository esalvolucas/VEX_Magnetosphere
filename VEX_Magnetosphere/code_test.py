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

def code_test(orbit):
    
#     #years = pd.date_range('2006-04-24 00:00:00','2014-11-25 00:00:00',freq='YS').astype(str).tolist()
#     #years = ['2006-04-24'] + years + ['2014-11-25']
#     years = ['2006-04-24','2014-11-25']
#    
#     print(years)
#     l = len(years)
#         
#     for i,val in enumerate(years):
#         if i != l-1:
#             print(years[i] + ' TO ' + years[i+1])
#             title_yr = str(years[i]) + ' TO ' + str(years[i+1])
#             dimtick = 0
#             for dim in [['YSC','ZSC'],['XSC','ZSC'],['XSC','YSC']]:
#                 x_pkl_name = years[i][0:7]+'_'+years[i+1][0:7]+'_Bx_'+dim[0]+'_'+dim[1]+"_C"
#                 y_pkl_name = years[i][0:7]+'_'+years[i+1][0:7]+'_By_'+dim[0]+'_'+dim[1]+"_C"
#                 z_pkl_name = years[i][0:7]+'_'+years[i+1][0:7]+'_Bz_'+dim[0]+'_'+dim[1]+"_C"
#                 print(x_pkl_name,y_pkl_name,z_pkl_name)
#                 x_pkl_name2D = "./VEX_data_files/VEX_bin_" + x_pkl_name + "_2DNS.pkl"
#                 y_pkl_name2D = "./VEX_data_files/VEX_bin_" + y_pkl_name + "_2DNS.pkl"
#                 z_pkl_name2D = "./VEX_data_files/VEX_bin_" + z_pkl_name + "_2DNS.pkl"
#                     
#                 X = cPickle.load(open(x_pkl_name2D,"rb"))
#                 Y = cPickle.load(open(y_pkl_name2D,"rb"))
#                 Z = cPickle.load(open(z_pkl_name2D,"rb"))
#                     
#                 #plot_dir = r'C:/Users/Elysia/Pictures/VEX Plots/gif/'
#                 plot_dir = r'C:/Users/Elysia/Pictures/VEX Plots/'
#                     
#                 if dimtick == 0:
#                     bin_3d(X,Y,Z,dim='x',v_toggle='off',save=True,name=plot_dir+x_pkl_name,title=title_yr)
#                 elif dimtick == 1:
#                     bin_3d(Y,X,Z,dim='y',v_toggle='off',save=True,name=plot_dir+y_pkl_name,title=title_yr)
#                 elif dimtick == 2:
#                     bin_3d(Z,X,Y,dim='z',v_toggle='off',save=True,name=plot_dir+z_pkl_name,title=title_yr)
#                     
#                 dimtick += 1
#                 print(dimtick)
                
#     Xxy = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bx_XSC_YSC_2D.pkl","rb"))
#     Yxy = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_By_XSC_YSC_2D.pkl","rb"))
#     Zxy = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bz_XSC_YSC_2D.pkl","rb"))
#     #Bxy = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_B_XSC_YSC_2D.pkl","rb"))
#     
#     Xxz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bx_XSC_ZSC_2D.pkl","rb"))
#     Yxz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_By_XSC_ZSC_2D.pkl","rb"))
#     Zxz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bz_XSC_ZSC_2D.pkl","rb"))
#     #Bxz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_B_XSC_ZSC_2D.pkl","rb"))
#     
#     Xyz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bx_YSC_ZSC_2D.pkl","rb"))
#     Yyz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_By_YSC_ZSC_2D.pkl","rb"))
#     Zyz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bz_YSC_ZSC_2D.pkl","rb"))
#     #Byz = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_B_YSC_ZSC_2D.pkl","rb"))
#     
#     
#     ### NIGHTSIDE ###
#     Xxyn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bx_XSC_YSC_2Dns.pkl","rb"))
#     Yxyn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_By_XSC_YSC_2Dns.pkl","rb"))
#     Zxyn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bz_XSC_YSC_2Dns.pkl","rb"))
#     Bxyn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_B_XSC_YSC_2Dns.pkl","rb"))
#     
#     Xxzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bx_XSC_ZSC_2Dns.pkl","rb"))
#     Yxzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_By_XSC_ZSC_2Dns.pkl","rb"))
#     Zxzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bz_XSC_ZSC_2Dns.pkl","rb"))
#     #Bxzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_B_XSC_ZSC_2Dns.pkl","rb"))
#     
#     Xyzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bx_YSC_ZSC_2Dns.pkl","rb"))
#     Yyzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_By_YSC_ZSC_2Dns.pkl","rb"))
#     Zyzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_Bz_YSC_ZSC_2Dns.pkl","rb"))
#     #Byzn = cPickle.load(open("./VEX_data_files/VEX_bin_2006-04_2014-11_B_YSC_ZSC_2Dns.pkl","rb"))
    
    
    
    #bin_3d(Zxy,Xxy,Yxy,dim='z',v_toggle='on')
    #bin_3d(B,X,Y,dim='z',v_toggle='on')
    #print(len(np.arange(-3,3,0.1)))
    #bin_3d(Yxz,Xxz,Zxz,dim='y',v_toggle='on')
    #bin_3d(Xyz,Yyz,Zyz,dim='x',v_toggle='off')
    
    #bin_3d(Zxyn,Xxyn,Yxyn,dim='z',v_toggle='on')
    #bin_3d(Bxyn,Xxyn,Yxyn,dim='z',v_toggle='off')
    #print(len(np.arange(-3,3,0.1)))
    #bin_3d(Yxzn,Xxzn,Zxzn,dim='y',v_toggle='on')
    #bin_3d(Xyzn,Yyzn,Zyzn,dim='x',v_toggle='off')
    
    
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
    #dates_file = mag_concat(start_time,end_time)
    dates_file = './VEX_data_files/' + orbit[0:10] + '_TO_' + orbit[0:10] + '.tab' 
    #LOAD DATA INTO PANDAS DATAFRAME
    table = vex_load_data(dates_file,disp=False)
    table = table.resample('T').mean()
    table = clock_cone_angle(table)
    plt.plot(table['Clock'])
     
     
    table['XSC'] = table['XSC']/6051.8
    table['YSC'] = table['YSC']/6051.8
    table['ZSC'] = table['ZSC']/6051.8
    table['RSC'] = table['RSC']/6051.8
     
     
     
    #table = table.where((table['YSC']<=2)&(table['YSC']>=-2))
    #table = table.where((table['ZSC']<=2)&(table['ZSC']>=-2))
    #print(table)
    #vex_plot_data(table)
     
    #data = read_sw(flag=[0,1])
     
    CA_select_in,CA_select_out = magnetosphere(table)
     
    VSE_table = VSO_to_VSE(table,CA_select_in,CA_select_out)
    #VSE_table = append_sw(VSE_table,data,CA_select_in,CA_select_out)
    #pd.set_option('display.max_rows', 10000)
    print(VSE_table)
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
    #VSO_avg(table)
    #VSO_avg(VSE_table,VSE=True)
    #PLOT 1-MINUTE CADENCE VSO DATA (3D)
    #VSO_3D_avg(table)

    #print(VSE_table['XSC'])
    #vex_plot_data(VSE_table)
    #plt.scatter(VSE_table['Bx'],VSE_table['By'],c=VSE_table['Bz'],cmap='jet')
    #plt.show()
code_test('2014-11-14 00:00:00')
#code_test('2014-10-02 00:00:00','2014-10-02 00:00:00')