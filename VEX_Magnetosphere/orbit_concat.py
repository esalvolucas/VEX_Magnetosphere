import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from VEX_Magnetosphere import *

def orbit_concat():
    #if need to print dataframe, don't wrap
    pd.set_option('display.width', None)
    #establish date ranges, one normal and one shifted for file creation (all 8 years standard)
    days = pd.date_range('2006-04-24 00:00:00','2014-11-25 00:00:00',freq='D').astype(str).tolist()
    days_shift = pd.date_range('2006-04-25 00:00:00','2014-11-26 00:00:00',freq='D').astype(str).tolist()

    #start with orbit number 0000
    orbit_number = 0

    #for each day in range
    for d,val in enumerate(days):
        #create 4-digit orbit number
        orbit_str = str(orbit_number).zfill(4)
        #pick two files for day and day+1
        file1 = './VEX_data_files/' + days[d][0:10] + '_TO_' + days[d][0:10] + '.tab'
        file2 = './VEX_data_files/' + days_shift[d][0:10] + '_TO_' + days_shift[d][0:10] + '.tab'
    
        #open and read tables of VSO data
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
            #concatenate day and day+1 files
            full_table = pd.concat([table1,table2])
            #downsample to 1m cadence through averaging
            full_table = full_table.resample('T').mean()
            #convert from km to Venus radii
            full_table['XSC'] = full_table['XSC']/6051.8
            full_table['YSC'] = full_table['YSC']/6051.8
            full_table['ZSC'] = full_table['ZSC']/6051.8
            full_table['RSC'] = full_table['RSC']/6051.8
            #find max values of spacecraft distance from planet
            maxInd = list(argrelextrema(full_table['RSC'].values, np.greater))
            #create range of indices between 2 maxima
            indlist = np.arange(maxInd[0][0],maxInd[0][1],1)
            #cut down concatenated table to apoapse-apoapse
            orbit_table = full_table.iloc[indlist]
            #correct for aberration
            ab_table = aberration(orbit_table)
            #append clock and cone angles to table
            orbit_table = clock_cone_angle(ab_table)


            #Martinecz bow shock model
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
            
            #find closest spacecraft crossinsg through the BS
            BS_table = orbit_table.iloc[list(argrelextrema(abs(orbit_table['BS-rho'].values), np.less))[0]]
            min_indices = list(argrelextrema(abs(orbit_table['BS-rho'].values), np.less))[0]
            #create list of potential crossings
            i_table = pd.DataFrame(data={'UTC':BS_table.index,'i':np.array(min_indices)})
            i_table = i_table.set_index('UTC')
            potential_crossings = BS_table.join(i_table)
            #sort list to find 2 closest crossings to the BS
            potential_crossings['BS-rho'] = abs(potential_crossings['BS-rho'])
            potential_crossings = potential_crossings.sort_values(['BS-rho'])
            BS_crossings = potential_crossings.iloc[[0,1]]
            BS_i = np.sort(BS_crossings['i'].values)
            #establish outfile with BS crossing indices in filename
            outfile = "./VEX_data_files/VSE/ORBIT_" + orbit_str + "_BS_" + str(BS_i[0]) + "_" + str(BS_i[1]) + ".tab"
            print(outfile)
            #select hour of data outside the BS on either side of the orbit
            CA_select_in = orbit_table.iloc[BS_i[0]-60:BS_i[0]]
            CA_select_out = orbit_table.iloc[BS_i[1]:BS_i[1]+60]
            #rotate to VSE from VSO
            VSE_table = rotate_to_VSE(orbit_table,BS_i[0],BS_i[1],CA_select_in,CA_select_out)
            #write VSE data to csv, tab delimited
            VSE_table.to_csv(outfile,header=None,sep='\t')
        except:
            print('table fail')
        #for each orbit, write start, end, and BS crossings to file for date_to_orbit reference
        orbit_ref = pd.DataFrame(data={'orbit':[orbit_str],'start':[orbit_table.index[0]],'end':[orbit_table.index[-1]],'BS_in':BS_i[0],'BS_out':BS_i[1]})
        #write/append to orbit reference file
        with open('./VEX_data_files/orbit_ref.tab', 'a') as f:
            orbit_ref.to_csv(f,header=False,sep='\t',index=False)
        #add orbit number
        orbit_number += 1
        f1.close()
        f2.close()
    f.close()
    

