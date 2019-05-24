from VEX_Magnetosphere import *
from time import sleep

def plotgen(startdate,enddate,pres=None,v=None,E=None):
    ## PRESSURE SORTING ##
    if pres!=None:
        #-0.25 < YSC < 0.25
        bin_main(startdate,enddate,slice=['YSC',-0.25,0.25],append='YSClow',pres='low')
        map_plots(startdate,enddate,append='YSClow',slicedir='YSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['YSC',-0.25,0.25],append='YSCmed',pres='med')
        map_plots(startdate,enddate,append='YSCmed',slicedir='YSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['YSC',-0.25,0.25],append='YSChigh',pres='high')
        map_plots(startdate,enddate,append='YSChigh',slicedir='YSC',pres=pres)
        sleep(7)
        
        #-0.25 < ZSC < 0.25
        bin_main(startdate,enddate,slice=['ZSC',-0.25,0.25],append='ZSClow',pres='low')
        map_plots(startdate,enddate,append='ZSClow',slicedir='ZSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['ZSC',-0.25,0.25],append='ZSCmed',pres='med')
        map_plots(startdate,enddate,append='ZSCmed',slicedir='ZSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['ZSC',-0.25,0.25],append='ZSChigh',pres='high')
        map_plots(startdate,enddate,append='ZSChigh',slicedir='ZSC',pres=pres)
        sleep(7)
        
        #1.0 < ZSC < 1.5
        bin_main(startdate,enddate,slice=['ZSC',1.0,1.5],append='ZSC115low',pres='low')
        map_plots(startdate,enddate,append='ZSC115low',slicedir='ZSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['ZSC',1.0,1.5],append='ZSC115med',pres='med')
        map_plots(startdate,enddate,append='ZSC115med',slicedir='ZSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['ZSC',1.0,1.5],append='ZSC115high',pres='high')
        map_plots(startdate,enddate,append='ZSC115high',slicedir='ZSC',pres=pres)
        sleep(7)
        
        #-1.5 < ZSC < -1.0
        bin_main(startdate,enddate,slice=['ZSC',-1.5,-1.0],append='ZSC-115low',pres='low')
        map_plots(startdate,enddate,append='ZSC-115low',slicedir='ZSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['ZSC',-1.5,-1.0],append='ZSC-115med',pres='med')
        map_plots(startdate,enddate,append='ZSC-115med',slicedir='ZSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['ZSC',-1.5,-1.0],append='ZSC-115high',pres='high')
        map_plots(startdate,enddate,append='ZSC-115high',slicedir='ZSC',pres=pres)
        sleep(7)
         
        #0.75 < XSC < 1.25
        bin_main(startdate,enddate,slice=['XSC',0.75,1.25],append='XSClow',pres='low')
        map_plots(startdate,enddate,append='XSClow',slicedir='XSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',0.75,1.25],append='XSCmed',pres='med')
        map_plots(startdate,enddate,append='XSCmed',slicedir='XSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',0.75,1.25],append='XSChigh',pres='high')
        map_plots(startdate,enddate,append='XSChigh',slicedir='XSC',pres=pres)
        sleep(7)
         
        #-2.0 < XSC < -1.0
        bin_main(startdate,enddate,slice=['XSC',-2.0,-1.0],append='XSCNSlow',pres='low')
        map_plots(startdate,enddate,append='XSCNSlow',slicedir='XSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',-2.0,-1.0],append='XSCNSmed',pres='med')
        map_plots(startdate,enddate,append='XSCNSmed',slicedir='XSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',-2.0,-1.0],append='XSCNShigh',pres='high')
        map_plots(startdate,enddate,append='XSCNShigh',slicedir='XSC',pres=pres)
        sleep(7)
         
        #0.5 < XSC < 1.0
        bin_main(startdate,enddate,slice=['XSC',0.5,1.0],append='XSC0510low',pres='low')
        map_plots(startdate,enddate,append='XSC0510low',slicedir='XSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',0.5,1.0],append='XSC0510med',pres='med')
        map_plots(startdate,enddate,append='XSC0510med',slicedir='XSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',0.5,1.0],append='XSC0510high',pres='high')
        map_plots(startdate,enddate,append='XSC0510high',slicedir='XSC',pres=pres)
        sleep(7)
            
        #0.0 < XSC < 0.5
        bin_main(startdate,enddate,slice=['XSC',0.0,0.5],append='XSC0005low',pres='low')
        map_plots(startdate,enddate,append='XSC0005low',slicedir='XSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',0.0,0.5],append='XSC0005med',pres='med')
        map_plots(startdate,enddate,append='XSC0005med',slicedir='XSC',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',0.0,0.5],append='XSC0005high',pres='high')
        map_plots(startdate,enddate,append='XSC0005high',slicedir='XSC',pres=pres)
        sleep(7)
            
        #All
        bin_main(startdate,enddate,slice=None,append='alllow',pres='low')
        map_plots(startdate,enddate,append='alllow',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=None,append='allmed',pres='med')
        map_plots(startdate,enddate,append='allmed',pres=pres)
        sleep(7)
        bin_main(startdate,enddate,slice=None,append='allhigh',pres='high')
        map_plots(startdate,enddate,append='allhigh',pres=pres)

    ## VELOCITY SORTING ##
    if v!=None:
        #-0.25 < YSC < 0.25
        bin_main(startdate,enddate,slice=['YSC',-0.25,0.25],append='YSClow',v='low')
        map_plots(startdate,enddate,append='YSClow',slicedir='YSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['YSC',-0.25,0.25],append='YSCmed',v='med')
        map_plots(startdate,enddate,append='YSCmed',slicedir='YSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['YSC',-0.25,0.25],append='YSChigh',v='high')
        map_plots(startdate,enddate,append='YSChigh',slicedir='YSC',v=v)
        sleep(7)
          
        #-0.25 < ZSC < 0.25
        bin_main(startdate,enddate,slice=['ZSC',-0.25,0.25],append='ZSClow',v='low')
        map_plots(startdate,enddate,append='ZSClow',slicedir='ZSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['ZSC',-0.25,0.25],append='ZSCmed',v='med')
        map_plots(startdate,enddate,append='ZSCmed',slicedir='ZSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['ZSC',-0.25,0.25],append='ZSChigh',v='high')
        map_plots(startdate,enddate,append='ZSChigh',slicedir='ZSC',v=v)
        sleep(7)
        
        #1.0 < ZSC < 1.5
        bin_main(startdate,enddate,slice=['ZSC',1.0,1.5],append='ZSC115low',v='low')
        map_plots(startdate,enddate,append='ZSC115low',slicedir='ZSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['ZSC',1.0,1.5],append='ZSC115med',v='med')
        map_plots(startdate,enddate,append='ZSC115med',slicedir='ZSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['ZSC',1.0,1.5],append='ZSC115high',v='high')
        map_plots(startdate,enddate,append='ZSC115high',slicedir='ZSC',v=v)
        sleep(7)
        
        #-1.5 < ZSC < -1.0
        bin_main(startdate,enddate,slice=['ZSC',-1.5,-1.0],append='ZSC-115low',v='low')
        map_plots(startdate,enddate,append='ZSC-115low',slicedir='ZSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['ZSC',-1.5,-1.0],append='ZSC-115med',v='med')
        map_plots(startdate,enddate,append='ZSC-115med',slicedir='ZSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['ZSC',-1.5,-1.0],append='ZSC-115high',v='high')
        map_plots(startdate,enddate,append='ZSC-115high',slicedir='ZSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['ZSC',1.0,1.5],append='ZSC115med',v='med')    
        
        #0.75 < XSC < 1.25
        bin_main(startdate,enddate,slice=['XSC',0.75,1.25],append='XSClow',v='low')
        map_plots(startdate,enddate,append='XSClow',slicedir='XSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',0.75,1.25],append='XSCmed',v='med')
        map_plots(startdate,enddate,append='XSCmed',slicedir='XSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',0.75,1.25],append='XSChigh',v='high')
        map_plots(startdate,enddate,append='XSChigh',slicedir='XSC',v=v)
        sleep(7)
          
        #-2.0 < XSC < -1.0
        bin_main(startdate,enddate,slice=['XSC',-2.0,-1.0],append='XSCNSlow',v='low')
        map_plots(startdate,enddate,append='XSCNSlow',slicedir='XSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',-2.0,-1.0],append='XSCNSmed',v='med')
        map_plots(startdate,enddate,append='XSCNSmed',slicedir='XSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',-2.0,-1.0],append='XSCNShigh',v='high')
        map_plots(startdate,enddate,append='XSCNShigh',slicedir='XSC',v=v)
        sleep(7)
            
        #0.5 < XSC < 1.0
        bin_main(startdate,enddate,slice=['XSC',0.5,1.0],append='XSC0510low',v='low')
        map_plots(startdate,enddate,append='XSC0510low',slicedir='XSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',0.5,1.0],append='XSC0510med',v='med')
        map_plots(startdate,enddate,append='XSC0510med',slicedir='XSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',0.5,1.0],append='XSC0510high',v='high')
        map_plots(startdate,enddate,append='XSC0510high',slicedir='XSC',v=v)
        sleep(7)
              
        #0.0 < XSC < 0.5
        bin_main(startdate,enddate,slice=['XSC',0.0,0.5],append='XSC0005low',v='low')
        map_plots(startdate,enddate,append='XSC0005low',slicedir='XSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',0.0,0.5],append='XSC0005med',v='med')
        map_plots(startdate,enddate,append='XSC0005med',slicedir='XSC',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=['XSC',0.0,0.5],append='XSC0005high',v='high')
        map_plots(startdate,enddate,append='XSC0005high',slicedir='XSC',v=v)
        sleep(7)
              
        #All
        bin_main(startdate,enddate,slice=None,append='alllow',v='low')
        map_plots(startdate,enddate,append='alllow',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=None,append='allmed',v='med')
        map_plots(startdate,enddate,append='allmed',v=v)
        sleep(7)
        bin_main(startdate,enddate,slice=None,append='allhigh',v='high')
        map_plots(startdate,enddate,append='allhigh',v=v)
        
    if pres == None and v == None and E == None:
        pass
        #0.25 < YSC < 0.25
        bin_main(startdate,enddate,slice=['YSC',-0.25,0.25],append='YSCall')
        map_plots(startdate,enddate,append='YSCall',slicedir='YSC')
           
        #0.25 < ZSC < 0.25
        bin_main(startdate,enddate,slice=['ZSC',-0.25,0.25],append='ZSCall')
        map_plots(startdate,enddate,append='ZSCall',slicedir='ZSC')
        sleep(7)
         
        #0.75 < XSC < 1.25
        bin_main(startdate,enddate,slice=['XSC',0.75,1.25],append='XSCall')
        map_plots(startdate,enddate,append='XSCall',slicedir='XSC')
        sleep(7)
           
        #2.0 < XSC < -1.0
        bin_main(startdate,enddate,slice=['XSC',-2.0,-1.0],append='XSCNSall')
        map_plots(startdate,enddate,append='XSCNSall',slicedir='XSC')
        sleep(7)
             
        #0.5 < XSC < 1.0
        bin_main(startdate,enddate,slice=['XSC',0.5,1.0],append='XSC0510all')
        map_plots(startdate,enddate,append='XSC0510all',slicedir='XSC')
        sleep(7)
               
        #0.0 < XSC < 0.5
        bin_main(startdate,enddate,slice=['XSC',0.0,0.5],append='XSC0005all')
        map_plots(startdate,enddate,append='XSC0005all',slicedir='XSC')
        sleep(7)
        
        #1.0 < ZSC < 1.5
        bin_main(startdate,enddate,slice=['ZSC',1.0,1.5],append='ZSC115low',pres='low')
        map_plots(startdate,enddate,append='ZSC115low',slicedir='ZSC',pres=pres)
        sleep(7)
        
        #-1.5 < ZSC < 1.0
        bin_main(startdate,enddate,slice=['ZSC',-1.5,-1.0],append='ZSC-115low',pres='low')
        map_plots(startdate,enddate,append='ZSC-115low',slicedir='ZSC',pres=pres)
        sleep(7)
        
        #All
        bin_main(startdate,enddate,slice=None,append='all')
        map_plots(startdate,enddate,append='all')
        sleep(7)
        
plotgen('2006-04-25','2014-11-24',pres='on')
plotgen('2006-04-25','2014-11-24',v='on')
plotgen('2006-04-25','2014-11-24')