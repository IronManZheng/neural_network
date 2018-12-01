import numpy as np
import matplotlib.pylab as mplb

def test_mySigmoid(x):
    return 1/(1 + np.exp(-x))

x = np.arange(-5,5,0.1)
y = test_mySigmoid(x)

mplb.plot(x,y)
mplb.ylim(-0.01,1)
mplb.show()