#PLOTS VEX DATA

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def vex_plot_data(table):
    #MAG PLOTTING
    #construct plot title with time range
    plot_title = "VEX MAG Data: " + str(np.array(table.index.values[0], dtype='datetime64[s]')) + ' to ' + str(np.array(table.index.values[-1], dtype='datetime64[s]'))
    
    #initialize subplotting
    fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1,sharex=True, sharey=False)
    #plot B x/y/z on same plot, remove xaxis labels, add plot title
    table[['Bx','By','Bz']].plot(ax=ax1,style=['b','g','r'],linewidth=0.25)
    ax1.axhline(y=0, linestyle='--', color='k')
    ax1.set(title=plot_title, xlabel='UTC', ylabel='B field (nT)')
    ax1.legend(loc=1)
    ax1.get_xaxis().set_visible(False)
    #plot |B| on subplot
    table[['|B|']].plot(ax=ax2,subplots=True,style=['k'],linewidth=0.25)
    ax2.set(xlabel='UTC', ylabel='|B| field (nT)', ylim=[0,50])
    ax2.legend(loc=1)
    #show plot
    
    plt.show()
    
#     #LOCATION PLOTTING
#     #initialize subplotting
#     fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1,sharex=True, sharey=True)
#     #plot B x/y/z on same plot, remove xaxis labels, add plot title
#     table[['XSC','YSC','ZSC']].plot(ax=ax1,style=['m','y','c'],linewidth=1)
#     ax1.set(title=plot_title, xlabel='UTC', ylabel='SC Location (km)')
#     ax1.legend(loc=1)
#     ax1.get_xaxis().set_visible(False)
#     #plot |B| on subplot
#     table['RSC'].plot(ax=ax2,subplots=True,style=['k'],linewidth=1)
#     ax2.set(xlabel='UTC', ylabel='SC Radius (km)')
#     ax2.legend(loc=1)
#     #show plot
#     plt.show()
    fig, (ax1,ax2,ax3) = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True)
    ax1.plot(table['XSC'],table['YSC'], color = 'c')
    ax1.set(xlabel='VSO X', ylabel='VSO Y')

    ax2.plot(table['XSC'],table['ZSC'], color = 'y')
    ax2.set(xlabel='VSO X', ylabel='VSO Z', title = "VEX Trajectory")

    ax3.plot(table['YSC'],table['ZSC'], color = 'm')
    ax3.set(xlabel='VSO Y', ylabel='VSO Z')

    plt.show()

    fig, (ax1,ax2,ax3) = plt.subplots(nrows=1, ncols=3, sharex=False, sharey=True)
    ax1.plot(table['XSC'],np.sqrt((table['YSC'])**2 + (table['ZSC'])**2),color='c')
    ax1.set(xlabel = 'VSO X', ylabel = r'VSO $\sqrt{Y^2 + Z^2}$')
    ax2.plot(table['YSC'],np.sqrt((table['XSC'])**2 + (table['ZSC'])**2),color='y')
    ax2.set(xlabel = 'VSO Y', ylabel = r'VSO $\sqrt{X^2 + Z^2}$',title='VEX Trajectory')
    ax3.plot(table['ZSC'],np.sqrt((table['XSC'])**2 + (table['YSC'])**2),color='m')
    ax3.set(xlabel = 'VSO Z', ylabel = r'VSO $\sqrt{X^2 + Y^2}$')

    plt.show()