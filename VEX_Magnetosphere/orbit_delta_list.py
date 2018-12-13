from pandas.tslib import Timestamp
from datetime import timedelta



def orbit_delta_list(start_time,end_time):
    orbits=[]
    s_ts = Timestamp(start_time)
    e_ts = Timestamp(end_time)
    delta = e_ts - s_ts
    for i in range(delta.days + 1):
        orbits = orbits + [str(s_ts + timedelta(i))]
         
    return orbits