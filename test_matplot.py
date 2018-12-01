import numpy as np
import matplotlib.pylab as mlb

x = np.arange(-5,5,0.1)
y = x*x

mlb.plot(x)
mlb.ylim(-5,5)
mlb.show()