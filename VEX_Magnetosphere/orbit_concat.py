import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from VEX_Magnetosphere import *
from VEX_Magnetosphere.date_to_orbit import *

def orbit_concat():
    
    pd.set_option('display.width', None)
    #days = pd.date_range('2014-02-01 00:00:00','2014-11-25 00:00:00',freq='D').astype(str).tolist()
    #days_shift = pd.date_range('2014-02-02 00:00:00','2014-11-26 00:00:00',freq='D').astype(str).tolist()
    days = pd.date_range('2006-04-24 00:00:00','2014-11-25 00:00:00',freq='D').astype(str).tolist()
    days_shift = pd.date_range('2006-04-25 00:00:00','2014-11-26 00:00:00',freq='D').astype(str).tolist()
    #days = ['2006-04-24 00:00:00','2006-04-25 00:00:00']
    #days_shift = ['2006-04-25 00:00:00','2006-04-26 00:00:00']
    
    orbit_number = 0

    for d,val in enumerate(days):
        orbit_str = str(orbit_number).zfill(4)
        
        file1 = './VEX_data_files/' + days[d][0:10] + '_TO_' + days[d][0:10] + '.tab'
        file2 = './VEX_data_files/' + days_shift[d][0:10] + '_TO_' + days_shift[d][0:10] + '.tab'
    
        try:
            with open(file1) as f1:
                table1 = pd.read_csv(f1,delim_whitespace=True,index_col=0,header=None,names = ['UTC','Bx','By','Bz','|B|','XSC','YSC','ZSC','RSC'])
            table1[(table1>=99999)|(table1<=-99999)] = np.nan
            table1 = table1.set_index(pd.DatetimeIndex(table1.index))
            
            with open(file2) as f2:
                table2 = pd.read_csv(f2,delim_whitespace=True,index_col=0,header=None,names = ['UTC','Bx','By','Bz','|B|','XSC','YSC','ZSC','RSC'])
            table2[(table2>=99999)|(table2<=-99999)] = np.nan
            table2 = table2.set_index(pd.DatetimeIndex(table2.index))
        except:
            print('DATE FILE NOT FOUND')
        
        try:
            full_table = pd.concat([table1,table2])
            full_table = full_table.resample('T').mean()
    
            full_table['XSC'] = full_table['XSC']/6051.8
            full_table['YSC'] = full_table['YSC']/6051.8
            full_table['ZSC'] = full_table['ZSC']/6051.8
            full_table['RSC'] = full_table['RSC']/6051.8
            
            maxInd = list(argrelextrema(full_table['RSC'].values, np.greater))
            #print(np.arange(maxInd[0][0],maxInd[0][1],1))
            indlist = np.arange(maxInd[0][0],maxInd[0][1],1)
            orbit_table = full_table.iloc[indlist]
            orbit_table = clock_cone_angle(orbit_table)
            #print(orbit_table)
            #########################
            #model bow shock
            L = 1.303
            epsilon = 1.056
            x0 = 0.788
            x = orbit_table['XSC'].values
            
            #spacecraft location sqrt(YSC^2 + ZSC^2)
            rho = np.sqrt((orbit_table['YSC'].values)**2 + (orbit_table['ZSC'].values)**2)
            BS = []
            for xval in x:
                #if VEX is outside of the BS (past the subsolar point), BS = 0
                if xval > 1.39:
                    xx = 0
                else:
                    xx = 1.1*np.sqrt(L**2 - 2*epsilon*(xval-x0)*L - (epsilon**2 - 1)*(xval-x0)**2) #10% safety buffer
                BS = BS + [xx]
            a = BS - rho
            #concatenate BS-rho onto existing dataframe
            a_table = pd.DataFrame(data={'time':orbit_table.index,'BS-rho':list(a)})
            a_table = a_table.set_index('time')
            orbit_table = orbit_table.join(a_table)
            
            #print(orbit_table)
            
            ###BS Crossing
            BS_table = orbit_table.iloc[list(argrelextrema(abs(orbit_table['BS-rho'].values), np.less))[0]]
            min_indices = list(argrelextrema(abs(orbit_table['BS-rho'].values), np.less))[0]
    
            i_table = pd.DataFrame(data={'UTC':BS_table.index,'i':np.array(min_indices)})
            i_table = i_table.set_index('UTC')
            potential_crossings = BS_table.join(i_table)
            
            potential_crossings['BS-rho'] = abs(potential_crossings['BS-rho'])
            potential_crossings = potential_crossings.sort_values(['BS-rho'])
            #b1,b2 = potential_crossings[]
            BS_crossings = potential_crossings.iloc[[0,1]]
            BS_i = np.sort(BS_crossings['i'].values)
            
            outfile = "./VEX_data_files/VSE/ORBIT_" + orbit_str + "_BS_" + str(BS_i[0]) + "_" + str(BS_i[1]) + ".tab"
            print(outfile)
            CA_select_in = orbit_table.iloc[BS_i[0]-60:BS_i[0]]
            CA_select_out = orbit_table.iloc[BS_i[1]:BS_i[1]+60]
            VSE_table = rotate_to_VSE(orbit_table,BS_i[0],BS_i[1],CA_select_in,CA_select_out)
            VSE_table.to_csv(outfile,header=None,sep='\t')
        except:
            print('table fail')
            
        #orbit_ref = pd.DataFrame(data={'orbit':[orbit_str],'start':[orbit_table.index[0]],'end':[orbit_table.index[-1]],'BS_in':BS_i[0],'BS_out':BS_i[1]})
        #with open('./VEX_data_files/orbit_ref.tab', 'a') as f:
        #   orbit_ref.to_csv(f,header=False,sep='\t',index=False)
        orbit_number += 1
        f1.close()
        f2.close()
    #f.close()
orbit_concat()