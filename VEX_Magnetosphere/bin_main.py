from VEX_Magnetosphere import *
import pandas as pd

def bin_main(start_time,end_time,ns=False,append=None,slice=None,v=None,E=None,pres=None):

    orbit_bin(start_time,end_time,mag='Bx',dim=['YSC','ZSC'],append=append,slice=slice,v=v,E=E,pres=pres)
    orbit_bin(start_time,end_time,mag='By',dim=['YSC','ZSC'],append=append,slice=slice,v=v,E=E,pres=pres)
    orbit_bin(start_time,end_time,mag='Bz',dim=['YSC','ZSC'],append=append,slice=slice,v=v,E=E,pres=pres)
    orbit_bin(start_time,end_time,mag='|B|',dim=['YSC','ZSC'],append=append,slice=slice,v=v,E=E,pres=pres)
 
    orbit_bin(start_time,end_time,mag='Bx',dim=['XSC','ZSC'],append=append,slice=slice,v=v,E=E,pres=pres)
    orbit_bin(start_time,end_time,mag='By',dim=['XSC','ZSC'],append=append,slice=slice,v=v,E=E,pres=pres)
    orbit_bin(start_time,end_time,mag='Bz',dim=['XSC','ZSC'],append=append,slice=slice,v=v,E=E,pres=pres)
    orbit_bin(start_time,end_time,mag='|B|',dim=['XSC','ZSC'],append=append,slice=slice,v=v,E=E,pres=pres)
     
    orbit_bin(start_time,end_time,mag='Bx',dim=['XSC','YSC'],append=append,slice=slice,v=v,E=E,pres=pres)
    orbit_bin(start_time,end_time,mag='By',dim=['XSC','YSC'],append=append,slice=slice,v=v,E=E,pres=pres)
    orbit_bin(start_time,end_time,mag='Bz',dim=['XSC','YSC'],append=append,slice=slice,v=v,E=E,pres=pres)
    orbit_bin(start_time,end_time,mag='|B|',dim=['XSC','YSC'],append=append,slice=slice,v=v,E=E,pres=pres)
