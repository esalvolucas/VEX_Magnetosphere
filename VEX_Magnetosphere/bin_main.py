from VEX_Magnetosphere import *
import pandas as pd
#from VEX_Magnetosphere.map_plots import *
#from VEX_Magnetosphere.orbit_concat import *
def bin_main(start_time,
             end_time,
             ns=False,
             append=None,
             slice=None):
    

#     bin_dim(start_time,end_time,mag='Bx',dim=['YSC','ZSC'],counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='By',dim=['YSC','ZSC'],counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='Bz',dim=['YSC','ZSC'],counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='|B|',dim=['YSC','ZSC'],counts=counts,append=append,slice=slice,slice2=slice2)
# 
#     bin_dim(start_time,end_time,mag='Bx',dim=['XSC','ZSC'],counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='By',dim=['XSC','ZSC'],counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='Bz',dim=['XSC','ZSC'],counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='|B|',dim=['XSC','ZSC'],counts=counts,append=append,slice=slice,slice2=slice2)
#     
#     bin_dim(start_time,end_time,mag='Bx',dim=['XSC','YSC'],counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='By',dim=['XSC','YSC'],counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='Bz',dim=['XSC','YSC'],counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='|B|',dim=['XSC','YSC'],counts=counts,append=append,slice=slice,slice2=slice2)

    orbit_bin(start_time,end_time,mag='Bx',dim=['YSC','ZSC'],append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='By',dim=['YSC','ZSC'],append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='Bz',dim=['YSC','ZSC'],append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='|B|',dim=['YSC','ZSC'],append=append,slice=slice)
 
    orbit_bin(start_time,end_time,mag='Bx',dim=['XSC','ZSC'],append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='By',dim=['XSC','ZSC'],append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='Bz',dim=['XSC','ZSC'],append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='|B|',dim=['XSC','ZSC'],append=append,slice=slice)
     
    orbit_bin(start_time,end_time,mag='Bx',dim=['XSC','YSC'],append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='By',dim=['XSC','YSC'],append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='Bz',dim=['XSC','YSC'],append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='|B|',dim=['XSC','YSC'],append=append,slice=slice)
    
# bin_main('2014-04-25','2014-05-04',slice=['XSC',-2.0,-1.0],append='NStest')
# map_plots('2014-04-25','2014-05-04',append='NStest')
#orbit_concat()

#bin_main('2006-04-25','2014-11-24',slice=['YSC',-0.25,0.25],append='YSC')
map_plots('2006-04-25','2014-11-24',append='YSC')
bin_main('2006-04-25','2014-11-24',slice=['ZSC',-0.25,0.25],append='ZSC')
map_plots('2006-04-25','2014-11-24',append='ZSC')
bin_main('2006-04-25','2014-11-24',slice=['XSC',0.75,1.25],append='XSC')
map_plots('2006-04-25','2014-11-24',append='XSC')
bin_main('2006-04-25','2014-11-24',slice=['XSC',-2.0,-1.0],append='XSCNS')
map_plots('2006-04-25','2014-11-24',append='XSCNS')
bin_main('2006-04-25','2014-11-24',slice=None,append='all')
map_plots('2006-04-25','2014-11-24',append='all')

#bin_main('2006-04-25','2014-11-24',append='all_full')
#map_plots('2006-04-25','2014-11-24',append='all_full')
#bin_main('2006-04-25','2014-11-24',ns=True,append='full_nn3')
#bin_main('2010-12-20','2010-12-21',slice2=True,append='orbit2')
#bin_main('2014-04-25','2014-11-24',ns=True,append='sumns')
#map_plots('2014-04-25','2014-11-24',ns=True,append='sumns')
#bin_main('2014-09-14','2014-12-14',slice2=True,append='avg025y3')
# dates = pd.date_range('2014-04-26','2014-11-24',freq='D').astype(str).tolist()
# for date in dates:
#     try:
#         bin_main('2014-04-25',date,slice=['YSC',-0.25,0.25],append='025y3')
#         map_plots('2014-04-25',date,append="025y3")
#     except:
#         continue