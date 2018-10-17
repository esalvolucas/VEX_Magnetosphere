import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
import matplotlib.colors
import matplotlib.colorbar
from colormap import rgb2hex
from matplotlib import ticker


def plot_3D(table):
        
    fig = plt.figure()
    # ax = fig.gca(projection='3d')
    ###########
    ax = fig.add_subplot(111, projection='3d')
    cax = plt.axes([0.85, 0.1, 0.035, 0.8])
    plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
    
    #cax = fig.add_subplot(122)
    ###############
    # grab table range for plot title
    table_start = str(np.array(table.index.values[0], dtype='datetime64[s]'))
    table_end = str(np.array(table.index.values[-1], dtype='datetime64[s]'))
    time_range_str = table_start + ' TO ' + table_end
    time = table.index.values
    num_ti = len(time)-1
    mag_line_i = []
    
    scale = 300  # km/nT
    n = 100  # vectors
    
    # plot VEX orbit
    ax.plot(table['XSC'], table['YSC'], table['ZSC'])
    
    # linspace the # of vectors wanted
    for i in np.linspace(0, num_ti, num=n):
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
        # Plot the thing
        bplot = ax.plot([table['XSC'][item], table['XSC'][item]+scale*table['Bx'][item]],
                        [table['YSC'][item], table['YSC'][item]+scale*table['By'][item]],
                        [table['ZSC'][item], table['ZSC'][item]+scale*table['Bz'][item]],
                        color=color)
    # This does not work and I do not know why...doesn't matter where you put it, or if you pass it bplot, fig, ax...
    # it just keeps throwing errors. You'll have to look into it.
    cb = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, ticks=bounds, orientation='vertical')
    cb.set_label('|B| Strength (nT)')
    tick_locator = ticker.MaxNLocator(nbins=10)
    cb.locator = tick_locator
    cb.update_ticks()
    
    #add venus to plot
    #add_venus_3D(ax)
    color_hemisphere(ax)
    #scale axes to mostly square
    ax.auto_scale_xyz([-35000, 35000], [-35000, 35000], [-65000, 5000])
    
    
    #set labels
    ax.set_xlabel('VSO X')
    ax.set_ylabel('VSO Y')
    ax.set_zlabel('VSO Z')
    
    #add sun vector
    #ax.quiver(0,0,0,35000,0,0,length=1.0,arrow_length_ratio=0.1,color=(1,1,0))

    #ax.set_facecolor('xkcd:slate grey')
    ax.w_xaxis.set_pane_color((112/255,128/255,144/255))
    ax.w_yaxis.set_pane_color((112/255,128/255,144/255))
    ax.w_zaxis.set_pane_color((112/255,128/255,144/255))
    
    #plot title
    ax.set_title('VEX Orbit MAG Data: '+time_range_str)
    #plt.title('VEX Orbit MAG Data: '+time_range_str)
    plt.show()
    
def add_venus_3D(ax):
    #add wireframe sphere representing venus
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v)
    
    r = 6051.8 #km (venus radius)
    #plot orange wireframe sphere
    ax.plot_wireframe(r*x, r*y, r*z, color=(1,165/255,0),alpha=0.5)
    
def color_hemisphere(ax):
    # Create a sphere
    r = 6051.8
    pi = np.pi
    cos = np.cos
    sin = np.sin
    phi, theta = np.mgrid[0.0:0.5*pi:90j, 0.0:2.0*pi:360j] # phi = alti, theta = azi
    #plot nightside
    z = -r*sin(phi)*cos(theta)
    y = r*sin(phi)*sin(theta)
    x = -r*cos(phi)    
    ax.plot_surface(
        x, y, z,  rstride=4, cstride=4, color='b', alpha=0.1, linewidth=0)    
    ax.plot_wireframe(x, y, z, color="k")
    #plot dayside
    z = r*sin(phi)*cos(theta)
    y = r*sin(phi)*sin(theta)                    
    x = r*cos(phi) 
    ax.plot_surface(
        x, y, z,  rstride=4, cstride=4, color='w', alpha=0.1, linewidth=0)    
    ax.plot_wireframe(x, y, z, color="w")