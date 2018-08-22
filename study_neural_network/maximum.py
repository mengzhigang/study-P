#ReLU函数
import numpy as np
import matplotlib.pylab as plb

def maximum(x):
    return np.maximum(0,x)

x = np.arange(-10, 10, 0.1)
y = maximum(x)

plb.plot(x,y)
plb.show()

