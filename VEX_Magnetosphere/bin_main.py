from VEX_Magnetosphere import *
import pandas as pd

def bin_main(start_time,end_time,ns=False,append=None,slice=None,pres=None):

    orbit_bin(start_time,end_time,mag='Bx',dim=['YSC','ZSC'],append=append,slice=slice,pres=pres)
    orbit_bin(start_time,end_time,mag='By',dim=['YSC','ZSC'],append=append,slice=slice,pres=pres)
    orbit_bin(start_time,end_time,mag='Bz',dim=['YSC','ZSC'],append=append,slice=slice,pres=pres)
    orbit_bin(start_time,end_time,mag='|B|',dim=['YSC','ZSC'],append=append,slice=slice,pres=pres)
 
    orbit_bin(start_time,end_time,mag='Bx',dim=['XSC','ZSC'],append=append,slice=slice,pres=pres)
    orbit_bin(start_time,end_time,mag='By',dim=['XSC','ZSC'],append=append,slice=slice,pres=pres)
    orbit_bin(start_time,end_time,mag='Bz',dim=['XSC','ZSC'],append=append,slice=slice,pres=pres)
    orbit_bin(start_time,end_time,mag='|B|',dim=['XSC','ZSC'],append=append,slice=slice,pres=pres)
     
    orbit_bin(start_time,end_time,mag='Bx',dim=['XSC','YSC'],append=append,slice=slice,pres=pres)
    orbit_bin(start_time,end_time,mag='By',dim=['XSC','YSC'],append=append,slice=slice,pres=pres)
    orbit_bin(start_time,end_time,mag='Bz',dim=['XSC','YSC'],append=append,slice=slice,pres=pres)
    orbit_bin(start_time,end_time,mag='|B|',dim=['XSC','YSC'],append=append,slice=slice,pres=pres)
    

bin_main('2006-04-25','2014-11-24',slice=['YSC',-0.25,0.25],append='YSClow',pres='low')
map_plots('2006-04-25','2014-11-24',append='YSClow')
bin_main('2006-04-25','2014-11-24',slice=['ZSC',-0.25,0.25],append='ZSClow',pres='low')
map_plots('2006-04-25','2014-11-24',append='ZSClow')
bin_main('2006-04-25','2014-11-24',slice=['XSC',0.75,1.25],append='XSClow',pres='low')
map_plots('2006-04-25','2014-11-24',append='XSClow')
bin_main('2006-04-25','2014-11-24',slice=['XSC',-2.0,-1.0],append='XSCNSlow',pres='low')
map_plots('2006-04-25','2014-11-24',append='XSCNSlow')
bin_main('2006-04-25','2014-11-24',slice=None,append='alllow',pres='low')
map_plots('2006-04-25','2014-11-24',append='alllow')
bin_main('2006-04-25','2014-11-24',slice=None,append='allhigh',pres='high')
map_plots('2006-04-25','2014-11-24',append='allhigh')

# dates = pd.date_range('2014-04-26','2014-11-24',freq='D').astype(str).tolist()
# for date in dates:
#     try:
#         bin_main('2014-04-25',date,slice=['YSC',-0.25,0.25],append='025y3')
#         map_plots('2014-04-25',date,append="025y3")
#     except:
#         continue