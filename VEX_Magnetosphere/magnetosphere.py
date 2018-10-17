import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def magnetosphere(table):
    #model bow shock
    L = 1.303
    epsilon = 1.056
    x0 = 0.788
    x = table['XSC'].values/6051.8
    
    rho = np.sqrt((table['YSC'].values/6051.8)**2 + (table['ZSC'].values/6051.8)**2)
    BS = 1.1*np.sqrt(L**2 - 2*epsilon*(x-x0)*L - (epsilon**2 - 1)*(x-x0)**2) #10% safety buffer
    
    
    plt.plot(x,BS)
    plt.plot(x,-BS)
    plt.plot(x,rho)
    plt.show()