import pandas as pd
from datetime import datetime

def date_to_orbit(date):
    filename = "./VEX_data_files/orbit_ref.tab"
    with open(filename) as f:
        orbit_ref = pd.read_csv(f,sep='\t',header=None,names = ['orbit','start','end','BS_in','BS_out'])
    orbit_ref['start'] = pd.to_datetime(orbit_ref['start']) 
    orbit_ref['end'] = pd.to_datetime(orbit_ref['end'])  
    #print(date[0:4],date[5:7],date[8:10])
    date = datetime(int(date[0:4]),int(date[5:7]),int(date[8:10]))
    
    for i in orbit_ref.index:
        if (date >= orbit_ref['start'][i]) and (date <= orbit_ref['end'][i]):
            orbit_num = orbit_ref['orbit'][i]
            break
    return orbit_num