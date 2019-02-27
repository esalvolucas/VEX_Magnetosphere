from VEX_Magnetosphere import *

def bin_main(start_time,
             end_time,
             ns=False,
             counts=True,
             append=None,
             slice=None,
             slice2=None):
    

    bin_dim(start_time,end_time,mag='Bx',dim=['YSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
    bin_dim(start_time,end_time,mag='By',dim=['YSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
    bin_dim(start_time,end_time,mag='Bz',dim=['YSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
    bin_dim(start_time,end_time,mag='|B|',dim=['YSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)

    bin_dim(start_time,end_time,mag='Bx',dim=['XSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
    bin_dim(start_time,end_time,mag='By',dim=['XSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
    bin_dim(start_time,end_time,mag='Bz',dim=['XSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
    bin_dim(start_time,end_time,mag='|B|',dim=['XSC','ZSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
    
    bin_dim(start_time,end_time,mag='Bx',dim=['XSC','YSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
    bin_dim(start_time,end_time,mag='By',dim=['XSC','YSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
    bin_dim(start_time,end_time,mag='Bz',dim=['XSC','YSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
    bin_dim(start_time,end_time,mag='|B|',dim=['XSC','YSC'],ns=ns,counts=counts,append=append,slice=slice,slice2=slice2)
    
#bin_main('2014-01-01','2014-03-01',ns=True,append='testBS')
#bin_main('2014-09-14','2014-12-14',ns=True,append='avg3')
bin_main('2014-09-14','2014-12-14',slice=True,append='avg025z3')
bin_main('2014-09-14','2014-12-14',slice2=True,append='avg025y3')