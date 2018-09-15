#READS VEX MAG DATA FROM FILES


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#with open('MAG_20071004_DOY277_D001_V1.TAB') as f:
pd.set_option('display.width', None)
with open('MAG_20071004_DOY277_D001_V1.TAB') as f:
    table = pd.read_csv(f,delim_whitespace=True,index_col=0,header=None,names = ['UTC','Bx','By','Bz','|B|','XSC','YSC','ZSC','RSC'],skiprows=177)
    #df = pd.DataFrame(table, columns=['A', 'B', 'C', 'D'])

table[(table>=99999)|(table<=-99999)] = np.nan
table = table.set_index(pd.DatetimeIndex(table.index))
#table = table.resample('T')
#print(table)
#table = table.clip(upper=4.1)
#print(table['Bx'])
#print(table.index.values)
#plt.plot(table.index, table['Bx'].values)
fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1)
table[['Bx','By','Bz']].plot(ax=ax1,style=['r','g','b'],linewidth=0.25)
ax1.set(xlabel='x-label', ylabel=r'$\beta$ field (nT)')
ax1.legend(loc=1)
#ax1.ylabel(r'|$\beta$| field (nT)')
table[['|B|']].plot(ax=ax2,subplots=True,style=['k'],linewidth=0.25)
ax2.set(xlabel='x2-label', ylabel=r'|$\beta$| field (nT)')
ax2.legend(loc=1)
#plt.ylabel(r'$\beta$ field (nT)')
plt.show()

#ax1.set_title('ax1 title')
#ax2.set_title('ax2 title')
print('sorry')