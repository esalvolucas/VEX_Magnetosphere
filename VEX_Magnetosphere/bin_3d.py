import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy import stats


def bin_3d(table):
    #Setup some dummy data
    points = np.random.randn(1000,3)
    bx = np.array(table['Bx'].values)
    by = np.array(table['By'].values)
    bz = np.array(table['Bz'].values)
    print(bx[0])
    print(by[0])
    print(bz[0])
    bxyz = (np.vstack((bx.T,by.T,bz.T))).T
    print(bxyz)
    points = bxyz
    hist, binedges = np.histogramdd(points, normed=False)
    
    #Setup a 3D figure and plot points as well as a series of slices
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.plot(points[:,0],points[:,1],points[:,2],'k.',alpha=0.3)
    
    #Use one less than bin edges to give rough bin location
    X, Y = np.meshgrid(binedges[0][:-1],binedges[1][:-1])
    
    #Loop over range of slice locations (default histogram uses 10 bins)
    for ct in [0,2,5,7,9]: 
        cs = ax1.contourf(X,Y,hist[:,:,ct], 
                          zdir='z', 
                          offset=binedges[2][ct], 
                          level=100, 
                          cmap=plt.cm.RdYlBu_r, 
                          alpha=0.5)
    
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-3, 3)
    ax1.set_zlim(-3, 3)
    plt.colorbar(cs)
    plt.show()