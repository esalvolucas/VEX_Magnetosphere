import numpy as np
import matplotlib.pyplot as plt
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
    n = 100 #vectors
    
    #plot VEX orbut
    ax.plot(table['XSC'],table['YSC'],table['ZSC'])
    
    #linspace the # of vectors wanted
    for i in np.linspace(0, num_ti, num=n):
        mag_line_i = mag_line_i + [int(round(i))]

    #plot each MAG 3D vector individually
    for i in mag_line_i:
        Bplot = ax.plot([table['XSC'][i],table['XSC'][i]+scale*table['Bx'][i]],
                        [table['YSC'][i],table['YSC'][i]+scale*table['By'][i]],
                        [table['ZSC'][i],table['ZSC'][i]+scale*table['Bz'][i]],
                        color='r')
        #print(Bplot)
        #fig.colorbar(Bplot)
#     print(len(table['ZSC'].values))
#     print(len(table['ZSC'].values+scale*table['Bx'].values))
#     Bplot = ax.plot([table['XSC'].values,table['XSC'].values+scale*table['Bx'].values],
#                         [table['YSC'].values,table['YSC'].values+scale*table['By'].values],
#                         [table['ZSC'].values,table['ZSC'].values+scale*table['Bz'].values])
        #fig.colorbar(Bplot)
#     plt.set_cmap('plasma')
    
    #add venus to plot
    add_venus_3D(ax)
    
    #scale axes to mostly square
    ax.auto_scale_xyz([-35000, 35000], [-35000, 35000], [-65000, 5000])
    
    #set labels
    ax.set_xlabel('VSO X')
    ax.set_ylabel('VSO Y')
    ax.set_zlabel('VSO Z')
    
    #add sun vector
    ax.quiver(0,0,0,35000,0,0,length=1.0,arrow_length_ratio=0.1,color=(1,1,0))

    #plot title
    plt.title('VEX Orbit MAG Data: '+time_range_str)
    plt.show()
    
def add_venus_3D(ax):
    #add wireframe sphere representing venus
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v)
    
    r = 6051.8 #km (venus radius)
    #plot orange wireframe sphere
    ax.plot_wireframe(r*x, r*y, r*z, color=(1,165/255,0))