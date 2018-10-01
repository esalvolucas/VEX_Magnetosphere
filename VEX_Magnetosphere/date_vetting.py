import VEX_Magnetosphere
import pandas as pd

def date_vetting(table,start_time,end_time):
    #replace extraneous characters in times for float comparison
    stuff_to_replace = ['T','-',' ',':']
        
    start_comp = start_time
    for i in stuff_to_replace:
        start_comp = start_comp.replace(i,'')
    end_comp = end_time
    for i in stuff_to_replace:
        end_comp = end_comp.replace(i,'')
      
    #compare table indices to start/stop times
    drop_i = []  
    for val in table.index:
        print(val)
        table_i = str(val)
        #vet characters to compare
        for i in stuff_to_replace:
            table_i = table_i.replace(i,'')
            
        #if start > table index or stop < table index, note index
        if (float(table_i) < float(start_comp)) or (float(table_i) > float(end_comp)):
            drop_i = drop_i + [val]
    
    #drop extraneous data from table
    table = table.drop(drop_i)
    print(table)
    
    return table