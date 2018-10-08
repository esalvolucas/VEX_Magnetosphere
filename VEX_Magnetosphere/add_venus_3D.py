import numpy as np

def add_venus_3D(ax):
    # Create a sphere
    r = 1
    pi = np.pi
    cos = np.cos
    sin = np.sin
    phi, theta = np.mgrid[0.0:0.5*pi:90j, 0.0:2.0*pi:360j] # phi = alti, theta = azi
    #plot nightside
    z = -r*sin(phi)*cos(theta)
    y = r*sin(phi)*sin(theta)
    x = -r*cos(phi)    
    ax.plot_surface(
        x, y, z,  rstride=4, cstride=4, color='b', alpha=0.1, linewidth=0)    
    ax.plot_wireframe(x, y, z, color="k")
    #plot dayside
    z = r*sin(phi)*cos(theta)
    y = r*sin(phi)*sin(theta)                    
    x = r*cos(phi) 
    ax.plot_surface(
        x, y, z,  rstride=4, cstride=4, color='w', alpha=0.1, linewidth=0)    
    ax.plot_wireframe(x, y, z, color="w")