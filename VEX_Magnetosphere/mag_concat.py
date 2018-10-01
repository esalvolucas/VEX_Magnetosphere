
from __future__ import division
import numpy
import glob
import os

def mag_concat(start_date,end_date):
    #send data to separate file
    catfilename = 'VEX_data_files/' + start_date[0:10] + '_TO_' + end_date[0:10] + '.tab'
    if not os.path.isfile(catfilename):
        print('Sending data to: ' + catfilename)
        start_day = start_date[0:10]
        end_day = end_date[0:10]
        #for each file in MAG data directory path
        #MAC
        #dir_path = "/Volumes/Venus_Express/calibrated_level_3/**/DATA/**/*.TAB"
        #WINDOWS
        dir_path = "D:/calibrated_level_3/**/DATA/**/*.TAB"
        for filename in glob.iglob(dir_path,recursive=True):
            #remove hyphens
            reg_start = start_day.replace('-','')
            reg_end = end_day.replace('-','')
            filedate = (os.path.basename(filename))[4:12]
            #find files in between start/stop times
            if (filedate >= reg_start) and (filedate <= reg_end):
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
