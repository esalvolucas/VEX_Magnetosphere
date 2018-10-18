import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
import matplotlib.colors
import matplotlib.colorbar
from colormap import rgb2hex
import cv2
from cv2 import ellipse
import matplotlib.patches
from matplotlib.patches import Arc
from VEX_Magnetosphere.add_venus_2D import add_venus_2D
from matplotlib import ticker



def VSO_avg(table):

    #grab table range for plot title
    table_start = str(np.array(table.index.values[0], dtype='datetime64[s]'))
    table_end = str(np.array(table.index.values[-1], dtype='datetime64[s]'))
    time_range_str = table_start + ' TO ' + table_end
    time = table.index.values
    #num_ti = len(time)-1
    mag_line_i = []
    
    
    #n = 100  # vectors
    r = 6051.8
    scale = 500/r  # venus radii/nT
    
    #scale location data by venus radius
    table['XSC'] = table['XSC']/r
    table['YSC'] = table['YSC']/r
    table['ZSC'] = table['ZSC']/r
    table['RSC'] = table['RSC']/r
    
    #plot location data
    fig, (ax1,ax2,ax3) = plt.subplots(nrows=1, ncols=3,sharex=True,sharey=True)
    ax1.plot(table['XSC'],table['YSC'], color = (139/255,0,0))
    ax2.plot(table['XSC'],table['ZSC'], color = (139/255,0,0))
    ax3.plot(table['YSC'],table['ZSC'], color = (139/255,0,0))

    #set axis labels
    ax1.set(xlabel='VSO X', ylabel='VSO Y')
    ax2.set(xlabel='VSO X', ylabel='VSO Z')
    ax3.set(xlabel='VSO Y', ylabel='VSO Z')



    cax = plt.axes([0.93, 0.1, 0.020, 0.8])
    plt.subplots_adjust(bottom=0.1, left=0.07, right=0.91, top=0.9)
    
    
    
    
    #downsample table to minute cadence
    table = table.resample('T').mean()
    
    time = table.index.values
    num_ti = len(time)-1
    print(num_ti)
    #linspace the # of vectors wanted
    for i in np.linspace(0, num_ti, num=num_ti):
        mag_line_i = mag_line_i + [int(round(i))]
    
    # define 3rd-axis values
    #o_mags_1 = table['Bz'].values # X vs Y
    #o_mags_2 = table['By'].values # X vs Z
    #o_mags_3 = table['Bx'].values # Y vs Z

    # define the colormap
    cmap = plt.get_cmap('viridis')
    # define the bins and normalize
#     bounds1 = np.linspace(np.nanmin(o_mags_1), np.nanmax(o_mags_1), 60)
#     norm1 = matplotlib.colors.BoundaryNorm(bounds1, cmap.N)
# 
#     bounds2 = np.linspace(np.nanmin(o_mags_2), np.nanmax(o_mags_2), 60)
#     norm2 = matplotlib.colors.BoundaryNorm(bounds2, cmap.N)
#     
#     bounds3 = np.linspace(np.nanmin(o_mags_3), np.nanmax(o_mags_3), 60)
#     norm3 = matplotlib.colors.BoundaryNorm(bounds3, cmap.N)
    
    #o_mags = list(o_mags_1) + list(o_mags_2) + list(o_mags_3)
    o_mags = table['|B|'].values
    bounds = np.linspace(np.nanmin(o_mags), np.nanmax(o_mags), 60)
    norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
    
    
    # plot each MAG 3D vector individually
    for i, item in enumerate(mag_line_i):
        # Getting the color for the Bz line
#         r = cmap(norm(o_mags_1[i]), bytes=True)[0]
#         g = cmap(norm(o_mags_1[i]), bytes=True)[1]
#         b = cmap(norm(o_mags_1[i]), bytes=True)[2]
        r = cmap(norm(o_mags[i]), bytes=True)[0]
        g = cmap(norm(o_mags[i]), bytes=True)[1]
        b = cmap(norm(o_mags[i]), bytes=True)[2]
        color1 = rgb2hex(r, g, b)
        # Plot
        bplot_1 = ax1.plot([table['XSC'][item], table['XSC'][item]+scale*table['Bx'][item]],
                        [table['YSC'][item], table['YSC'][item]+scale*table['By'][item]],
                        color=color1)

        # Getting the color for the By line
#         r = cmap(norm(o_mags_2[i]), bytes=True)[0]
#         g = cmap(norm(o_mags_2[i]), bytes=True)[1]
#         b = cmap(norm(o_mags_2[i]), bytes=True)[2]
        r = cmap(norm(o_mags[i]), bytes=True)[0]
        g = cmap(norm(o_mags[i]), bytes=True)[1]
        b = cmap(norm(o_mags[i]), bytes=True)[2]
        color2 = rgb2hex(r, g, b)
        # Plot
        bplot_2 = ax2.plot([table['XSC'][item], table['XSC'][item]+scale*table['Bx'][item]],
                        [table['ZSC'][item], table['ZSC'][item]+scale*table['Bz'][item]],
                        color=color2)
        
        # Getting the color for the Bx line
#         r = cmap(norm(o_mags_3[i]), bytes=True)[0]
#         g = cmap(norm(o_mags_3[i]), bytes=True)[1]
#         b = cmap(norm(o_mags_3[i]), bytes=True)[2]
        r = cmap(norm(o_mags[i]), bytes=True)[0]
        g = cmap(norm(o_mags[i]), bytes=True)[1]
        b = cmap(norm(o_mags[i]), bytes=True)[2]
        color3 = rgb2hex(r, g, b)
        # Plot
        bplot_3 = ax3.plot([table['YSC'][item], table['YSC'][item]+scale*table['By'][item]],
                        [table['ZSC'][item], table['ZSC'][item]+scale*table['Bz'][item]],
                        color=color3)
        
        
    cb = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, ticks=bounds, orientation='vertical')
    cb.set_label(r'$B_{\perp}$ Strength (nT)')
    tick_locator = ticker.MaxNLocator(nbins=11)
    cb.locator = tick_locator
    cb.update_ticks()
    
    #add circle to represent venus
    add_venus_2D((0,0), radius=1, angle=90, ax=ax1, colors=('k','w'))
    add_venus_2D((0,0), radius=1, angle=90, ax=ax2, colors=('k','w'))
    add_venus_2D((0,0), radius=1, angle=90, ax=ax3, colors=('w','w'))

    #darken plot background
    ax1.set_facecolor('xkcd:slate grey')
    ax2.set_facecolor('xkcd:slate grey')
    ax3.set_facecolor('xkcd:slate grey')
    
    #set title above middle plot
    ax2.set(title='VEX Orbit MAG Data: '+time_range_str)
    
    #standardize plot limits
    #ax1.set_xlim([-5.5,3.5])
    #ax1.set_ylim([-12,2.5])    
    #ax2.set_xlim([-5.5,3.5])
    #ax2.set_ylim([-12,2.5])   
    #ax3.set_xlim([-5.5,3.5])
    #ax3.set_ylim([-12,2.5])
    
    
    plt.show()
    