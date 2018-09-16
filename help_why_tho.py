

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def vex_load_data(filename,disp=False):
    #remove column wrapping output
    pd.set_option('display.width', None)
    #open file, read into pandas dataframe
    with open(filename) as f:
        table = pd.read_csv(f,delim_whitespace=True,index_col=0,header=None,names = ['UTC','Bx','By','Bz','|B|','XSC','YSC','ZSC','RSC'],skiprows=177)
    #clip outliers
    table[(table>=99999)|(table<=-99999)] = np.nan
    #set UTC column to datetimeindex
    table = table.set_index(pd.DatetimeIndex(table.index))
    if disp==True:
        print(table)
    return table

def vex_plot_data(table):
    #MAG PLOTTING
    #construct plot title with time range
    plot_title = "VEX MAG Data: " + str(np.array(table.index.values[0], dtype='datetime64[s]')) + ' to ' + str(np.array(table.index.values[-1], dtype='datetime64[s]'))
    
    #initialize subplotting
    fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1,sharex=True, sharey=True)
    #plot B x/y/z on same plot, remove xaxis labels, add plot title
    table[['Bx','By','Bz']].plot(ax=ax1,style=['r','g','b'],linewidth=0.25)
    ax1.set(title=plot_title, xlabel='UTC', ylabel='B field (nT)')
    ax1.legend(loc=1)
    ax1.get_xaxis().set_visible(False)
    #plot |B| on subplot
    table[['|B|']].plot(ax=ax2,subplots=True,style=['k'],linewidth=0.25)
    ax2.set(xlabel='UTC', ylabel='|B| field (nT)')
    ax2.legend(loc=1)
    #show plot
    
    plt.show()
    
    #LOCATION PLOTTING
    #initialize subplotting
    fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1,sharex=True, sharey=True)
    #plot B x/y/z on same plot, remove xaxis labels, add plot title
    table[['XSC','YSC','ZSC']].plot(ax=ax1,style=['m','y','c'],linewidth=1)
    ax1.set(title=plot_title, xlabel='UTC', ylabel='SC Location (km)')
    ax1.legend(loc=1)
    ax1.get_xaxis().set_visible(False)
    #plot |B| on subplot
    table['RSC'].plot(ax=ax2,subplots=True,style=['k'],linewidth=1)
    ax2.set(xlabel='UTC', ylabel='SC Radius (km)')
    ax2.legend(loc=1)
    #show plot
    plt.show()
    
table = vex_load_data('MAG_20071004_DOY277_D001_V1.TAB', disp=True)
vex_plot_data(table)