# def orbit_concat():
#     #if need to print dataframe, don't wrap
#     pd.set_option('display.width', None)
#     #establish date ranges, one normal and one shifted for file creation (all 8 years standard)
#     days = pd.date_range('2006-04-24 00:00:00','2014-11-25 00:00:00',freq='D').astype(str).tolist()
#     days_shift = pd.date_range('2006-04-25 00:00:00','2014-11-26 00:00:00',freq='D').astype(str).tolist()
# 
#     #start with orbit number 0000
#     orbit_number = 0
#     swdata = read_sw(flag=[0,1])
#     #for each day in range
#     for d,val in enumerate(days):
#         #create 4-digit orbit number
#         orbit_str = str(orbit_number).zfill(4)
#         #pick two files for day and day+1
#         file1 = './VEX_data_files/' + days[d][0:10] + '_TO_' + days[d][0:10] + '.tab'
#         file2 = './VEX_data_files/' + days_shift[d][0:10] + '_TO_' + days_shift[d][0:10] + '.tab'
#     
#         #open and read tables of VSO data
#         try:
#             with open(file1) as f1:
#                 table1 = pd.read_csv(f1,delim_whitespace=True,index_col=0,header=None,names = ['UTC','Bx','By','Bz','|B|','XSC','YSC','ZSC','RSC'])
#             table1[(table1>=99999)|(table1<=-99999)] = np.nan
#             table1 = table1.set_index(pd.DatetimeIndex(table1.index))
#             
#             with open(file2) as f2:
#                 table2 = pd.read_csv(f2,delim_whitespace=True,index_col=0,header=None,names = ['UTC','Bx','By','Bz','|B|','XSC','YSC','ZSC','RSC'])
#             table2[(table2>=99999)|(table2<=-99999)] = np.nan
#             table2 = table2.set_index(pd.DatetimeIndex(table2.index))
#         except:
#             print('DATE FILE NOT FOUND')
#         
#         #try:
#         #concatenate day and day+1 files
#         full_table = pd.concat([table1,table2])
#         #downsample to 1m cadence through averaging
#         full_table = full_table.resample('T').mean()
#         #convert from km to Venus radii
#         full_table['XSC'] = full_table['XSC']/6051.8
#         full_table['YSC'] = full_table['YSC']/6051.8
#         full_table['ZSC'] = full_table['ZSC']/6051.8
#         full_table['RSC'] = full_table['RSC']/6051.8
#         #find max values of spacecraft distance from planet
#         maxInd = list(argrelextrema(full_table['RSC'].values, np.greater))
#         #create range of indices between 2 maxima
#         indlist = np.arange(maxInd[0][0],maxInd[0][1],1)
#         #cut down concatenated table to apoapse-apoapse
#         orbit_table = full_table.iloc[indlist]
#         #correct for aberration
#         ab_table = aberration(orbit_table)
#         #append clock and cone angles to table
#         orbit_table = clock_cone_angle(ab_table)
# 
# 
#         #Martinecz bow shock model
#         L = 1.303
#         epsilon = 1.056
#         x0 = 0.788
#         x = orbit_table['XSC'].values
#         
#         #spacecraft location sqrt(YSC^2 + ZSC^2)
#         rho = np.sqrt((orbit_table['YSC'].values)**2 + (orbit_table['ZSC'].values)**2)
#         BS = []
#         for xval in x:
#             #if VEX is outside of the BS (past the subsolar point), BS = 0
#             if xval > 1.39:
#                 xx = 0
#             else:
#                 xx = 1.1*np.sqrt(L**2 - 2*epsilon*(xval-x0)*L - (epsilon**2 - 1)*(xval-x0)**2) #10% safety buffer
#             BS = BS + [xx]
#         a = BS - rho
#         #concatenate BS-rho onto existing dataframe
#         a_table = pd.DataFrame(data={'time':orbit_table.index,'BS-rho':list(a)})
#         a_table = a_table.set_index('time')
#         orbit_table = orbit_table.join(a_table)
#         
#         #find closest spacecraft crossinsg through the BS
#         BS_table = orbit_table.iloc[list(argrelextrema(abs(orbit_table['BS-rho'].values), np.less))[0]]
#         min_indices = list(argrelextrema(abs(orbit_table['BS-rho'].values), np.less))[0]
#         #create list of potential crossings
#         i_table = pd.DataFrame(data={'UTC':BS_table.index,'i':np.array(min_indices)})
#         i_table = i_table.set_index('UTC')
#         potential_crossings = BS_table.join(i_table)
#         #sort list to find 2 closest crossings to the BS
#         potential_crossings['BS-rho'] = abs(potential_crossings['BS-rho'])
#         potential_crossings = potential_crossings.sort_values(['BS-rho'])
#         BS_crossings = potential_crossings.iloc[[0,1]]
#         BS_i = np.sort(BS_crossings['i'].values)
#         #establish outfile with BS crossing indices in filename
#         outfile = "./VEX_data_files/VSE/ORBIT_" + orbit_str + "_BS_" + str(BS_i[0]) + "_" + str(BS_i[1]) + ".tab"
#         print(outfile)
#         #select hour of data outside the BS on either side of the orbit
#         CA_select_in = orbit_table.iloc[BS_i[0]-60:BS_i[0]]
#         CA_select_out = orbit_table.iloc[BS_i[1]:BS_i[1]+60]
#         
#         #rotate to VSE from VSO
#         VSE_table = rotate_to_VSE(orbit_table,BS_i[0],BS_i[1],CA_select_in,CA_select_out)
#         indices = VSE_table.index.values
#         VSE_table['Pressure'] = swdata['pressure'][indices]
#         VSE_table['Speed'] = swdata['speed'][indices]
#         #append solar wind data
#         #VSE_table = VSE_table.join(pd.DataFrame(data={'Pressure':VSE_table['Bx'],'Speed':VSE_table['Bx']}))
#         #VSE_table = append_sw(VSE_table,swdata)
#         #fakedf = pd.DataFrame({'vx':VSE_table['Speed'],'vy':0.0*VSE_table['Speed'],'vz':0.0*VSE_table['Speed'],'|E|':0.0*VSE_table['Speed']})
#         #VSE_table = VSE_table.join(fakedf)
#         print(VSE_table,swdata)
#         for time in VSE_table.index:
# #                 #set aberration angle at Venus (6 degrees) in radians
# #                 theta = -0.104719755
# #                 
# #                 #establish rotation matrix (rotate around z-axis)
# #                 c,s = np.cos(theta), np.sin(theta)
# #                 rot_ab = np.array(((c,-s,0),
# #                                    (s,c,0),
# #                                    (0,0,1)))
# #                 
# #                 
# #                 #rotate magnetic field and location values
# #                 Vx = VSE_table['Speed'][time]
# #                 Vy = 0.0*VSE_table['Speed'][time]
# #                 Vz = 0.0*VSE_table['Speed'][time]
# #                 
# #                 vel_unab = np.array(((Vx),(Vy),(Vz)))
# #                 vel_ab = np.matmul(rot_ab,vel_unab)
# #                 
# #                 VSE_table['vx'][time] = vel_ab[0]
# #                 VSE_table['vy'][time] = vel_ab[1]
# #                 VSE_table['vz'][time] = vel_ab[2]
#             
#             Bx = VSE_table['Bx'][time]
#             By = VSE_table['By'][time]
#             Bz = VSE_table['Bz'][time]
#             vx = VSE_table['vx'][time]
#             vy = VSE_table['vy'][time]
#             vz = VSE_table['vz'][time]
#             print(Bx,By,Bz,vx,vy,vz)
#             E = np.abs(np.cross(-1000*[-vx,vy,vz],(10**-9)*[Bx,By,Bz]))
#             VSE_table['|E|'][time] = E
#         #write VSE data to csv, tab delimited
#         VSE_table.to_csv(outfile,header=None,sep='\t')
#         #except:
#         #    print('table fail')
#         #for each orbit, write start, end, and BS crossings to file for date_to_orbit reference
#         orbit_ref = pd.DataFrame(data={'orbit':[orbit_str],'start':[orbit_table.index[0]],'end':[orbit_table.index[-1]],'BS_in':BS_i[0],'BS_out':BS_i[1]})
#         #write/append to orbit reference file
#         with open('./VEX_data_files/orbit_ref.tab', 'a') as f:
#             orbit_ref.to_csv(f,header=False,sep='\t',index=False)
#         #add orbit number
#         orbit_number += 1
#         f1.close()
#         f2.close()
#     f.close()
# orbit_concat()