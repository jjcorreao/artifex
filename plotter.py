
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def length(x, y, Lx):
    L1 = np.sqrt(x**2 + y**2)
    L2 = np.sqrt((Lx-x)**2 + y**2)
    alpha = np.arcsin(y/L1)
    beta = np.arcsin((L1/L2)*np.sin(alpha))
    return L1, L2, alpha, beta

def tension(L1, L2, alpha, beta, m1, g):
    T2 = (m1*g*np.cos(alpha))/(np.sin(beta)*(np.cos(beta)+np.cos(alpha)))
    T1 = (T2*np.cos(beta))/np.cos(alpha)
    return T1, T2

def fig(x,y,Lx):
    verts = [
    (0, 0), # left, bottom
    (x, y), # left, top
    (Lx, 0), # right, top
    ]

    codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         ]

    path = Path(verts, codes)

    fig = plt.figure()
    ax = plt.gca()

    patch = patches.PathPatch(path, facecolor='orange', lw=1)
    ax.add_patch(patch)
    ax.set_xlim(0,Lx)
    ax.set_ylim(0,Lx)
    fig.gca().invert_yaxis()

    return fig

Lx = 1.5
x = 0.1
# x = np.linspace(1,5,5)
y = 0.5
# y = np.linspace(1,5,)
m1 = 5
g = 1 # ft/s2


figures = {}
# points = []
# codes_all = []

for i in range(len(x)):
    L1, L2, alpha, beta = length(x[i],y[i],Lx)
    T1, T2 = tension(L1, L2, alpha, beta, m1, g)
    figures[i] = fig(x[i],y[i],Lx)
    # points.append((x[i],y[i]))
    # codes_all.append(Path.LINETO)
    # [i] = [(x,y)].append()
    # + {'key': i,
    #        'value': fig(x[i],y[i],Lx)}
    # figures['key'] = i
    # figures['value'] =


#
# print("T1(%s,%s) = %s | T2(%s,%s) = %s | alpha = %s deg | beta = %s deg" % (x,y,T1,x,y,T2,np.rad2deg(alpha),np.rad2deg(beta)))
#
# figure = fig(x,y,Lx)

# verts = [
# (0, 0), # left, bottom
# (x[0], y[0]), # left, top
# (Lx, 0), # right, top
# ]

# codes_all[0] = Path.MOVETO
# path = Path(points, codes_all)
#
# fig = plt.figure()
# ax = plt.gca()
# # ax = plt.figure()
#
# patch = patches.PathPatch(path, lw=1)
# ax.add_patch(patch)
# # ax.plot(figures[0].figure,color='black')
# # ax.plot(figures[1].figure,color='blue')
# # ax.plot(figures[2].figure,color='green')
# ax.set_xlim(0,Lx)
# ax.set_ylim(0,Lx)
# fig.gca().invert_yaxis()
# fig.show()
# ax.show()

# figures[0].show()
# figures[5].show()
# figures[10].show()



