from matplotlib.patches import Wedge


def add_venus_2D(center, radius, angle=0, ax=None, colors=('w','k')):
    #get 2 halves of venus
    theta1, theta2 = angle, angle + 180
    #create wedge items for each half, with each color
    w1 = Wedge(center, radius, theta1, theta2, fc=colors[0])
    w2 = Wedge(center, radius, theta2, theta1, fc=colors[1])
    #add to specified axis
    for wedge in [w1, w2]:
        ax.add_artist(wedge)
        
    return [w1, w2]