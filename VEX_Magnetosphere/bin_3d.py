import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np
from matplotlib import ticker
from VEX_Magnetosphere import *

def bin_3d(final_stat,final_x,final_y,dim='x',v_toggle='off',save=False,name=None,title=None,bs='off',magB=False):

    #create figure
    fig,ax = plt.subplots(nrows=1, ncols=1)
    #create colorbar axis
    cax = plt.axes([0.85, 0.1, 0.05, 0.8])
    #adjust main plot to make room for colorbar
    plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
    
    #create edges between -3 and 3 Rv
    yedges = np.arange(-3,3.2,0.2)
    zedges = np.arange(-3,3.2,0.2)
    #make meshgrid to plot bins
    ymesh,zmesh = np.meshgrid(yedges,zedges)
    #add venus as black circle
    venus1=plt.Circle((0,0),1,color='k',fill=False)
    ax.add_artist(venus1)
    if dim=='y':
        ax.plot([-1,1],[0,0],color='k',linestyle='-')
        ax.plot([-0.707,0.707],[0.707,0.707],color='k',linestyle='-')
        ax.plot([-0.707,0.707],[-0.707,-0.707],color='k',linestyle='-')
    if dim=='z':
        venustop=plt.Circle((0,0),0.25,color='k',fill=False)
        ax.add_artist(venustop)
        venustop=plt.Circle((0,0),0.707,color='k',fill=False)
        ax.add_artist(venustop)
    if magB==True:
        #pick r/w/b divergent colormap
        cmap = plt.get_cmap('RdPu')
        #pick bounds for colorbar to be 0 to 30 with 90 distinct colors
        bounds = np.linspace(0, 30, 90)
        #set colorbar norm and other settings
        norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
        cb = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, ticks=bounds, orientation='vertical')
    else:
        #pick r/w/b divergent colormap
        cmap = plt.get_cmap('seismic')
        #pick bounds for colorbar to be -10 to 10 with 60 distinct colors
        bounds = np.linspace(-10, 10, 60)
        #set colorbar norm and other settings
        norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
        cb = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, ticks=bounds, orientation='vertical')
    
    #set colorbar label
    if magB==True:
        cb.set_label(r'$|B|$ Strength (nT)')
    else:
        cb.set_label(r'$B_{' + dim + r'}$ Strength (nT)')
    #set colorbar ticks
    tick_locator = ticker.MaxNLocator(nbins=11)
    cb.locator = tick_locator
    cb.update_ticks()
    if magB==True:
        #plot bins with 0 to 30 nT range
        ax.pcolormesh(ymesh,zmesh,final_stat,cmap=cmap,vmin=0, vmax=30)
    else:
        #plot bins with -10 to 10 nT range
        ax.pcolormesh(ymesh,zmesh,final_stat,cmap=cmap,vmin=-10, vmax=10)

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
    
    #toggle 2D black and white venus on/off
    if v_toggle == 'on':
        if dim == 'x':
            add_venus_2D((0,0), 1, 90, ax, colors=('w','w'))
        elif dim == 'y':
            add_venus_2D((0,0), 1, 90, ax, colors=('k','w'))
        elif dim == 'z':
            add_venus_2D((0,0), 1, 90, ax, colors=('k','w'))
        
    #create mesh to plot vectors in middle of each bin    
    yedges = np.arange(-2.9,3.3,0.2)
    zedges = np.arange(-2.9,3.3,0.2)
    ymesh,zmesh = np.meshgrid(yedges,zedges)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    X = ymesh
    Y = zmesh
    U = final_x/np.sqrt(final_x**2 + final_y**2)
    V = final_y/np.sqrt(final_x**2 + final_y**2)
    #add magnetic field direction vectors, autoscale length
    ax.quiver(X, Y, U, V,scale=25)

    #add BS to plots dependent on projection
    if bs=='on':
        L = 1.303
        epsilon = 1.056
        x0 = 0.788
        x = np.arange(-3,3,0.001)
        BS = np.sqrt(L**2 - 2*epsilon*(x-x0)*L - (epsilon**2 - 1)*(x-x0)**2)

        if dim == 'x':
            BS_YZ = plt.Circle((0,0),1.94804,color='k',linestyle=":",fill=False)
            ax.add_artist(BS_YZ)
            BS_YZ = plt.Circle((0,0),2.50004,color='k',linestyle=":",fill=False)
            ax.add_artist(BS_YZ)
            BS_YZ = plt.Circle((0,0),2.91123,color='k',linestyle=":",fill=False)
            ax.add_artist(BS_YZ)
        if dim == 'y' or dim == 'z':
            ax.plot(x,BS,color='k',linestyle=':')
            ax.plot(x,-BS,color='k',linestyle=':')
            
    #set title, either show/save figure            
    if title != None:
        ax.set_title(title)
    if save == False: 
        plt.show()
    if save == True:
        plt.savefig(name+'.png')
        plt.clf()
        plt.cla()

    