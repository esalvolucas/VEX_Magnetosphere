import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
import matplotlib.colors
import matplotlib.colorbar
from colormap import rgb2hex
from VEX_Magnetosphere.add_venus_3D import add_venus_3D
from matplotlib import ticker


def VSO_3D_avg(table):
        
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # grab table range for plot title
    table_start = str(np.array(table.index.values[0], dtype='datetime64[s]'))
    table_end = str(np.array(table.index.values[-1], dtype='datetime64[s]'))
    time_range_str = table_start + ' TO ' + table_end
    time = table.index.values
    num_ti = len(time)-1
    mag_line_i = []
    
    r = 6051.8
    scale = 300/r  # venus radii/T
    
    table['XSC'] = table['XSC']/r
    table['YSC'] = table['YSC']/r
    table['ZSC'] = table['ZSC']/r
    table['RSC'] = table['RSC']/r
    
    # plot VEX orbit
    ax.plot(table['XSC'], table['YSC'], table['ZSC'], color = (139/255,0,0))
    
    cax = plt.axes([0.85, 0.1, 0.035, 0.8])
    plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
    
    #resample table to minute cadence
    table = table.resample('T').mean()
    
    time = table.index.values
    num_ti = len(time)-1
    print(num_ti)
    #linspace the # of vectors wanted
    for i in np.linspace(0, num_ti, num=num_ti):
        mag_line_i = mag_line_i + [int(round(i))]

    # Get a list of the overall magnetic field magnitudes for the desired times
    # Values from table
    overall_mag = table['|B|'].values
    # Now get a list
    o_mags = list()
    for i in mag_line_i:
        o_mags.append(overall_mag[i])

    # define the colormap
    cmap = plt.get_cmap('viridis')
    # define the bins and normalize
    bounds = np.linspace(np.nanmin(o_mags), np.nanmax(o_mags), 60)
    norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)

    # plot each MAG 3D vector individually
    for i, item in enumerate(mag_line_i):
        # Getting the color for the vector line
        r = cmap(norm(o_mags[i]), bytes=True)[0]
        g = cmap(norm(o_mags[i]), bytes=True)[1]
        b = cmap(norm(o_mags[i]), bytes=True)[2]
        color = rgb2hex(r, g, b)
        # Plot
        bplot = ax.plot([table['XSC'][item], table['XSC'][item]+scale*table['Bx'][item]],
                        [table['YSC'][item], table['YSC'][item]+scale*table['By'][item]],
                        [table['ZSC'][item], table['ZSC'][item]+scale*table['Bz'][item]],
                        color=color)
    # This does not work and I do not know why...doesn't matter where you put it, or if you pass it bplot, fig, ax...
    # it just keeps throwing errors. You'll have to look into it.
    # cb = matplotlib.colorbar.ColorbarBase(bplot, cmap=cmap, norm=norm, ticks=bounds, orientation='vertical')
    # cb.set_label('Some Units')
    cb = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, ticks=bounds, orientation='vertical')
    cb.set_label('|B| Strength (nT)')
    tick_locator = ticker.MaxNLocator(nbins=11)
    cb.locator = tick_locator
    cb.update_ticks()
    
    #add venus to plot
    add_venus_3D(ax)
    #scale axes to mostly square
    
    #set labels
    ax.set_xlabel('VSO X')
    ax.set_ylabel('VSO Y')
    ax.set_zlabel('VSO Z')
    
    #add sun vector
    #ax.quiver(0,0,0,35000,0,0,length=1.0,arrow_length_ratio=0.1,color=(1,1,0))

    # darken plot background
    ax.w_xaxis.set_pane_color((112/255,128/255,144/255))
    ax.w_yaxis.set_pane_color((112/255,128/255,144/255))
    ax.w_zaxis.set_pane_color((112/255,128/255,144/255))
    
    #set axis ranges
    X = table['XSC']
    Y = table['YSC']
    Z = table['ZSC']
        
    max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0
    
    mid_x = (X.max()+X.min()) * 0.5
    mid_y = (Y.max()+Y.min()) * 0.5
    mid_z = (Z.max()+Z.min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    
    #plot title
    ax.set_title('VEX Orbit MAG Data: '+time_range_str)
    
    plt.show()