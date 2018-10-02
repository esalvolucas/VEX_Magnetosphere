import matplotlib.pyplot as plt
import numpy as np

def orbit_mag_plot(table):
    #grab table range for plot title
    table_start = str(np.array(table.index.values[0], dtype='datetime64[s]'))
    table_end = str(np.array(table.index.values[-1], dtype='datetime64[s]'))
    time_range_str = table_start + ' TO ' + table_end
    time = table.index.values
    num_ti = len(time)-1
    mag_line_i = []
    #linspace the # of vectors wanted
    for i in np.linspace(0, num_ti, num=200):
        mag_line_i = mag_line_i + [int(round(i))]
    #plot data
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.plot(table['XSC'],table['YSC'], color = 'c')
    ax.set(xlabel='VSO X', ylabel='VSO Y')
    for i in mag_line_i:
        print(table['Bx'][i], table['By'][i])
        #if positive direction, red
        if table['Bz'][i] > 0:
            c = 'r'
        #if negative direction, blue
        else:
            c = 'b'
        ax.plot([table['XSC'][i],table['XSC'][i]+100*table['Bx'][i]],[table['YSC'][i],table['YSC'][i]+100*table['By'][i]],color=c)
    #add circle to represent venus
    add_venus(ax)
    #square axes
    ax.axis('equal')
    ax.set(title='VEX Orbit MAG Data: '+time_range_str)
    plt.show()
    
def add_venus(ax):
    #make venus orange circle w/ accepted venus radius, 6051.8 km
    venus = plt.Circle((0,0), 6051.8,color=(1,165/255,0))
    ax.add_artist(venus)