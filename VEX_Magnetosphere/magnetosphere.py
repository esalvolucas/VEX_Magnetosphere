import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
from VEX_Magnetosphere import *

def magnetosphere(table):
    #model bow shock
    L = 1.303
    epsilon = 1.056
    x0 = 0.788
    x = table['XSC'].values/6051.8
    
    #print(table.iloc[11653])

    rho = np.sqrt((table['YSC'].values/6051.8)**2 + (table['ZSC'].values/6051.8)**2)
    BS = 1.1*np.sqrt(L**2 - 2*epsilon*(x-x0)*L - (epsilon**2 - 1)*(x-x0)**2) #10% safety buffer
    
    a = BS - rho
    minInd = argrelextrema(abs(a), np.less)
    print(minInd)
    #print(np.where((BS - rho)==a))
    #print(table.iloc[11653])
    
    fig,ax = plt.subplots(nrows=1, ncols=1)
    
    for i in minInd[0]:
        if a[i+1] <= 0:
            dir = 'out'
            CA_select_out = table.iloc[i:i+60]
            plt.plot(x[i:i+60],rho[i:i+60],'*')
        else:
            dir = 'in'
            CA_select_in = table.iloc[i-60:i]
            plt.plot(x[i-60:i],rho[i-60:i],'*')
        print(dir)
       
    #print(table.iloc[11653])
 
    print(CA_select_in)
    
    print(CA_select_in['Clock'].mean())
    #plt.plot(x[minInd],BS[minInd],'*')
    #plt.plot(x[minInd],rho[minInd],'*')
    plt.plot(x,BS)
    plt.plot(x,-BS)
    plt.plot(x,rho)
    add_venus_2D((0,0), radius=1, angle=90, ax=ax, colors=('k','w'))
    ax.set_facecolor('xkcd:slate grey')
    plt.axis('equal')
    plt.show()
    
    return CA_select_in, CA_select_out