import numpy as np
import matplotlib.pylab as plb

def sigmoid(x):
    return 1 /  (1 + np.exp(-x))

x = np.arange(-10,10,0.1)
y = sigmoid(x)

plb.plot(x,y)
plb.show()

