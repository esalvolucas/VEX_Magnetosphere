import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

def plot_3D(table):
        
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    #grab table range for plot title
    table_start = str(np.array(table.index.values[0], dtype='datetime64[s]'))
    table_end = str(np.array(table.index.values[-1], dtype='datetime64[s]'))
    time_range_str = table_start + ' TO ' + table_end
    time = table.index.values
    num_ti = len(time)-1
    mag_line_i = []
    
    scale = 300 #km/T
    
    #linspace the # of vectors wanted
    for i in np.linspace(0, num_ti, num=100):
        mag_line_i = mag_line_i + [int(round(i))]
        
    for i in mag_line_i:
#         print(table['Bx'][i], table['By'][i])
#         #if positive direction, red
#         if table['Bz'][i] > 0:
#             c = 'r'
#         #if negative direction, blue
#         else:
#             c = 'b'
        Bplot = ax.plot([table['XSC'][i],table['XSC'][i]+scale*table['Bx'][i]],
                        [table['YSC'][i],table['YSC'][i]+scale*table['By'][i]],
                        [table['ZSC'][i],table['ZSC'][i]+scale*table['Bz'][i]],
                        color='r')
        #fig.colorbar(Bplot)
    ax.plot(table['XSC'],table['YSC'],table['ZSC'])
    add_venus_3D(ax)
    ax.auto_scale_xyz([-35000, 35000], [-35000, 35000], [-65000, 5000])
    
    ax.set_xlabel('VSO X')
    ax.set_ylabel('VSO Y')
    ax.set_zlabel('VSO Z')
    
    ax.quiver(0,0,0,35000,0,0,length=1.0,arrow_length_ratio=0.1,color='y')

    plt.title('VEX Orbit MAG Data: '+time_range_str)
    plt.show()
    
def add_venus_3D(ax):
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v)
    
    r = 6051.8
    ax.plot_wireframe(r*x, r*y, r*z, color=(1,165/255,0))