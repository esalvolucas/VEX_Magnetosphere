from __future__ import division
import numpy
import glob
import os
from datetime import timedelta, date


def make_nanfile():
    dir_path = "D:/calibrated_level_3/**/DATA/**/*.TAB"
    current_files = []
    for filename in glob.iglob(dir_path,recursive=True):
        filedate = (os.path.basename(filename))[4:12]
        current_files = current_files + [filedate]
    #print(current_files[0][0:4],current_files[0][4:6],current_files[0][6:8])
    
    all_files = []
    start_file = current_files[0]
    end_file = current_files[-1]
    start_dt = date(int(start_file[0:4]),int(start_file[4:6]),int(start_file[6:8]))
    end_dt = date(int(end_file[0:4]),int(end_file[4:6]),int(end_file[6:8]))
    for dt in daterange(start_dt, end_dt):
        all_files = all_files + [dt.strftime("%Y%m%d")]
    
    #print(len(current_files))
    #print(len(all_files))
    
    full_list = all_files + current_files
    
    diff_list = list(set(all_files) - set(current_files))
    print(len(diff_list))
    print(diff_list)
    a = diff_list[0]
    fakedate = a[0:4] + '-' + a[4:6] + '-' + a[6:8] + 'T' + '12:00:00.000'
    fakedata = fakedate + '    ' + '999999' + '    ' + '999999' + '    ' + '999999' + '    ' + '999999' + '    ' + '999999' + '    ' + '999999' + '    ' + '999999' + '    ' + '999999\n'
    #print('2006-06-01T00:00:00.673    999999    999999     999999      999999    999999    999999    999999    999999')
    fakefilename = 'MAG_' + a + '_DOYnan_Dnan_V1.tab'
    print(fakedata)
    with open(fakefilename, "w") as f:
        i = 0
        while i != 228:
            f.write(fakedata)
            i = i + 1
    
    
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)


    
make_nanfile()
