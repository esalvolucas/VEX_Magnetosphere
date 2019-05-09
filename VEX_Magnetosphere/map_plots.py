from VEX_Magnetosphere import *
import _pickle as cPickle

def map_plots(start_date,end_date,append=None,slicedir=None):
    #print time range plotted
    print(start_date + ' TO ' + end_date)
    #create title string for date range
    title_yr = str(start_date) + ' TO ' + str(end_date)
    dimtick = 0
    #for each projection
    for dim in [['YSC','ZSC'],['XSC','ZSC'],['XSC','YSC']]:
        print(dimtick)

        #grab names of pkl files
        x_pkl_name = start_date[0:10]+'_'+end_date[0:10]+'_Bx_'+dim[0]+'_'+dim[1]+"_"+append
        y_pkl_name = start_date[0:10]+'_'+end_date[0:10]+'_By_'+dim[0]+'_'+dim[1]+"_"+append
        z_pkl_name = start_date[0:10]+'_'+end_date[0:10]+'_Bz_'+dim[0]+'_'+dim[1]+"_"+append
        b_pkl_name = start_date[0:10]+'_'+end_date[0:10]+'_B_'+dim[0]+'_'+dim[1]+"_"+append

        print(x_pkl_name,y_pkl_name,z_pkl_name)       
        #grab full file paths
        x_pkl_name2D = "./VEX_data_files/VSE/VEX_bin_" + x_pkl_name + "_2D.pkl"
        y_pkl_name2D = "./VEX_data_files/VSE/VEX_bin_" + y_pkl_name + "_2D.pkl"
        z_pkl_name2D = "./VEX_data_files/VSE/VEX_bin_" + z_pkl_name + "_2D.pkl"
        b_pkl_name2D = "./VEX_data_files/VSE/VEX_bin_" + b_pkl_name + "_2D.pkl"

        #load pickle files 2D
        xpkl = open(x_pkl_name2D,"rb")
        ypkl = open(y_pkl_name2D,"rb")
        zpkl = open(z_pkl_name2D,"rb")
        bpkl = open(b_pkl_name2D,"rb")
        X = cPickle.load(xpkl)
        Y = cPickle.load(ypkl)
        Z = cPickle.load(zpkl)
        B = cPickle.load(bpkl)
        
        #set plot directory path
        #plot_dir = r'C:/Users/Elysia/Pictures/VEX Plots/gif/'
        plot_dir = r'/Users/ellu2839/Pictures/VEX_Plots/'
        
        #depending on projection, plot the binned data
        if dimtick == 0:
            bin_3d(X,Y,Z,dim='x',v_toggle='off',save=True,name=plot_dir+x_pkl_name,title=title_yr,bs='on')
        elif dimtick == 1:
            bin_3d(Y,X,Z,dim='y',v_toggle='off',save=True,name=plot_dir+y_pkl_name,title=title_yr,bs='on')
        elif dimtick == 2:
            bin_3d(Z,X,Y,dim='z',v_toggle='off',save=True,name=plot_dir+z_pkl_name,title=title_yr,bs='on')
        
        #pick projection of slice
        if slicedir=='XSC' and dimtick==0:
            bin_3d(B,Y,Z,dim='x',v_toggle='off',save=True,name=plot_dir+b_pkl_name,title=title_yr,bs='on',magB=True)
        elif slicedir=='YSC' and dimtick==1:
            bin_3d(B,X,Z,dim='y',v_toggle='off',save=True,name=plot_dir+b_pkl_name,title=title_yr,bs='on',magB=True)
        if slicedir=='ZSC' and dimtick==2:
            bin_3d(B,X,Y,dim='z',v_toggle='off',save=True,name=plot_dir+b_pkl_name,title=title_yr,bs='on',magB=True)

        dimtick += 1

    xpkl.close()
    ypkl.close()
    zpkl.close()
    bpkl.close()