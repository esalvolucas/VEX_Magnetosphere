
from __future__ import division
import numpy
import glob
import os

def mag_concat(start_date,end_date):
    #send data to separate file
    catfilename = start_date + '_TO_' + end_date + '.tab'
    print('Sending data to: ' + catfilename)
    
    #for each file in MAG data directory path
    for filename in glob.iglob("/Volumes/Venus_Express/calibrated_level_3/**/DATA/**/*.TAB",recursive=True):
        #remove hyphens
        reg_start = start_date.replace('-','')
        reg_end = end_date.replace('-','')
        
        #find files in between start/stop times
        if (filename[90:98] >= reg_start) and (filename[90:98] <= reg_end):
            #print(filename)
        
            #read in data from file
            fin = open(filename, "r", encoding='iso-8859-1' )
            data_list = fin.readlines()
            fin.close()
                    
            #remove header, append to new file
            fout = open(catfilename, "a")
            fout.writelines(data_list[227:])
            fout.close()
            
    #replace any instances of HH:MM:60.000 with HH:MM:59.999
    with open(catfilename) as f:
        newText=f.read().replace(':60.000', ':59.999')
    with open(catfilename, "w") as f:
        f.write(newText)
    
    return catfilename
