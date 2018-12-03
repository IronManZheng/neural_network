#import numpy as np
#import matplotlib.pylab as mplb
import numpy as np
import matplotlib.pylab as mplb

def testreLU(x):
    return np.maximum(0,x) #当x小于0时，只返回0，否则就返回它本身

x = np.arange(-5,5.1,0.1)
#x = 5
y = testreLU(x)
print(y)
mplb.plot(x,y)
mplb.ylim(-0.1,5)
mplb.show()