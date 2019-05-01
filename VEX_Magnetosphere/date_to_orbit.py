import pandas as pd
from datetime import datetime

def date_to_orbit(date):
    #establish path to orbit reference file
    filename = "./VEX_data_files/orbit_ref.tab"
    #open orbit reference file into pandas dataframe
    with open(filename) as f:
        orbit_ref = pd.read_csv(f,sep='\t',header=None,names = ['orbit','start','end','BS_in','BS_out'])
    #find orbit start and end times from whole file
    orbit_ref['start'] = pd.to_datetime(orbit_ref['start']) 
    orbit_ref['end'] = pd.to_datetime(orbit_ref['end'])  
    #make desired date a datetime instead of a string
    date = datetime(int(date[0:4]),int(date[5:7]),int(date[8:10]))
    
    #for each orbit in orbit reference file
    for i in orbit_ref.index:
        #if desired date is within two orbits, break
        if (date >= orbit_ref['start'][i]) and (date <= orbit_ref['end'][i]):
            orbit_num = orbit_ref['orbit'][i]
            break
    f.close()
    #return orbit number of date
    return orbit_num