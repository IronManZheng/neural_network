import basepackage

def checkX(x):
    return basepackage.np.array(x > 0,dtype=basepackage.np.int)

x = basepackage.np.arange(-5,5,0.1)
y = checkX(x)
basepackage.mplb.plot(x,y)
basepackage.mplb.ylim(-0.1,1.1)
basepackage.mplb.show()
