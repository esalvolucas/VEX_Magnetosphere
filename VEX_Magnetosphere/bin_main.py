from VEX_Magnetosphere import *
import pandas as pd
from VEX_Magnetosphere.map_plots import *

def bin_main(start_time,
             end_time,
             ns=False,
             append=None,
             slice=None):
    

#     bin_dim(start_time,end_time,mag='Bx',dim=['YSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='By',dim=['YSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='Bz',dim=['YSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='|B|',dim=['YSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
# 
#     bin_dim(start_time,end_time,mag='Bx',dim=['XSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='By',dim=['XSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='Bz',dim=['XSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='|B|',dim=['XSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
#     
#     bin_dim(start_time,end_time,mag='Bx',dim=['XSC','YSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='By',dim=['XSC','YSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='Bz',dim=['XSC','YSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
#     bin_dim(start_time,end_time,mag='|B|',dim=['XSC','YSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)

    orbit_bin(start_time,end_time,mag='Bx',dim=['YSC','ZSC'],ns=ns,append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='By',dim=['YSC','ZSC'],ns=ns,append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='Bz',dim=['YSC','ZSC'],ns=ns,append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='|B|',dim=['YSC','ZSC'],ns=ns,append=append,slice=slice)
 
    orbit_bin(start_time,end_time,mag='Bx',dim=['XSC','ZSC'],ns=ns,append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='By',dim=['XSC','ZSC'],ns=ns,append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='Bz',dim=['XSC','ZSC'],ns=ns,append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='|B|',dim=['XSC','ZSC'],ns=ns,append=append,slice=slice)
     
    orbit_bin(start_time,end_time,mag='Bx',dim=['XSC','YSC'],ns=ns,append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='By',dim=['XSC','YSC'],ns=ns,append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='Bz',dim=['XSC','YSC'],ns=ns,append=append,slice=slice)
    orbit_bin(start_time,end_time,mag='|B|',dim=['XSC','YSC'],ns=ns,append=append,slice=slice)
    
#bin_main('2014-04-25','2014-11-24',slice=['YSC',-0.25,0.25],append='sumYSC')
#map_plots('2014-04-25','2014-11-24',append='sumYSC')

bin_main('2006-04-25','2014-11-24',slice=['YSC',-0.25,0.25],append='sumYSC')
map_plots('2006-04-25','2014-11-24',append='sumYSC')
bin_main('2006-04-25','2014-11-24',slice=['ZSC',-0.25,0.25],append='sumZSC')
map_plots('2006-04-25','2014-11-24',append='sumZSC')
bin_main('2006-04-25','2014-11-24',slice=['XSC',0.75,1.25],append='sumXSC')
map_plots('2006-04-25','2014-11-24',append='sumXSC')
bin_main('2006-04-25','2014-11-24',slice=None,append='sumall')
map_plots('2006-04-25','2014-11-24',append='sumall')

#bin_main('2006-04-25','2014-11-24',append='all_full')
#map_plots('2006-04-25','2014-11-24',append='all_full')
#bin_main('2006-04-25','2014-11-24',ns=True,append='full_nn3')
#bin_main('2010-12-20','2010-12-21',slice2=True,append='orbit2')
#bin_main('2014-04-25','2014-11-24',ns=True,append='sumns')
#map_plots('2014-04-25','2014-11-24',ns=True,append='sumns')
#bin_main('2014-09-14','2014-12-14',slice2=True,append='avg025y3')
# dates = pd.date_range('2014-03-27','2014-04-04',freq='D').astype(str).tolist()
# for date in dates:
#     bin_main('2014-01-04',date,slice2=True,append='025y3')
#     map_plots('2014-01-04',date,append="025y3")