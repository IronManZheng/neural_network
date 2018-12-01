import numpy as np
import matplotlib.pylab as mplb

def first_sigmoid(x):
    return 1/(1 + np.exp(-x))

x = np.arange(-5,5,0.1)
y = first_sigmoid(x)
z = first_sigmoid(y)
w = first_sigmoid(z)

mplb.plot(x,w)
mplb.ylim(-0.1,1.1)
mplb.show()