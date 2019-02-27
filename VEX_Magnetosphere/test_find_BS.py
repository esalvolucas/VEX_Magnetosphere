import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from VEX_Magnetosphere import *

def test_find_BS(orbit):
    dates_file = './VEX_data_files/' + orbit[0:10] + '_TO_' + orbit[0:10] + '.tab' 
    #LOAD DATA INTO PANDAS DATAFRAME
    table = vex_load_data(dates_file,disp=False)
    table = table.resample('T').mean()
    table = clock_cone_angle(table)
    #plt.plot(table['Clock'])
        
        
    table['XSC'] = table['XSC']/6051.8
    table['YSC'] = table['YSC']/6051.8
    table['ZSC'] = table['ZSC']/6051.8
    table['RSC'] = table['RSC']/6051.8
     
    print(table)
       
 
    CA_select_in,CA_select_out = magnetosphere(table)
    #table = aberration(table)
    #print(table.iloc[0:10])
    #VSE_table = VSO_to_VSE(table,CA_select_in,CA_select_out)
    
    L = 1.303
    epsilon = 1.056
    x0 = 0.788
    x = table['XSC'].values
    rho = np.sqrt((table['YSC'].values)**2 + (table['ZSC'].values)**2)

    BS = []
    for xval in x:
        #if VEX is outside of the BS (past the subsolar point), BS = 0
        if xval > 1.39:
            xx = 0
        else:
            xx = 1.1*np.sqrt(L**2 - 2*epsilon*(xval-x0)*L - (epsilon**2 - 1)*(xval-x0)**2) #10% safety buffer
        BS = BS + [xx]
        
    a = BS - rho
    #print(a)
    #print(type(a))
    a_table = pd.DataFrame(data={'time':table.index,'BS-rho':list(a)})
    #print(a_table)
    a_table = a_table.set_index('time')
    #table = pd.concat([table, a_table], axis=1)

    table = table.join(a_table)
    
    for time in table.index:
        if (table['BS-rho'][time]<0):
            table['Bx'][time] = 10000
            table['By'][time] = 10000
            table['Bz'][time] = 10000
            table['|B|'][time] = 10000
    
    BS = np.array(BS)
    #x = np.arange(-3,3,0.001)
    #plt.plot(x,BS,color='k')#,linestyle=':')
    #plt.plot(x,-BS,color='k')#,linestyle=':')
    #plt.plot(x,table['YSC'].values)
    #plt.plot(x[np.where(table['BS-rho']>0)],table['YSC'].values[np.where(table['BS-rho']>0)])
    #plt.plot(x[np.where(table['BS-rho']<0)],table['YSC'].values[np.where(table['BS-rho']<0)])

    #plt.show()
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x,BS,np.zeros(1440),color='k')
    ax.plot(x,np.zeros(1440),BS,color='k')
    ax.plot(x,-BS,np.zeros(1440),color='k')
    ax.plot(x,np.zeros(1440),-BS,color='k')
    ax.plot(x,BS,BS,color='k')
    ax.plot(x,BS,-BS,color='k')
    ax.plot(x,-BS,BS,color='k')
    ax.plot(x,-BS,-BS,color='k')
    BS_YZ = plt.Circle((0,0),1.9727,color='k',linestyle=":",fill=False)
    ax.add_artist(BS_YZ)
    ax.scatter(x[np.where(table['BS-rho']<0)],table['YSC'].values[np.where(table['BS-rho']<0)],table['ZSC'].values[np.where(table['BS-rho']<0)])
    plt.show()

    print('wut')
    
test_find_BS('2014-11-14')
            
    