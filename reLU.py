#import numpy as np
#import matplotlib.pylab as mplb
import basepackage

def testreLU(x):
    return basepackage.np.maximum(0,x) #当x小于0时，只返回0，否则就返回它本身

x = basepackage.np.arange(-5,5.1,0.1)
#x = 5
y = testreLU(x)
print(y)
basepackage.mplb.plot(x,y)
basepackage.mplb.ylim(-0.1,5)
basepackage.mplb.show()