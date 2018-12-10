from VEX_Magnetosphere import *
from pandas.tslib import Timestamp
from _datetime import time
from datetime import date, timedelta
import matplotlib.pyplot as plt
from VEX_Magnetosphere import magnetosphere_mmo
import matplotlib.colors
import numpy as np
from matplotlib import ticker
from pydivide import bin
from scipy import stats
import _pickle as cPickle

def bin_3d(final_stat,dim='x',v_toggle='off'):
    
    bindim = r'$B_{' + dim + r'}$ Strength (nT)'
    print(bindim)
    fig,ax = plt.subplots(nrows=1, ncols=1)
 
    cax = plt.axes([0.85, 0.1, 0.05, 0.8])
     
    plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
    yedges = np.arange(-3,3,0.1)
    zedges = np.arange(-3,3,0.1)
    ymesh,zmesh = np.meshgrid(yedges,zedges)
    #print(ymesh)
    #print(zmesh)
    venus1=plt.Circle((0,0),1,color='k',fill=False)
    ax.add_artist(venus1)
    #plt.show()
  
    cmap = plt.get_cmap('seismic')
    #o_mags = VSE_table['Bx'].values
    bounds = np.linspace(-20, 20, 60)
    norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
    cb = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, ticks=bounds, orientation='vertical')
    cb.set_label(bindim)
    tick_locator = ticker.MaxNLocator(nbins=11)
    cb.locator = tick_locator
    cb.update_ticks()
    
    ax.pcolormesh(ymesh,zmesh,final_stat,cmap=cmap,vmin=-20,vmax=20)
    #print(final_stat)

#      
    ax.set_xlim(-3,3)
    ax.set_ylim(-3,3)
    
    if dim == 'x':
        ax.set_xlabel('YSC')
        ax.set_ylabel('ZSC')
    elif dim == 'y':
        ax.set_xlabel('XSC')
        ax.set_ylabel('ZSC')
    elif dim == 'z':
        ax.set_xlabel('XSC')
        ax.set_ylabel('YSC')
        
    if v_toggle == 'on':
        if dim == 'x':
            add_venus_2D((0,0), 1, 90, ax, colors=('w','w'))
        elif dim == 'y':
            add_venus_2D((0,0), 1, 90, ax, colors=('k','w'))
        elif dim == 'z':
            add_venus_2D((0,0), 1, 90, ax, colors=('k','w'))
        

    #ax.set(title='VEX Orbit MAG Data: ' + start_time + ' TO ' + end_time)
    #ax.axis('equal')
    plt.show()

    