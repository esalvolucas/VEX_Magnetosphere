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
from matplotlib.patches import Wedge



def orbit_mag_plot(table):
    #grab table range for plot title
    table_start = str(np.array(table.index.values[0], dtype='datetime64[s]'))
    table_end = str(np.array(table.index.values[-1], dtype='datetime64[s]'))
    time_range_str = table_start + ' TO ' + table_end
    time = table.index.values
    num_ti = len(time)-1
    mag_line_i = []
    
    scale = 300  # km/T
    n = 100  # vectors
    
    #linspace the # of vectors wanted
    for i in np.linspace(0, num_ti, num=n):
        mag_line_i = mag_line_i + [int(round(i))]
    #plot data
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.plot(table['XSC'],table['YSC'], color = 'c')
    ax.set(xlabel='VSO X', ylabel='VSO Y')
    
    
    # Get a list of the overall magnetic field magnitudes for the desired times
    # Values from table
    overall_mag = table['Bz'].values
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
                        color=color)
        
        #print(table['Bz'].values[i])
#     for i in mag_line_i:
# 
#         Bplot = ax.plot([table['XSC'][i],table['XSC'][i]+100*table['Bx'][i]],
#                         [table['YSC'][i],table['YSC'][i]+100*table['By'][i]],
#                         color=c)
    #cbar = fig.colorbar(Bplot, ticks=[min(table['Bz'].values), np.median(table['Bz'].values), max(table['Bz'].values)])
    #cbar.ax.set_yticklabels(['?', '?', '?'])
    
    
    #add circle to represent venus
    #add_venus(ax)
    #plt.grid(b=True, which='major', axis='both')

    dual_half_circle((0, 0), radius=6051.8, angle=90, ax=ax)


    #square axes
    ax.axis('equal')
    
    ax.set_facecolor('xkcd:slate grey')

    ax.set(title='VEX Orbit MAG Data: '+time_range_str)
    
    return fig,ax
    #plt.show()
    
# def add_venus(ax):
#     #make venus orange circle w/ accepted venus radius, 6051.8 km
#     r = 6051.8
#     #venus = plt.Circle((0,0), 6051.8,color=(1,165/255,0))
#     #ax.add_artist(venus)
#     
#     # generate the points
#     theta = np.linspace(np.radians(-90), np.radians(90))
#     points = np.vstack((r*np.cos(theta),r*np.sin(theta))
#     # build the polygon and add it to the axes
#     #poly = matplotlib.patches.Polygon(points.T, closed=True)
#     #ax.add_patch(poly)
# 
#     
#     #ellipse(ax, (0,0), (6052,6052), -90, -90, 90, 'k')
    
def dual_half_circle(center, radius, angle=0, ax=None, colors=('w','k')):
    """
    Add two half circles to the axes *ax* (or the current axes) with the 
    specified facecolors *colors* rotated at *angle* (in degrees).
    """
    if ax is None:
        ax = plt.gca()
    theta1, theta2 = angle, angle + 180
    w1 = Wedge(center, radius, theta1, theta2, fc=colors[0])
    w2 = Wedge(center, radius, theta2, theta1, fc=colors[1])
    for wedge in [w1, w2]:
        ax.add_artist(wedge)
    return [w1, w2]