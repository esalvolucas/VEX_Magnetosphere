from VEX_Magnetosphere import *
import pandas as pd
from time import sleep
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
    

# bin_main('2006-04-25','2014-11-24',slice=['YSC',-0.25,0.25],append='YSClow1',pres='low')
# map_plots('2006-04-25','2014-11-24',append='YSClow1',slicedir='YSC')
# sleep(7)
# bin_main('2006-04-25','2014-11-24',slice=['ZSC',-0.25,0.25],append='ZSClow1',pres='low')
# map_plots('2006-04-25','2014-11-24',append='ZSClow1',slicedir='ZSC')
# sleep(7)
# bin_main('2006-04-25','2014-11-24',slice=['XSC',0.75,1.25],append='XSClow1',pres='low')
# map_plots('2006-04-25','2014-11-24',append='XSClow',slicedir='XSC')
# sleep(7)
# bin_main('2006-04-25','2014-11-24',slice=['XSC',-2.0,-1.0],append='XSCNSlow1',pres='low')
# map_plots('2006-04-25','2014-11-24',append='XSCNSlow1',slicedir='XSC')
# sleep(7)
# bin_main('2006-04-25','2014-11-24',slice=None,append='alllow1',pres='low')
# map_plots('2006-04-25','2014-11-24',append='alllow1')
# sleep(7)
# bin_main('2006-04-25','2014-11-24',slice=['YSC',-0.25,0.25],append='YSCmed1',pres='med')
# map_plots('2006-04-25','2014-11-24',append='YSCmed1',slicedir='YSC')
# sleep(7)
# bin_main('2006-04-25','2014-11-24',slice=['ZSC',-0.25,0.25],append='ZSCmed1',pres='med')
# map_plots('2006-04-25','2014-11-24',append='ZSCmed1',slicedir='ZSC')
# sleep(7)
bin_main('2006-04-25','2014-11-24',slice=['XSC',0.75,1.25],append='XSCmed1',pres='med')
map_plots('2006-04-25','2014-11-24',append='XSCmed1',slicedir='XSC')
sleep(7)
bin_main('2006-04-25','2014-11-24',slice=['XSC',-2.0,-1.0],append='XSCNSmed1',pres='med')
map_plots('2006-04-25','2014-11-24',append='XSCNSmed1',slicedir='XSC')
sleep(7)
bin_main('2006-04-25','2014-11-24',slice=None,append='allmed1',pres='med')
map_plots('2006-04-25','2014-11-24',append='allmed1')
sleep(7)
bin_main('2006-04-25','2014-11-24',slice=['YSC',-0.25,0.25],append='YSChigh1',pres='high')
map_plots('2006-04-25','2014-11-24',append='YSChigh1',slicedir='YSC')
sleep(7)
bin_main('2006-04-25','2014-11-24',slice=['ZSC',-0.25,0.25],append='ZSChigh1',pres='high')
map_plots('2006-04-25','2014-11-24',append='ZSChigh1',slicedir='ZSC')
sleep(7)
bin_main('2006-04-25','2014-11-24',slice=['XSC',0.75,1.25],append='XSChigh1',pres='high')
map_plots('2006-04-25','2014-11-24',append='XSChigh1',slicedir='XSC')
sleep(7)
bin_main('2006-04-25','2014-11-24',slice=['XSC',-2.0,-1.0],append='XSCNShigh1',pres='high')
map_plots('2006-04-25','2014-11-24',append='XSCNShigh1',slicedir='XSC')
sleep(7)
bin_main('2006-04-25','2014-11-24',slice=None,append='allhigh1',pres='high')
map_plots('2006-04-25','2014-11-24',append='allhigh1')

bin_main('2006-04-25','2014-11-24',slice=['XSC',0.5,1.0],append='XSC0510low1',pres='low')
map_plots('2006-04-25','2014-11-24',append='XSC0510low1',slicedir='XSC')
bin_main('2006-04-25','2014-11-24',slice=['XSC',0.5,1.0],append='XSC0510med1',pres='med')
map_plots('2006-04-25','2014-11-24',append='XSC0510med1',slicedir='XSC')
bin_main('2006-04-25','2014-11-24',slice=['XSC',0.5,1.0],append='XSC0510high1',pres='high')
map_plots('2006-04-25','2014-11-24',append='XSC0510high1',slicedir='XSC')


bin_main('2006-04-25','2014-11-24',slice=['XSC',0.0,0.5],append='XSC0005low1',pres='low')
map_plots('2006-04-25','2014-11-24',append='XSC0005low1',slicedir='XSC')
bin_main('2006-04-25','2014-11-24',slice=['XSC',0.0,0.5],append='XSC0005med1',pres='med')
map_plots('2006-04-25','2014-11-24',append='XSC0005med1',slicedir='XSC')
bin_main('2006-04-25','2014-11-24',slice=['XSC',0.0,0.5],append='XSC0005high1',pres='high')
map_plots('2006-04-25','2014-11-24',append='XSC0005high1',slicedir='XSC')




# dates = pd.date_range('2014-04-26','2014-11-24',freq='D').astype(str).tolist()
# for date in dates:
#     try:
#         bin_main('2014-04-25',date,slice=['YSC',-0.25,0.25],append='025y3')
#         map_plots('2014-04-25',date,append="025y3")
#     except:
#         continue