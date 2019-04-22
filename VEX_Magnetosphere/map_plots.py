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

def map_plots(start_date,end_date,ns=False,append=None):
    #years = pd.date_range('2006-04-24 00:00:00','2014-11-25 00:00:00',freq='YS').astype(str).tolist()
    #years = ['2006-04-24'] + years + ['2014-11-25']
    #years = ['2006-04-24','2014-11-25']
    years = [start_date,end_date]
    
    l = len(years)
         
    for i,val in enumerate(years):
        if i != l-1:
            print(years[i] + ' TO ' + years[i+1])
            title_yr = str(years[i]) + ' TO ' + str(years[i+1])
            dimtick = 0
            for dim in [['YSC','ZSC'],['XSC','ZSC'],['XSC','YSC']]:
                x_pkl_name = years[i][0:10]+'_'+years[i+1][0:10]+'_Bx_'+dim[0]+'_'+dim[1]+"_"+append
                y_pkl_name = years[i][0:10]+'_'+years[i+1][0:10]+'_By_'+dim[0]+'_'+dim[1]+"_"+append
                z_pkl_name = years[i][0:10]+'_'+years[i+1][0:10]+'_Bz_'+dim[0]+'_'+dim[1]+"_"+append
                b_pkl_name = years[i][0:10]+'_'+years[i+1][0:10]+'_B_'+dim[0]+'_'+dim[1]+"_"+append

                print(x_pkl_name,y_pkl_name,z_pkl_name)       
                if ns==True:
                    x_pkl_name2D = "./VEX_data_files/VSE/VEX_bin_" + x_pkl_name + "_2DNS.pkl"
                    y_pkl_name2D = "./VEX_data_files/VSE/VEX_bin_" + y_pkl_name + "_2DNS.pkl"
                    z_pkl_name2D = "./VEX_data_files/VSE/VEX_bin_" + z_pkl_name + "_2DNS.pkl"
                    b_pkl_name2D = "./VEX_data_files/VSE/VEX_bin_" + b_pkl_name + "_2DNS.pkl"
                else:
                    x_pkl_name2D = "./VEX_data_files/VSE/VEX_bin_" + x_pkl_name + "_2D.pkl"
                    y_pkl_name2D = "./VEX_data_files/VSE/VEX_bin_" + y_pkl_name + "_2D.pkl"
                    z_pkl_name2D = "./VEX_data_files/VSE/VEX_bin_" + z_pkl_name + "_2D.pkl"
                    b_pkl_name2D = "./VEX_data_files/VSE/VEX_bin_" + b_pkl_name + "_2D.pkl"

                
#                 x_pkl_name3D = "./VEX_data_files/VEX_bin_" + x_pkl_name + "_3D.pkl"
#                 y_pkl_name3D = "./VEX_data_files/VEX_bin_" + y_pkl_name + "_3D.pkl"
#                 z_pkl_name3D = "./VEX_data_files/VEX_bin_" + z_pkl_name + "_3D.pkl"
                
                X = cPickle.load(open(x_pkl_name2D,"rb"))
                Y = cPickle.load(open(y_pkl_name2D,"rb"))
                Z = cPickle.load(open(z_pkl_name2D,"rb"))
                B = cPickle.load(open(b_pkl_name2D,"rb"))
                
#                 X = cPickle.load(open(x_pkl_name3D,"rb"))
#                 Y = cPickle.load(open(y_pkl_name3D,"rb"))
#                 Z = cPickle.load(open(z_pkl_name3D,"rb"))
                     
                #plot_dir = r'C:/Users/Elysia/Pictures/VEX Plots/gif/'
                plot_dir = r'/Users/ellu2839/Pictures/VEX_Plots/'
                     
                if dimtick == 0:
                    bin_3d(X,Y,Z,dim='x',v_toggle='off',save=True,name=plot_dir+x_pkl_name,title=title_yr,bs='on')
                elif dimtick == 1:
                    bin_3d(Y,X,Z,dim='y',v_toggle='off',save=True,name=plot_dir+y_pkl_name,title=title_yr,bs='on')
                elif dimtick == 2:
                    bin_3d(Z,X,Y,dim='z',v_toggle='off',save=True,name=plot_dir+z_pkl_name,title=title_yr,bs='on')
                    bin_3d(B,X,Y,dim='z',v_toggle='off',save=True,name=plot_dir+b_pkl_name,title=title_yr,bs='on',magB=True)

                dimtick += 1
                print(dimtick)

#map_plots('2010-12-20','2010-12-21',append="orbit2")
#map_plots(append="_C_avg025z3")
#map_plots(append="_C_avg025y3")
map_plots(append='_C_20140101')
