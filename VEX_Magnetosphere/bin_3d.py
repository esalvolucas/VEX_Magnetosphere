import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np
from matplotlib import ticker
from VEX_Magnetosphere import *

def bin_3d(final_stat,final_x,final_y,dim='x',v_toggle='off',save=False,name=None,title=None):
    #initialize colorbar label
    bindim = r'$B_{' + dim + r'}$ Strength (nT)'
    print(bindim)
    #create figure
    fig,ax = plt.subplots(nrows=1, ncols=1)
    #create colorbar axis
    cax = plt.axes([0.85, 0.1, 0.05, 0.8])
    #adjust main plot to make room for colorbar
    plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
    #create edges between -3 and 3 Rv
    yedges = np.arange(-3,3,0.1)
    zedges = np.arange(-3,3,0.1)
    #make meshgrid to plot bins
    ymesh,zmesh = np.meshgrid(yedges,zedges)
    #add venus as black circle
    venus1=plt.Circle((0,0),1,color='k',fill=False)
    ax.add_artist(venus1)
    #pick r/w/b divergent colormap
    cmap = plt.get_cmap('seismic')
    #pick bounds for colorbar to be -20 to 20 with 60 distinct colors
    bounds = np.linspace(-20, 20, 60)
    #set colorbar norm and other settings
    norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
    cb = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, ticks=bounds, orientation='vertical')
    cb.set_label(bindim)
    tick_locator = ticker.MaxNLocator(nbins=11)
    cb.locator = tick_locator
    cb.update_ticks()
    #plot bins
    ax.pcolormesh(ymesh,zmesh,final_stat,cmap=cmap,vmin=-20,vmax=20)

    #set axis limits     
    ax.set_xlim(-3,3)
    ax.set_ylim(-3,3)
    
    #set axis labels
    if dim == 'x':
        ax.set_xlabel('YSC')
        ax.set_ylabel('ZSC')
    elif dim == 'y':
        ax.set_xlabel('XSC')
        ax.set_ylabel('ZSC')
    elif dim == 'z':
        ax.set_xlabel('XSC')
        ax.set_ylabel('YSC')
    
    #toggle 2D venus on/off
    if v_toggle == 'on':
        if dim == 'x':
            add_venus_2D((0,0), 1, 90, ax, colors=('w','w'))
        elif dim == 'y':
            add_venus_2D((0,0), 1, 90, ax, colors=('k','w'))
        elif dim == 'z':
            add_venus_2D((0,0), 1, 90, ax, colors=('k','w'))
        
    #create mesh to plot vectors in middle of each bin    
    yedges = np.arange(-2.95,3.05,0.1)
    zedges = np.arange(-2.95,3.05,0.1)
    ymesh,zmesh = np.meshgrid(yedges,zedges)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    X = ymesh
    Y = zmesh
    U = final_x
    V = final_y
    #add magnetic field direction vectors, autoscale length
    ax.quiver(X, Y, U, V)

    #set title, either show/save figure            
    if title != None:
        ax.set_title(title)
    if save == False: 
        plt.show()
    if save == True:
        plt.savefig(name+'.png')

    