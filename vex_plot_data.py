#PLOTS VEX DATA

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def vex_plot_data(table):
    #construct plot title with time range
    plot_title = "VEX MAG Data: " + str(np.array(table.index.values[0], dtype='datetime64[s]')) + ' to ' + str(np.array(table.index.values[-1], dtype='datetime64[s]'))
    
    #initialize subplotting
    fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1,sharex=True, sharey=True)
    #plot B x/y/z on same plot, remove xaxis labels, add plot title
    table[['Bx','By','Bz']].plot(ax=ax1,style=['r','g','b'],linewidth=0.25)
    ax1.set(title=plot_title, xlabel='UTC', ylabel=r'$\beta$ field (nT)')
    ax1.legend(loc=1)
    ax1.get_xaxis().set_visible(False)
    #plot |B| on subplot
    table[['|B|']].plot(ax=ax2,subplots=True,style=['k'],linewidth=0.25)
    ax2.set(xlabel='UTC', ylabel=r'|$\beta$| field (nT)')
    ax2.legend(loc=1)
    #show plot
    plt.show()