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



def VSO_xyz_mag(table):
#     if axes == 'xy':
#         xlabel = 'VSO X'
#         ylabel = 'VSO Y'
#         
#         mag_col1 = 'Bx'
#         mag_col2 = 'By'
#         mag_col3 = 'Bz'
#         
#         sc1 = 'XSC'
#         sc2 = 'YSC'
#         sc3 = 'ZSC'
#     
#     elif axes == 'xz':        
#         xlabel = 'VSO X'
#         ylabel = 'VSO Z'
#         
#         mag_col1 = 'Bx'
#         mag_col2 = 'Bz'
#         mag_col3 = 'By'
#         
#         sc1 = 'XSC'
#         sc2 = 'ZSC'
#         sc3 = 'YSC'
#     
#     else: 
#         xlabel = 'VSO Y'
#         ylabel = 'VSO Z'
#         
#         mag_col1 = 'By'
#         mag_col2 = 'Bz'
#         mag_col3 = 'Bx'
#         
#         sc1 = 'YSC'
#         sc2 = 'ZSC'
#         sc3 = 'XSC'
#         
        
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
    fig, (ax1,ax2,ax3) = plt.subplots(nrows=1, ncols=3)
    ax1.plot(table['XSC'],table['YSC'], color = (139/255,0,0))
    ax2.plot(table['XSC'],table['ZSC'], color = (139/255,0,0))
    ax3.plot(table['YSC'],table['ZSC'], color = (139/255,0,0))

    ax1.set(xlabel='VSO X', ylabel='VSO Y')
    ax2.set(xlabel='VSO X', ylabel='VSO Z')
    ax3.set(xlabel='VSO Y', ylabel='VSO Z')

    # Get a list of the overall magnetic field magnitudes for the desired times
    # Values from table
    overall_mag_1 = table['Bz'].values # X vs Y
    overall_mag_2 = table['By'].values # X vs Z
    overall_mag_3 = table['Bx'].values # Y vs Z

    # Now get a list
    o_mags_1 = list()
    o_mags_2 = list()
    o_mags_3 = list()
    
    for i in mag_line_i:
        o_mags_1.append(overall_mag_1[i])
        o_mags_2.append(overall_mag_2[i])
        o_mags_3.append(overall_mag_3[i])

    # define the colormap
    cmap = plt.get_cmap('viridis')
    # define the bins and normalize
    bounds1 = np.linspace(np.nanmin(o_mags_1), np.nanmax(o_mags_1), 60)
    norm1 = matplotlib.colors.BoundaryNorm(bounds1, cmap.N)

    bounds2 = np.linspace(np.nanmin(o_mags_2), np.nanmax(o_mags_2), 60)
    norm2 = matplotlib.colors.BoundaryNorm(bounds2, cmap.N)
    
    bounds3 = np.linspace(np.nanmin(o_mags_3), np.nanmax(o_mags_3), 60)
    norm3 = matplotlib.colors.BoundaryNorm(bounds3, cmap.N)
    
    # plot each MAG 3D vector individually
    for i, item in enumerate(mag_line_i):
        # Getting the color for the vector line
        r = cmap(norm1(o_mags_1[i]), bytes=True)[0]
        g = cmap(norm1(o_mags_1[i]), bytes=True)[1]
        b = cmap(norm1(o_mags_1[i]), bytes=True)[2]
        color1 = rgb2hex(r, g, b)
        # Plot the thing
        bplot_1 = ax1.plot([table['XSC'][item], table['XSC'][item]+scale*table['Bx'][item]],
                        [table['YSC'][item], table['YSC'][item]+scale*table['By'][item]],
                        color=color1)

        # Getting the color for the vector line
        r = cmap(norm2(o_mags_2[i]), bytes=True)[0]
        g = cmap(norm2(o_mags_2[i]), bytes=True)[1]
        b = cmap(norm2(o_mags_2[i]), bytes=True)[2]
        color2 = rgb2hex(r, g, b)
        # Plot the thing
        bplot_2 = ax2.plot([table['XSC'][item], table['XSC'][item]+scale*table['Bx'][item]],
                        [table['ZSC'][item], table['ZSC'][item]+scale*table['Bz'][item]],
                        color=color2)
        
        # Getting the color for the vector line
        r = cmap(norm3(o_mags_3[i]), bytes=True)[0]
        g = cmap(norm3(o_mags_3[i]), bytes=True)[1]
        b = cmap(norm3(o_mags_3[i]), bytes=True)[2]
        color3 = rgb2hex(r, g, b)
        # Plot the thing
        bplot_3 = ax3.plot([table['YSC'][item], table['YSC'][item]+scale*table['By'][item]],
                        [table['ZSC'][item], table['ZSC'][item]+scale*table['Bz'][item]],
                        color=color3)
    #add circle to represent venus
    #add_venus(ax)
    dual_half_circle((0, 0), radius=6051.8, angle=90, ax=ax1, colors=('k','w'))
    dual_half_circle((0, 0), radius=6051.8, angle=90, ax=ax2, colors=('k','w'))
    dual_half_circle((0, 0), radius=6051.8, angle=90, ax=ax3, colors=('w','w'))

    #square axes
    #ax1.axis('equal')
    #ax2.axis('equal')
    #ax3.axis('equal')
    ax1.set_facecolor('xkcd:slate grey')
    ax2.set_facecolor('xkcd:slate grey')
    ax3.set_facecolor('xkcd:slate grey')
    
    ax2.set(title='VEX Orbit MAG Data: '+time_range_str)
    
    ax1.set_xlim([-35000,30000])
    ax1.set_ylim([-80000,20000])
    ax2.set_xlim([-35000,30000])
    ax2.set_ylim([-80000,20000])    
    ax3.set_xlim([-35000,30000])
    ax3.set_ylim([-80000,20000])
    plt.show()
    
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